#!/usr/bin/env python3
"""Trafego OS — métricas do dia. Stdlib puro (python3.9+), sem dependências.

Uso:
  python3 scripts/metrics.py data/processed/norm-YYYYMMDD.csv [--json out.json]
  python3 scripts/metrics.py arquivo.csv --min-impressoes 1000 --z 2.5

Schema esperado (veja data/exemplos/schemas.md):
  dt, platform, nivel, id, nome, impressoes, clicks, spend, conv, revenue[, reach]

Produz: agregados por nível (campaign/adset/ad) com métricas derivadas;
índice de fatigue por criativo (>= 3 dias); anomalias diárias por z-score
(CPA e CTR, |z| > limiar). Tudo em stdout; JSON opcional para os agentes.
"""
import argparse, csv, json, math, sys
from collections import defaultdict

def num(x, default=0.0):
    try:
        x = str(x or "").replace(",", "").replace('"', "").strip()
        return float(x) if x not in ("", "-") else default
    except ValueError:
        return default

def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            rows.append({ (k or "").strip().lower(): v for k, v in r.items() })
    if not rows:
        sys.exit("arquivo vazio: " + path)
    return rows

def agg(rows):
    g = defaultdict(lambda: {"imp": 0.0, "clk": 0.0, "spend": 0.0, "conv": 0.0, "rev": 0.0, "reach": 0.0})
    for r in rows:
        k = (r.get("platform"), r.get("nivel"), r.get("id"), r.get("nome"))
        d = g[k]
        d["imp"] += num(r.get("impressoes")); d["clk"] += num(r.get("clicks"))
        d["spend"] += num(r.get("spend")); d["conv"] += num(r.get("conv"))
        d["rev"] += num(r.get("revenue")); d["reach"] += num(r.get("reach"))
    return g

def m(d):
    out = dict(spend=round(d["spend"], 2), impressions=int(d["imp"]), clicks=int(d["clk"]),
               conv=d["conv"], revenue=round(d["rev"], 2))
    out["ctr"] = round(d["clk"] / d["imp"], 5) if d["imp"] else None
    out["cpm"] = round(d["spend"] / d["imp"] * 1000, 2) if d["imp"] else None
    out["cpc"] = round(d["spend"] / d["clk"], 4) if d["clk"] else None
    out["cpa"] = round(d["spend"] / d["conv"], 2) if d["conv"] else None
    out["roas"] = round(d["rev"] / d["spend"], 3) if d["spend"] else None
    if d["reach"]:
        out["frequency"] = round(d["imp"] / d["reach"], 2)
    return out

def fatigue(rows):
    """fatigue index = CTR ultimos 3 dias / CTR primeiros 3 dias (por criativo)."""
    by_creative = defaultdict(lambda: defaultdict(lambda: [0.0, 0.0]))
    for r in rows:
        if r.get("nivel") not in ("ad", "creative"):
            continue
        by_creative[(r.get("id"), r.get("nome"))][r.get("dt")][0] += num(r.get("impressoes"))
        by_creative[(r.get("id"), r.get("nome"))][r.get("dt")][1] += num(r.get("clicks"))
    res = []
    for (cid, nome), dias in by_creative.items():
        ds = sorted(dias.keys())
        if len(ds) < 3:
            continue
        def ctr_of(days):
            imp = sum(dias[x][0] for x in days); clk = sum(dias[x][1] for x in days)
            return clk / imp if imp else 0.0
        first, last = ctr_of(ds[:3]), ctr_of(ds[-3:])
        if first <= 0:
            continue
        idx = last / first
        res.append({"creative": cid, "nome": str(nome)[:40], "dias": len(ds),
                    "impressoes": int(sum(v[0] for v in dias.values())),
                    "ctr_first3": round(first, 5), "ctr_last3": round(last, 5),
                    "fatigue_index": round(idx, 3),
                    "status": "OK" if idx >= 0.9 else ("ATENCAO" if idx >= 0.7 else "FADIGADO")})
    return sorted(res, key=lambda x: x["fatigue_index"])

