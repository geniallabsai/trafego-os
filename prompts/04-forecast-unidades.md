# Prompt — Forecast de Custos e Vendas

Uso: semanal (30d), ad-hoc (7d/lançamento), ou pós-DEC que muda premissa. Agente 12 com inputs de 02/03/00.

```
FORECAST {{HORIZONTE}}D — conta(s) {{CONTAS}}, budget planejado {{BUDGET}}, data-base {{DATA}}.

PARÂMETROS DISPONÍVEIS:
- Conta 28d ponderada: CPM {{CPM}} | CTR {{CTR}} | CVR {{CVR}} | ticket {{TICKET}} | margem {{MARGEM}}
- Testes ativos afetando parâmetros: {{TESTES}}
- Radar de mercado/sazonalidade (03): {{RADAR}} (multiplicadores sazonais: {{MULTS}})
- DEC recentes que mudam premissa: {{DEC}}
- Histórico de acurácia (MAPE por parâmetro): {{MAPE}}

EXECUÇÃO:
1. Hierarquizar cada parâmetro (R8) com origem declarada (conta-28d / teste / benchmark / analogia).
2. Rodar scripts/forecast.py (incluir o comando exeto na saída) com parâmetros base.
3. Gerar 3 cenários (pessimista/base/otimista) — otimista só com fundamento documentado.
4. Aplicar multiplicadores sazonais do horizonte (declara quais).
5. Calcular: funil completo, CAC, ROAS, ROAS break-even, LTV, payback, MER, margem contributiva.
6. Comparar com desvio rolling (previsto × realizado últimos 7d/28d); MAPE atual por parâmetro.
7. Patches: para cada DEC ativa, ajustar premissa e registrar delta.
8. Riscos do horizonte: eventos de leilão, calendário, estoque, plataforma change (do radar).

SAÍDA: FORECAST no formato do docs/03 §4 + comandos reproduzíveis + tabela de sensibilidade (o que acontece se CPM subir 20% / CVR cair 20%).
```
