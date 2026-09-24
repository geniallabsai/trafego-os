# Prompt — Revisão Socrática (a pente-fino de uma decisão)

Uso: antes de qualquer DEC de grande impacto (escala > 30% do budget, mudança de oferta, lançamento black), ou quando o 01 já rejeitou 2×. Todos os agentes envolvidos + 01 como árbitro.

```
REVISÃO SOCcrÁTICA — DEC-{{REF}}: {{DECISAO}}.
DADOS APOIO: {{DADOS}} | FORECAST: {{FORECAST}} | RADAR: {{RADAR}} | HISTÓRICO DE DECISÕES SEMELHANTES E RESULTADOS: {{HISTORICO}}.

CADA AGENTE RESPONDE POR ESSE ÂNGULO (1 bloco cada, sem repetir o outro):
1. AGENTE 02 (POR QUE-dados): a evidência sustenta o mecanismo? Qual dado refutaria? Está ponderado (28d vs 3d)? Amostra suficiente?
2. AGENTE 04 (POR QUE-mecanismo): como as plataformas vão reagir a essa mudança? (learning phase, leilão, sinais) Janela real de efeito?
3. AGENTE 12 (COMO-números): impacto projetado nos 3 cenários; quanto custa errar? Qual a perda máxima se a hipótese for falsa?
4. AGENTE 05/11 (COMO-criativo): a frota aguenta? Existe sucessor no pipeline? O que o banco de kills diz sobre este ângulo?
5. AGENTE 09 (COMO-oferta): a promessa continua coerente com a oferta? Algum elemento de preço/escassez entra em jogo?
6. AGENTE 10 (QUANDO-mercado): há janelas/sazonais que favorecem ou prejudicam a execução agora?
7. AGENTE 00 (QUANDO-ONDE-execução): cadência, magnitude, plano B, data de revisão, limiar de reversão — todos explícitos.
8. AGENTE 01 (A QUESTÃO FINAL): o que mudaria a ideia — métrica, limiar, consequência — está declarável em 1 frase? Se sim, declare. Se não, REJEITAR com a pergunta exata.

VEREDITO: GO (com resalvas listadas) / NO-GO (com o que precisaria mudar) / GO-CONDICIONAL (condição + data de reavaliação).
O veredito e o raciocínio vão na DEC final — a próxima pessoa que ler em 3 meses tem que entender por quê.
```
