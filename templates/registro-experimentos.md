# Registro de Experimentos (EXP)

> Todo teste de criativo, copy, oferta, estrutura vira EXP. Nada de teste "olhando o painel".

## EXP-{{NNNN}} — {{HIPÓTESE_EM_1_FRASE}}
- **Dono:** agente {{NN}} · **Início:** {{DATA}} · **Fim máximo:** {{DATA}} (data de morte declarada antes de começar)
- **Funil/estágio AAAR afetado:** {{...}}
- **Variável única testada:** {{UM_PARAMETRO_POR_VEZ}}
- **Baseline (14d prévio, fonte):** {{VALORES}}

### Hipótese socrática
- **Se** {{ação específica}}, **então** {{métrica}} move **{{+X%}}**, **porque** {{mecanismo nomeado}}.

### Tamanho de amostra & limiar
- Métrica de decisão: {{CVR/CTR/CPA}} · Baseline: {{p0}} · Efeito mínimo detectável: {{delta}}
- Amostras necessárias (aprox.): {{n por braco — calculado; se n > capacidade de 2 semanas, usar métrica intermediária (CTR/CPC) como leading e anotar}}
- **Limiar de sucesso:** {{valor}} · **Limiar de aborto antecipado:** {{valor/data}}

### Design
| Braço A (controle) | Braço B (variação) |
|--------------------|--------------------|
| {{...}} | {{...}} |
- Voo: mesmo adset/budget/horario · Duracao: {{...}} · Fontes rotuladas: sim

### Resultados (preenchido na data de veredito)
| Braço | Imp | Cli | CTR | Conv | CVR | Spend | CPA | ROAS | confianca |
|-------|-----|-----|-----|------|-----|-------|-----|------|-----------|
| A | | | | | | | | | |
| B | | | | | | | | | |

### Veredito
- {{GANHOU A / GANHOU B / EMPATE TECNICO (decisão por custo — documentar) / ABORTADO (razão)}}
- Escala: {{sim/não/padrão}} -> DEC ref {{...}}
- Banco que alimenta: LABORATÓRIO (05) / FORECAST (12) / ALGO (04) — entrada registrada: {{sim/ref}}
