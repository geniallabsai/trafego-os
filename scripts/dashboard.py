#!/usr/bin/env python3
"""Trafego OS — dashboard Streamlit. Todos os dados, campanhas e criativos em uma tela.

Uso:
  pip install -r requirements.txt
  streamlit run scripts/dashboard.py

Fontes: data/processed/norm-*.csv (gerado por scripts/ingest.py) ou upload manual
no schema comum (data/exemplos/schemas.md). Nenhuma métrica é estimada aqui:
o painel exibe o que está nos arquivos (regra R8).
"""
import glob

import pandas as pd
import streamlit as st

st.set_page_config(page_title="trafego-os · dashboard", page_icon="🚦", layout="wide")

NUMCOLS = ["impressoes", "clicks", "spend", "conv", "revenue", "reach"]


def _to_num(df):
    for col in NUMCOLS:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(",", "").str.replace("R$", "", regex=False),
                errors="coerce",
            ).fillna(0.0)
    return df


@st.cache_data(show_spinner=False)
def load_one(path):
    return _to_num(pd.read_csv(path))


def fmt(v, kind="num"):
    if v is None or pd.isna(v):
        return "—"
    if kind == "bRL" or kind == "brl":
        return f"R$ {v:,.2f}"
    if kind == "pct":
        return f"{v:.2%}"
    if kind == "x":
        return f"{v:.2f}×"
    return f"{v:,.2f}"


def derive(df):
    g = df.groupby(["platform", "nivel", "id", "nome"], as_index=False)[NUMCOLS].sum()
    g["ctr"] = (g["clicks"] / g["impressoes"]).where(g["impressoes"] > 0)
    g["cpm"] = (g["spend"] / g["impressoes"] * 1000).where(g["impressoes"] > 0)
    g["cpc"] = (g["spend"] / g["clicks"]).where(g["clicks"] > 0)
    g["cpa"] = (g["spend"] / g["conv"]).where(g["conv"] > 0)
    g["roas"] = (g["revenue"] / g["spend"]).where(g["spend"] > 0)
    return g.sort_values("spend", ascending=False)


def fatigue(df):
    ads = df[df["nivel"].isin(["ad", "creative"])].copy()
    if ads.empty:
        return pd.DataFrame(columns=["criativo", "nome", "dias", "impressoes", "fatigue_index", "status"])
    daily = ads.groupby(["id", "nome", "dt"], as_index=False)[["impressoes", "clicks"]].sum().sort_values("dt")
    rows = []
    for (cid, nome), d in daily.groupby(["id", "nome"]):
        if len(d) < 3:
            continue
        imp, clk = d["impressoes"], d["clicks"]
        f_imp, l_imp = float(imp.iloc[:3].sum()), float(imp.iloc[-3:].sum())
        f_clk, l_clk = float(clk.iloc[:3].sum()), float(clk.iloc[-3:].sum())
        if f_imp <= 0 or l_imp <= 0 or f_clk <= 0:
            continue
        idx = (l_clk / l_imp) / (f_clk / f_imp)
        status = "OK" if idx >= 0.9 else ("ATENÇÃO" if idx >= 0.7 else "FADIGADO")
        rows.append({"criativo": cid, "nome": str(nome)[:48], "dias": len(d),
                     "impressoes": int(imp.sum()), "fatigue_index": round(idx, 2), "status": status})
    return pd.DataFrame(rows).sort_values("fatigue_index").reset_index(drop=True)


def kpi_block(df):
    tot_imp, tot_clk = float(df["impressoes"].sum()), float(df["clicks"].sum())
    tot_spend, tot_conv = float(df["spend"].sum()), float(df["conv"].sum())
    tot_rev = float(df["revenue"].sum())
    roas = tot_rev / tot_spend if tot_spend else float("nan")
    cpa = tot_spend / tot_conv if tot_conv else float("nan")
    ctr = tot_clk / tot_imp if tot_imp else float("nan")
    c = st.columns(6)
    c[0].metric("Spend", fmt(tot_spend, "brl"))
    c[1].metric("Receita", fmt(tot_rev, "brl"))
    c[2].metric("ROAS", fmt(roas, "x"))
    c[3].metric("CPA médio", fmt(cpa, "brl"))
    c[4].metric("CTR", fmt(ctr, "pct"))
    c[5].metric("Período", f"{df['dt'].min()} → {df['dt'].max()}")
    if tot_clk < 100 or tot_conv < 5:
        st.warning("Amostra insuficiente (mínimo 100 cliques ou 5 conversões) — trate os números como indicativos.")


