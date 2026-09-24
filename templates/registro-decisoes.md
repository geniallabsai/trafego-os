# Registro de Decisões (DEC)

> Uma DEC por decisão de mídia/estrutura/oferta. Sequencial, imutável após auditoria (correcao = nova DEC referenciando).

## DEC-{{NNNN}} — {{TITULO_CURTO}}
- **Data/hora:** {{DATA}} · **Decisor:** agente 00 · **Auditoria:** agente 01 (APROVADA / RESALVA / REJEITADA->reaberta)
- **Contexto (3 linhas):** {{por que esta decisão existe agora}}

### Respostas socráticas
- **POR QUE (mecanismo + dado c/ fonte):** {{...}} (fontes: conta-28d / teste-XXXX / benchmark)
- **COMO (parâmetro, magnitude, cadência):** {{...}}
- **QUANDO (execução, revisão, condição de saída):** {{...}}
- **ONDE (conta>campanha>adset>criativo; escopo de replicação):** {{...}}
- **O que mudaria minha ideia:** métrica {{METRICA}} + limiar {{LIMIAR}} -> consequência {{CONSEQUENCIA}}

### Impacto previsto
- R$/mês: {{+/-}} (cenário base) · Custo do erro se hipótese falsa: {{...}}
- Efeito sobre o forecast: {{patch necessário? ref FORECAST-PATCH}}

### Plano B
{{o que fazer se o limiar for violado}}

### Execução
- Via: MCP / API / CLI / humano · Data exec: {{...}}
### Revisão (preenchida na data marcada)
- Resultado vs limiar: {{atingiu?}} · Aprendizado: {{1 linha}} · Próxima DEC se necessária: {{ref}}
