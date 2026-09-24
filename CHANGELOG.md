# Changelog

Formato: [Sem Ver] — datas em UTC.

### Em destaque (v1.2)
- 3 novos agentes: **14 Relatorista Streamlit** (dashboard), **15 LP & Conversão (CRO) + CRM de sites**, **16 Tracking Ponta a Ponta** (gate de decisão).


## [1.2.0] — 2026-09-24
### Adicionado
- `agents/14-dashboard-streamlit` — mantém e expande o dashboard.
- `agents/15-lp-conversao-crm` — LP de alta conversão (message match, atrito, CRO com amostra) + CRM de sites (segmentos, cadências, scoring).
- `agents/16-tracking-ponta-a-ponta` — 6 checkpoints (disparo, dedupe event_id, server-side, convergência plataforma×GA4×ERP, valores, atribuição); gate do Head.
- `scripts/dashboard.py` + `requirements.txt` — dashboard Streamlit: KPIs, campanhas/adsets/criativos, fatigue, série diária, preview de forecast.
### Alterado
- README: time agora com 17 agentes; quickstep do dashboard.
- Repo: homepage removida; autoria do commit neutra.

## [1.1.0] — 2026-09-24
### Adicionado
- `assets/logo.svg` — identidade visual do repositório.
- `config/.env.example` + `config/TOKENS.md` + `config/mcp.example.json` — seção de chaves: LLM (geração de criativos/copy), Meta, Google Ads, TikTok, GitHub, ERP/GA4. Tabela de quién-consuma-quê e fases leitura→escrita.
- `docs/07-estruturas-validadas.md` — blueprints validados: **Meta CBO**, **Meta ABO**, **Google PMax**, **Google Search** (brand + non-brand), com matriz de escolha, regras de learning phase e erros comuns.
- `data/estruturas/*.json` — esqueletos de máquina das 4 estruturas (os agentes carregam e montam).
- `scripts/metrics.py`, `scripts/ingest.py`, `scripts/forecast.py` — pipeline bruto→insight e forecast 3 cenários (stdlib puro).
- `data/exemplos/` — schemas.md + CSVs de exemplo Meta e Google prontos para o pipeline.
- `LICENSE`, `ROADMAP.md`, `CONTRIBUTING.md`, `GO-TO-STARS.md`.

## [1.0.0] — 2026-09-24
### Adicionado
- Fundação completa: 14 agentes, 6 documentos de metodologia, 4 workflows, 9 prompts, 7 templates, hub de orquestração (AGENTS.md) e README.
