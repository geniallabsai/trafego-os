# Prompt — Ciclo de Otimização (rota de manutenção)

Uso: semanal (ou quando desvio > 15% por 3d). Agentes 00, 01, 02, 04, 05, 11, 12.

```
CICLO DE OTIMIZAÇÃO — semana {{SEMANA}}, contas {{CONTAS}}.

DADOS 7d (metrics.json): {{METRICS7}}
FATIGUE INDEX por criativo ativo: {{FATIGUE}}
DESVIOS vs FORECAST: {{DESVIOS}}
DECISÕES DOS ÚLTIMOS 7 DIAS + RESULTADO (atingiu limiar?): {{DECS}}
RADAR LEILÃO (03/04): {{LEILAO}}

PASSOS:
1. AGENTE 02: leitura 7d — tendências (mínimo 3 pontos), vazamento AAAR da semana, anomalias não explicadas.
2. AGENTE 11: triagem de fatigue completa + solicitações de renovação ao 05 com diagnóstico (ângulo/execução/audiência/leilão).
3. AGENTE 04: confirma/refuta mudança de leilão/plataforma (ordem 1→6) para cada anomalia relevante.
4. AGENTE 12: recalibra forecast (patches declarados) + MAPE atual.
5. AGENTE 00: DECISÕES da semana — para cada candidata: o quê, as 5 respostas socráticas, impacto, plano B. Priorizar por impacto em R$; máximo 5 execuções por semana (foco).
6. AGENTE 01: auditoria de todas.
7. AGENTE 05: aprova os lotes de renovação solicitados (big ideas novas OU ressurreições, conforme diagnóstico).
8. AGENTE 13: REL-SEMANAL completo (tendência + pipeline + forecast 30d + top 3 ideias).

REGRA DA SEMANA: nenhuma nova big idea entra se o pipeline de renovação dos criativos em pico estiver vazio (manutenção precede invenção).
```
