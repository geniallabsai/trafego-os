#!/usr/bin/env python3
"""Trafego OS — forecast de custos e vendas em 3 cenarios. Stdlib puro.

Uso (doc 03 e a norma):
  python3 scripts/forecast.py --budget 30000 --cpm 25 --ctr 0.015 --cvr 0.03 \
      --ticket 97 --margem 0.6 [--dias 30] [--repeat 0.25] [--leads-close 0.5]

Parametros:
  --budget     orcamento total do horizonte (BRL)
  --cpm        custo por 1000 impressoes (BRL)
  --ctr        taxa de clique (0-1)
  --cvr        conversao clique->venda direta (0-1); OU
  --cvr-lead + --leads-close  se o funil tem lead intermediario
  --ticket     ticket medio (BRL)
  --margem     margem bruta (0-1) -> ROAS break-even = 1/margem
  --dias       horizonte em dias (padrao 30)
  --repeat     fator de recompra (ex.: 0.3 ~ 30% do ticket extra)
  --nome       rotulo da conta (cOSMETICO)
"""
import argparse

def funil(budget, cpm, ctr, cvr, ticket, margem, repeat=0.0):
    imp = budget / cpm * 1000 if cpm else 0.0
    clicks = imp * ctr
    vendas = clicks * cvr
    receita = vendas * ticket
    roas = receita / budget if budget else 0.0
    cac = budget / vendas if vendas else float("inf")
    be = 1 / margem if margem else float("inf")
    lucro = receita * margem - budget
    ltv = ticket * margem * (1 + repeat)
    ltv_cac = ltv / cac if vendas else float("inf")
    return dict(impressoes=imp, clicks=clicks, vendas=vendas, receita=receita,
                roas=roas, cac=cac, be=be, lucro=lucro, ltv=ltv, ltv_cac=ltv_cac)

def show(nome, f):
    cac = f["cac"]
    cac_s = f"{cac:,.2f}" if cac != float("inf") else "-"
    print(f"  {nome:<11} imp={f['impressoes']:>12,.0f}  cliques={f['clicks']:>10,.0f}  "
          f"vendas={f['vendas']:>8,.0f}  receita=R$ {f['receita']:>13,.2f}  "
          f"ROAS={f['roas']:>5.2f}  CAC=R$ {cac_s:>9}  lucro=R$ {f['lucro']:>13,.2f}")

def main():
    ap = argparse.ArgumentParser(description="forecast trafego-os")
    for a in ("budget", "cpm", "ctr", "cvr", "cvr_lead", "leads_close", "ticket", "margem", "dias", "repeat"):
        ap.add_argument("--" + a.replace("_", "-"), dest=a, type=float, default=None)
    ap.add_argument("--nome", default="conta")
    args = ap.parse_args()

    req = ("budget", "cpm", "ctr", "ticket", "margem")
    if any(getattr(args, k) is None for k in req) or (args.cvr is None and args.cvr_lead is None):
        ap.error("faltam parametros: precisa --budget --cpm --ctr --ticket --margem e --cvr (ou --cvr-lead)")
    cvr = args.cvr if args.cvr is not None else args.cvr_lead * (args.leads_close or 1.0)
    dias = int(args.dias or 30)
    b, c, t, m, rep = args.budget, args.cpm, args.ticket, args.margem, (args.repeat or 0.0)
    be = 1 / m

    print(f"FORECAST {dias}D — {args.nome} | budget R$ {b:,.0f} | CPM R$ {c:.2f} | CTR {args.ctr:.2%} | CVR {cvr:.2%} | ticket R$ {t:,.2f} | margem {m:.0%} | ROAS break-even {be:.2f}")
    print("FUNIL-BASE (declare a origem de cada parametro — regra R8):")
    show("base", funil(b, c, args.ctr, cvr, t, m, rep))
    print("CENARIOS:")
    show("pessimista", funil(b, c * 1.2, args.ctr * 0.85, cvr * 0.8, t, m, rep))
    show("base", funil(b, c, args.ctr, cvr, t, m, rep))
    show("otimista*", funil(b, c * 0.9, args.ctr, cvr * 1.1, t, m, rep * 1.1))
    print("  (*otimista exige fundamento documentado — doc 03)")
    base = funil(b, c, args.ctr, cvr, t, m, rep)
    ltc = base["ltv_cac"]
    print(f"LTV (c/ recompra fator {rep}): R$ {base['ltv']:,.2f} | LTV:CAC = {ltc:.2f} (meta >= 3)")
    print(f"SENSIBILIDADE: CPM +20% => ROAS {funil(b, c*1.2, args.ctr, cvr, t, m)['roas']:.2f} | "
          f"CVR -20% => ROAS {funil(b, c, args.ctr, cvr*0.8, t, m)['roas']:.2f}")
    ok = base["roas"] >= be
    print("VEREDITO ECONOMICO:", "ESCALAVEL (ROAS acima do break-even)" if ok
          else "ABAIXO DO BREAK-EVEN — nao escalar; trabalhar CTR/CVR/oferta antes")

if __name__ == "__main__":
    main()
