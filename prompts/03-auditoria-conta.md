# Prompt — Auditoria de Conta (health check completo)

Uso: mensal, onboarding de conta nova, ou quando o CAC drifted > 20% em 30d. Todos os agentes.

```
AUDITORIA DE CONTA {{CONTA}} — período: {{PERIODO}}.

Checklist executado seção por seção, cada item com veredito OK/PROBLEMA/EVIDÊNCIA:

A. TRACKING (04) — pixel/CAPI/Events API: eventos chegando? dedupe ok? valor real em Purchase? Advanced Matching ativo? janela de atribuição documentada? tag manager sem conflito?
B. ESTRUTURA (04/00) — 1 conta por cliente? objetivos corretos por funil (COLD/WARM/HOT)? naming house? CBO/ABO coerente? budget vs roleta (nada de micro-budget morto)?
C. APRENDIZADO (04) — adsets com volume suficiente de eventos? mudanças que reiniciam learning phase detectadas nos últimos 30d?
D. CRIATIVOS (11/05) — índice de fatigue da frota? meio-vida por ângulo? pipeline de sucessor para líderes de spend? banco de kills documentado?
E. OFERTA (09) — escassez verdadeira? garantia coerente? AOV vs potencial (bump/upsell presentes)? desalinhamento promessa×oferta?
F. FUNIL (06/07/08) — consistência de mensagem anúncio→página→checkout (auditoria do 06)? velocidade da página (LCP < 2.5s)? SLA de DM? fluxos de retenção ativos?
G. ECONÔMICO (12/00) — CAC vs break-even por oferta? MER? LTV:CAC? payback? MAPE do forecast no período?
H. EXTERNO (03) — posição no leilão (concorrentes ativos), sazonalidade do próximo trimestre, riscos declarados.

SAÍDA: relatório de auditoria com score por seção (0–10), ranking dos 5 problemas por custo estimado em R$/mês, e plano de correção (DEC com owner e data para cada um). Nada de achado sem evidência numerada.
```