def anomalies(rows, zlim):
    """z-score diário de CTR e CPA por criativo contra a própria série."""
    per = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r.get("nivel") not in ("ad", "creative"):
            continue
        imp, clk, sp, cv = num(r.get("impressoes")), num(r.get("clicks")), num(r.get("spend")), num(r.get("conv"))
        if imp and clk:
            per[(r.get("id"), r.get("nome"))]["ctr"].append((r.get("dt"), clk / imp))
        if sp and cv:
            per[(r.get("id"), r.get("nome"))]["cpa"].append((r.get("dt"), sp / cv))
    out = []
    for (cid, nome), series in per.items():
        for metrica, pts in series.items():
            if len(pts) < 3:
                continue
            vals = [v for _, v in pts]
            mean = sum(vals) / len(vals)
            sd = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
            if sd == 0:
                continue
            for dt, v in pts:
                z = (v - mean) / sd
                if abs(z) > zlim:
                    out.append({"creative": cid, "nome": str(nome)[:40], "dt": dt, "metrica": metrica,
                                "valor": round(v, 4), "z": round(z, 2),
                                "direcao": "SUBIU" if z > 0 else "CAIU"})
    return sorted(out, key=lambda x: -abs(x["z"]))[:20]

HEADERS = ["plataforma", "nivel", "id", "nome", "spend", "impressions", "clicks", "ctr", "cpm", "cpc", "conv", "cpa", "revenue", "roas", "frequency"]

def fmt_table(rows, limit=None):
    rr = rows if limit is None else rows[:limit]
    lines = ["| " + " | ".join(HEADERS) + " |", "|" + "---|" * len(HEADERS)]
    for x in rr:
        vals = []
        for h in HEADERS:
            v = x.get(h)
            if v is None:
                vals.append("-")
            elif isinstance(v, float) and v < 1:
                vals.append(f"{v:.4f}")
            else:
                vals.append(str(v))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description="metrics trafego-os")
    ap.add_argument("csv")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--min-impressoes", type=float, default=1000.0)
    ap.add_argument("--z", type=float, default=2.5)
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    rows = load(args.csv)
    g = agg(rows)
    per_level = {}
    for nivel in ("campaign", "adset", "ad"):
        sel = [dict(m(d), plataforma=p, nivel=l, id=i, nome=str(n)[:44])
               for (p, l, i, n), d in g.items() if l == nivel and d["imp"] >= args.min_impressoes]
        per_level[nivel] = sorted(sel, key=lambda x: -x["spend"])
        print(f"\n=== AGREGADO POR {nivel.upper()} (impressoes >= {args.min_impressoes:g}) ===")
        print(fmt_table(per_level[nivel], args.top))

    fat = fatigue(rows)
    print("\n=== FATIGUE INDEX (criativos >= 3 dias) ===")
    if fat:
        print("| criativo | dias | imp | CTR-1sem | CTR-ult | indice | status |")
        print("|---|---|---|---|---|---|---|")
        for f in fat[:30]:
            print(f"| {f['creative']} ({f['nome']}) | {f['dias']} | {f['impressoes']} | "
                  f"{f['ctr_first3']:.3%} | {f['ctr_last3']:.3%} | {f['fatigue_index']:.2f} | {f['status']} |")
    else:
        print("(sem criativos com serie suficiente)")

    an = anomalies(rows, args.z)
    print(f"\n=== ANOMALIAS DIARIAS (|z| > {args.z:g}, top {len(an)}) ===")
    for a in an:
        print(f"  {a['dt']}  {a['metrica'].upper()} {a['direcao']:>5}  z={a['z']:+.2f}  "
              f"val={a['valor']}  criativo={a['creative']} ({a['nome']})")
    if not an:
        print("  nenhuma anomalia acima do limiar (serie curta ou sem picos)")

    if args.json_out:
        payload = {"input": args.csv, "levels": per_level, "fatigue": fat, "anomalies": an}
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print(f"\nJSON gravado: {args.json_out}")

if __name__ == "__main__":
    main()
