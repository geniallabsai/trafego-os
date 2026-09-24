#!/usr/bin/env python3
"""Trafego OS — normaliza exports brutos para o schema comum. Stdlib puro.

Uso:
  python3 scripts/ingest.py data/raw/meta-....csv --out data/processed/norm-YYYYMMDD.csv
  python3 scripts/ingest.py google-....csv --out norm.csv --append
  python3 scripts/ingest.py erp-....csv --out norm.csv --append --fx 5.43

Schema de saida (data/exemplos/schemas.md):
  dt, platform, nivel, id, nome, impressoes, clicks, spend, conv, revenue, reach

Aliases reconhecidos (case-insensitive, variacoes comuns de export):
  date/dia/dt/timestamp · campaign_name/campanha · adset_name/adgroup · ad_name/criativo
  impressions/impressoes · link_clicks/cliques · reach/alcance · cost/gasto/custo
  actions/conversions/purchases · purchase_values/conv_value/receita · value
  --fx converte USD -> BRL quando o export estiver em dolar.
"""
import argparse, csv, sys
from pathlib import Path

COMMON = ["dt", "platform", "nivel", "id", "nome", "impressoes", "clicks", "spend", "conv", "revenue", "reach"]
ALIASES = {
    "dt": ["dt", "date", "dia", "timestamp", "day"],
    "platform": ["platform", "plataforma"],
    "nivel": ["nivel", "level"],
    "id": ["id", "campaign_id", "ad_id", "adset_id", "creative_id"],
    "campaign": ["campaign_name", "campaign", "campanha"],
    "adset": ["adset_name", "adgroup_name", "adgroup", "conjunto_de_anuncios"],
    "ad": ["ad_name", "creative", "criativo", "anuncio"],
    "impressoes": ["impressions", "impressoes"],
    "clicks": ["clicks", "link_clicks", "cliques"],
    "reach": ["reach", "alcance"],
    "spend": ["spend", "cost", "gasto", "custo", "invest"],
    "conv": ["actions", "conversions", "conv", "purchases", "result_conversions"],
    "revenue": ["purchase_values", "purchase_amount", "conv_value", "receita", "revenue", "conversion_value", "value"],
}

def find_col(header, candidates):
    norm = [(c, c.strip().lower().replace("_", " ")) for c in header]
    for cand in candidates:
        for c, cn in norm:
            if cn == cand.replace("_", " "):
                return c
    for cand in candidates:
        for c, cn in norm:
            if cand.replace("_", " ") in cn:
                return c
    return None

def guess_platform(name, header, rows):
    blob = (name + " " + " ".join(header) + " " + " ".join(str(r) for r in rows[:3])).lower()
    if "meta" in blob or "facebook" in blob or "instagram" in blob:
        return "meta"
    if "tiktok" in blob:
        return "tiktok"
    if "google" in blob or "pmax" in blob or "search" in blob or "shopping" in blob or "youtube" in blob or "demand gen" in blob:
        return "google"
    if "pedido" in blob or "order" in blob or "erp" in blob:
        return "erp"
    return "desconhecida"

def clean_num(v):
    try:
        s = str(v or "").replace("R$", "").replace("$", "").replace("%", "").strip()
        if "," in s and "." in s:
            s = s.replace(".", "").replace(",", ".")
        elif "," in s:
            s = s.replace(",", ".")
        return float(s or 0.0)
    except ValueError:
        return 0.0

def pick(r, *cols):
    for c in cols:
        if c and r.get(c) not in (None, ""):
            return r.get(c)
    return ""

def main():
    ap = argparse.ArgumentParser(description="ingest trafego-os")
    ap.add_argument("csv"); ap.add_argument("--out", required=True)
    ap.add_argument("--append", action="store_true")
    ap.add_argument("--platform", default=None)
    ap.add_argument("--fx", type=float, default=None, help="taxa USD->BRL (se export em dolar)")
    args = ap.parse_args()

    src = Path(args.csv)
    with open(src, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f)
        header = [h.strip() for h in (rd.fieldnames or [])]
        raw = list(rd)
    if not raw:
        sys.exit("sem linhas em " + str(src))

    platform = args.platform or guess_platform(src.name, header, raw)
    col = {k: find_col(header, v) for k, v in ALIASES.items()}
    missing = [k for k in ("dt", "spend") if not col.get(k)]
    if missing:
        sys.exit(f"colunas obrigatorias faltando: {missing}; headers vistos: {header}")

    fx = args.fx or 1.0
    warns, out_rows = [], []
    for r in raw:
        dt = (r.get(col["dt"]) or "").strip()[:10]
        if "/" in dt:
            p = dt.split("/"); dt = f"{p[-1]}-{p[0].zfill(2)}-{p[1].zfill(2)}"
        if not dt or ("-") not in dt:
            warns.append(f"dt suspeito ignorado: {dt!r}")
            continue
        nivel = pick(r, col.get("nivel"))
        if not nivel:
            nivel = ("ad" if (col.get("ad") and r.get(col["ad"]))
                     else ("adset" if (col.get("adset") and r.get(col["adset"]))
                           else "campaign"))
        out_rows.append({
            "dt": dt, "platform": platform, "nivel": nivel,
            "id": pick(r, col.get("id")),
            "nome": pick(r, col.get("ad"), col.get("adset"), col.get("campaign"),
                     find_col(header, ["nome", "name"]), col.get("id")),
            "impressoes": clean_num(r.get(col["impressoes"])) if col.get("impressoes") else 0.0,
            "clicks": clean_num(r.get(col["clicks"])) if col.get("clicks") else 0.0,
            "reach": clean_num(r.get(col["reach"])) if col.get("reach") else 0.0,
            "spend": round(clean_num(r.get(col["spend"])) * fx, 2),
            "conv": clean_num(r.get(col["conv"])) if col.get("conv") else 0.0,
            "revenue": round(clean_num(r.get(col["revenue"])) * fx, 2) if col.get("revenue") else 0.0,
        })

    if fx != 1.0:
        warns.append(f"fx aplicada: {fx} (USD->BRL)")
    if platform == "desconhecida":
        warns.append("plataforma nao identificada — use --platform para corrigir")

    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    mode = "a" if (args.append and out.exists()) else "w"
    write_header = mode == "w" or not out.exists()
    with open(out, mode, newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=COMMON, extrasaction="ignore")
        if write_header:
            wr.writeheader()
        wr.writerows(out_rows)
    print(f"[ingest] {src.name} -> {out.name}: {len(out_rows)} linhas ({platform}, fx={fx})")
    for msg in warns[:10]:
        print("  aviso:", msg)

if __name__ == "__main__":
    main()
