# Prompt — Criação de Campanha Completa (do produto à estrutura)

Uso: lançamento de oferta/nova conta/nova campanha. Requer: 05, 06, 09, 00, 04 ativos.

```
NOVA CAMPEANHA: criar do zero, seguindo os workflows da plataforma alvo.

INPUTS:
- Produto/oferta: {{PRODUTO}} | Margem bruta: {{MARGEM}} | Ticket: {{TICKET}}
- Público-alvo (descrição + região + idioma): {{PUBLICO}}
- Plataforma e conta: {{PLATAFORMA_CONTA}}
- Budget diário total disponível: {{BUDGET}}
- Prova disponível (números, casos, demos): {{PROVA}}
- Ângulos já testados e resultados (se houver conta): {{HISTORICO}}
- Sazonalidade/leilão (radar 03): {{RADAR}}

EXECUTAR NA ORDEM:
1. AGENTE 09: define a oferta desta campanha (white ou black conforme o input) — stack ancorada, garantia, escassez com motivo, bump/upsell prontos.
2. AGENTE 06: MSGN-MAE (promessa, mecanismo, dores na linguagem do público, provas, objeções) + headline de landing + script VSL 30s + copy de anúncio (texto de cada plataforma).
3. AGENTE 05: 10 big ideas → crivo → 2–3 aprovadas × 3–5 hooks cada + especificação de produção (brief-criativo.md preenchido).
4. AGENTE 04: estrutura técnica da plataforma (workflow 01/02/03) — campanhas, adsets, objetivas, naming house, públicos, orçamento por nível (cold/warm/hot).
5. AGENTE 12: forecast DIA 0 com 3 cenários (parâmetros hierárquicos R8, origem declarada) + metas de decisão (CPA-alvo, ROAS BE, gatilhos de escala/pausa para o 00).
6. AGENTE 00: DEC-ESTRUTURA registrando tudo (premissas + gatilhos de revisão dia 3/7/14).
7. AGENTE 01: auditoria final da estrutura (qualquer premissa sem mecanismo volta).

SAÍDA ÚNICA: arquivo de campanha (estrutura + copies + creative briefs + forecast + gatilhos) pronto para execução, com checklist do workflow preenchido.
```