def forecast_block():
    st.subheader("Preview de forecast (mesma fórmula de scripts/forecast.py)")
    f = st.form("fc", border=True)
    b1, b2, b3, b4 = f.columns(4)
    budget = b1.number_input("Budget (BRL)", value=30000, step=1000)
    cpm = b2.number_input("CPM (BRL)", value=25.0, step=1.0)
    ctr = b3.number_input("CTR (%)", value=1.5, step=0.1) / 100
    cvr = b3.number_input("CVR (%)", value=3.0, step=0.1) / 100
    ticket = b4.number_input("Ticket (BRL)", value=97.0, step=1.0)
    margem = b4.number_input("Margem (%)", value=60, step=1) / 100
    dias = f.slider("Horizonte (dias)", 7, 90, 30)
    ok = f.form_submit_button("Calcular")
    if ok and budget and cpm and margem:
        imp = budget / cpm * 1000
        clicks = imp * ctr
        vendas = clicks * cvr
        receita = vendas * ticket
        be = 1 / margem
        scen = {
            "pessimista (CPM+20%, CTR-15%, CVR-20%)": (cpm * 1.2, ctr * 0.85, cvr * 0.8),
            "base": (cpm, ctr, cvr),
            "otimista* (CPM-10%, CVR+10%)": (cpm * 0.9, ctr, cvr * 1.1),
        }
        rows = []
        for nome, (c_, t_, v_) in scen.items():
            i2 = budget / c_ * 1000; v2 = i2 * t_ * v_; r2 = v2 * ticket
            rows.append({"cenário": nome, "impressões": int(i2), "cliques": int(i2 * t_),
                         "vendas": int(v2), "receita": r2,
                         "ROAS": r2 / budget if budget else None,
                         "CAC": (budget / v2 if v2 else None),
                         "lucro bruto": r2 * margem - budget})
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        st.caption(f"{dias} dias · ROAS break-even = {be:.2f} · (*otimista exige fundamento documentado)")


# ---------------- UI ----------------
st.title("🚦 trafego-os — tráfego pago em uma tela")
st.caption("Dados de data/processed (pipeline ingest→metrics). Regra da casa: sem rótulo de fonte, sem número.")

with st.sidebar:
    st.header("Fonte de dados")
    paths = sorted(glob.glob("data/processed/norm-*.csv"))
    chosen = st.multiselect("Arquivos normalizados", paths, default=paths,
                            disabled=not paths, placeholder="nenhum em data/processed/")
    up = st.file_uploader("ou envie CSV (schema comum)", type=["csv"])
    st.divider()
    with st.expander("Como alimentar"):
        st.markdown(
            "```bash\npython3 scripts/ingest.py data/raw/<bruto>.csv \\\n    --out data/processed/norm-YYYYMMDD.csv\n```"
            "\n\nSchema: `data/exemplos/schemas.md`. Exemplos: `data/exemplos/*-exemplo.csv`."
        )

df = None
if chosen:
    df = pd.concat([load_one(p) for p in chosen], ignore_index=True)
if up is not None:
    try:
        extra = _to_num(pd.read_csv(up))
        df = extra if df is None else pd.concat([df, extra], ignore_index=True)
    except Exception as e:
        st.error(f"CSV inválido: {e}")

if df is None or df.empty:
    st.info("Sem dados ainda. Rode o ingest ou envie um CSV — o exemplo vive em `data/exemplos/`.")
    st.stop()

kpi_block(df)

tab_camp, tab_crea, tab_serie, tab_fc = st.tabs(["Campanhas", "Criativos & fatigue", "Série diária", "Forecast"])

with tab_camp:
    g = derive(df)
    cols = st.columns(2)
    plat = cols[0].selectbox("Plataforma", ["todas"] + sorted(g["platform"].unique()))
    nivel = cols[1].selectbox("Nível", ["campaign", "adset", "ad", "todos"], index=0)
    view = g
    if plat != "todas":
        view = view[view["platform"] == plat]
    if nivel != "todos":
        view = view[view["nivel"] == nivel]
    shown = view.copy()
    shown["ctr"] = shown["ctr"].map(lambda v: fmt(v, "pct"))
    shown["cpm"] = shown["cpm"].map(lambda v: fmt(v, "brl"))
    shown["cpc"] = shown["cpc"].map(lambda v: fmt(v, "brl"))
    shown["cpa"] = shown["cpa"].map(lambda v: fmt(v, "brl"))
    shown["roas"] = shown["roas"].map(lambda v: fmt(v, "x"))
    shown["spend"] = shown["spend"].map(lambda v: fmt(v, "brl"))
    shown["revenue"] = shown["revenue"].map(lambda v: fmt(v, "brl"))
    st.dataframe(shown, use_container_width=True, hide_index=True)
    st.download_button("baixar CSV", shown.to_csv(index=False).encode(), file_name="campanhas.csv")

with tab_crea:
    ft = fatigue(df)
    if ft.empty:
        st.info("Nenhum criativo com série suficiente (≥ 3 dias) para índice de fatigue.")
    else:
        ft_view = ft.copy()
        ft_view["fatigue_index"] = ft_view["fatigue_index"].map(lambda v: f"{v:.2f}")
        st.dataframe(ft_view, use_container_width=True, hide_index=True)
        st.caption("fatigue = CTR últimos 3 dias ÷ CTR primeiros 3 dias. < 0.9 atenção · < 0.7 FADIGADO (pausar, lote novo em 48h — agente 11).")

with tab_serie:
    daily = df.groupby("dt", as_index=False)[["spend", "revenue", "clicks"]].sum().sort_values("dt")
    st.line_chart(daily.set_index("dt")[["spend", "revenue"]])
    st.line_chart(daily.set_index("dt")[["clicks"]])
    st.dataframe(daily, use_container_width=True, hide_index=True)

with tab_fc:
    forecast_block()
