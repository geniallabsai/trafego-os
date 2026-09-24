# Prompt — Briefing Diário (o "standup" do time)

Uso: rodar todo dia 09h, com todos os agentes ativos (ou o time mínimo 00+01+02+12+13). Cola este prompt com os dados do dia.

```
É {{DATA}}, 09h. Corte de dados do dia anterior fechado.

DADOS (metrics.json do pipeline): {{METRICS}}
FORECAST VIGENTE (12): {{FORECAST}}
DESVIOS rolling 7d: {{DESVIOS}}
RADAR MERCADO (03, último): {{RADAR}}
STATUS PIPELINE CRIATIVOS (05/11): {{PIPELINE}}
OFERTAS ATIVAS (09): {{OFERTAS}}
DECISIONES PENDENTES (00): {{PENDENTES}}

ROTEIRO DO STANDUP (respeitar a ordem):
1. AGENTE 12: forecast do dia — previsto × realizado por métrica-chave, status dos desvios, patch necessário?
2. AGENTE 02: top 3 achados do dia (INSITE resumido, impacto em R$).
3. AGENTE 00: suas decisões candidatas do dia em formato DEC completo (contexto + 5 respostas socráticas + impacto + plano B), ranqueadas por R$.
4. AGENTE 01: audita cada DEC no formato fixo (aprovada / rejeitada+pergunta em falta / ressalva+limiar).
5. AGENTE 00: confirma decisões aprovadas; declara execução (via MCP ou lista para humano).
6. AGENTE 13: consolida REL-DIARIO completo (estrutura obrigatória) e as top 3 ideias de melhoria no formato fixo.
7. Fecho: qual é o risco das próximas 72h (1 frase) e o que deve acontecer amanhã de manhã (3 ações com dono e data).

REGRAS DA REUNIÃO: ninguém fala sem fonte de número (R6); decisão sem socrático não entra (R7); mau número é falado direto, sem adjetivo.
```
