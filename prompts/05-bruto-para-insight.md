# Prompt — Bruto → Insight (transformar export em ideia)

Uso: qualquer momento, com qualquer CSV bruto ou metrics.json. Agente 02 (+ 04 para anomalias de entrega).

```
DADOS: {{CSV_OU_JSON}} (fonte: {{FONTE}}, período: {{PERIODO}}, moeda: {{MOEDA}}).
CONTEXTO: alterações internas dos últimos 14 dias: {{ALTERACOES}} | testes ativos: {{TESTES}} | forecast vigente: {{FORECAST}}.

PROTOCOLO:
1. Sanidade: duplicatas? gaps de data? conversão > clique? spend sem impressões? (qualidade primeiro)
2. Normalizar mentalmente para o schema comum (dt, platform, nivel, id, nome, impressions, clicks, spend, conv, revenue).
3. Calcular por nível: CTR, CPC, CPM, CPA, ROAS, frequência (se houver reach). Comparar contra baseline 28d da conta e contra forecast (delta %).
4. Série temporal: quais criativos/campanhas desviaram? z-score do diário (|z|>2.5 = anomalia candidata). Fatigue index dos ativos.
5. Para cada anomalia TOP (máx 5): classificar na ordem 1→6 (tracking → interno → learning → leilão → plataforma → ruído) com a evidência.
6. Transformar em INSITE no formato fixo: O quê / Por quê (mecanismo) / Como confirmar / Quando / Onde / Ideia de ação (com impacto em R$) / Fonte.

SAÍDA: relatório de sanidade (2 linhas) + N INSITEs ranqueados por impacto em R$ + 1 pergunta que ainda responde (dados faltantes que impedem veredicto).
Nunca: tabela sem interpretação. Nunca: causa única sem verificar a ordem. Nunca: amostra < 100 cliques como veredicto ("insuficiente").
```
