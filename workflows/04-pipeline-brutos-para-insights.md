# Workflow — Do bruto ao insight (pipeline diário de dados)

Este é o fluxo que transforma export em decisão. Roda todo dia 08h (corte do dia anterior) ou quando dados caem em `data/raw/`.

## 1. Captura (raw → `data/raw/`)
| Fonte | Formato | Como |
|-------|---------|------|
| Meta Insights | CSV (breakdown: campaign, ad, day) | export manual ou Graph API (fields: date, campaign_name, ad_name, impressions, clicks, reach, frequency, spend, actions, purchase_values) |
| Google Ads | CSV | relatórios de campanha/anúncio por dia |
| TikTok | CSV | Marketing API reports ou export |
| ERP/CRM | CSV | pedidos: data, pedido_id, valor, item, cliente_id, canal, cupom |

Naming dos raws: `<plataforma>-<escopo>-YYYYMMDD.csv`. Raw é imutável (entrada só; o processado nasce em `data/processed/`).

## 2. Normalização (`scripts/ingest.py`)
```bash
python3 scripts/ingest.py data/raw/meta-campaign-20260924.csv --out data/processed/norm-20260924.csv
python3 scripts/ingest.py data/raw/google-campaign-20260924.csv --out data/processed/norm-20260924.csv --append
python3 scripts/ingest.py data/raw/erp-pedidos-20260924.csv --out data/processed/norm-20260924.csv --append
```
Saída: schema comum documentado em `data/exemplos/schemas.md`:
`dt, platform, nivel, id, nome, impressoes, clicks, spend, conv, revenue, reach`

Erros que o ingest reporta (nunca silencia): header desconhecido, coluna de moeda ausente, dt fora da série, duplicatas exatas (suspeita de re-export).

## 3. Métricas (`scripts/metrics.py`)
```bash
python3 scripts/metrics.py data/processed/norm-20260924.csv --json data/processed/metrics-20260924.json
```
Produz: agregados por campanha/criativo/dia (CTR, CPC, CPM, CPA, ROAS, frequência quando houver reach), índice de fatigue por criativo (≥ 3 dias), anomalias por z-score (CPA/CTR diário, |z|>2.5), e o JSON completo para os agentes.

## 4. Interpretação (agente 02)
O script aponta; o analista interpreta — ordem fixa (doc do agente 02): tracking → mudanças internas → learning phase → leilão externo → plataforma → ruído/amostra. Saída: até 5 INSITEs ranqueados por impacto em R$.

## 5. Decisão e fechamento do anel (agentes 00/01/13)
1. INSITEs + FORECAST (12) → 00 decide (DEC) → 01 audita → executa.
2. 12 aplica patch do forecast se a DEC muda premissa.
3. 13 consolida tudo em REL-DIARIO com as 3 ideias de melhoria.
4. Amanhã, o passo 1 consome a realidade nova. **Anel fechado.**

## 6. Regras de qualidade
- Datas: corte = 00:00 do fuso da conta; "ontem" é dia fechado completo.
- Moeda: normalizar para BRL (ingest aceita USD e converte com taxa declarada no arquivo `data/exemplos/schemas.md` — atualizar mensalmente).
- Amostra mínima para claim: 100 cliques ou 5 conversões, senão "insuficiente".
- O JSON é a fonte dos relatórios: número que não está no metrics.json não entra em REL sem rotular `manual-verificado`.
