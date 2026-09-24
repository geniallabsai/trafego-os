# Schema comum do trafego-os

Todo dado que entra no pipeline (manual ou API) e normalizado para este schema pelo `scripts/ingest.py`. O `scripts/metrics.py` consome exatamente isto.

## Tabela normalizada (midia de entrega)
| Coluna | Tipo | Descriao | Exemplo |
|--------|------|-----------|---------|
| dt | date (AAAA-MM-DD) | dia fechado, fuso America/Sao_Paulo | 2026-09-23 |
| platform | enum | meta / google / tiktok / erp | meta |
| nivel | enum | campaign / adset / ad (ou pedido, p/ ERP) | campaign |
| id | string | id nativo da plataforma | 1202... |
| nome | string | nome legivel (naming house) | COLD-BLACK-MEC-2609 |
| impressoes | int | impresses | 40210 |
| clicks | int | cliques | 610 |
| spend | float | BRL (converte USD com --fx) | 1005.40 |
| conv | float | converses (unidades) | 18 |
| revenue | float | BRL atribuido a linha | 1746.00 |
| reach | int (opcional) | alcancados (calcula frequencia) | 21000 |

## Regras
- **Moeda:** tudo em BRL. Export em dolar usa `--fx 5.43` (taxa declarada aqui todo mes).
- **Imutabilidade:** `data/raw/` so recebe; processado nasce em `data/processed/`.
- **Amostra minima para claim:** 100 cliques OU 5 converses (abaixo disso: "insuficiente").
- **Nomes:** seguem a naming house do workflow da plataforma — o nome E metadados.

## Exemplos
- `meta-daily-exemplo.csv` e `google-daily-exemplo.csv`: ja no schema comum (prontos para `metrics.py`).
- Para bruto "como veio da plataforma", rode o ingest: `python3 scripts/ingest.py <bruto>.csv --out data/processed/norm.csv`.
