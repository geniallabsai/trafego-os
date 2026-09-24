# Funil AAAR (+ camada de engajamento)

Definição deste repositório:

- **Aquisição (Acquisition):** o usuário chega via mídia paga e consome o ponto de contato (anúncio → landing/VSL/DM/loja).
- **Ativação (Activation):** primeira ação de valor **para ele**: primeira compra (EC/info white), primeiro cadastro completo (lead gen), primeira sessão útil (app), primeira conversa respondida (DM).
- **Retenção (Retention):** volta dentro da janela (D7/D30/D90): recompra, segunda interação, onboarding concluído, recorrência ativa.
- **Receita (Revenue):** monetização sustentada: LTV, upsells, recorrência, referidos pagos.

Sobre o AAAR canônico de produto (AARRR): aqui **Revenue absorve Referral** como alavanca explícita dentro de Receita + a camada de **Engajamento** opera transversalmente, pois em tráfego pago social o engajamento *é* aquisição barata (organico assistindo pago, social proof, remarketing orgânico).

## 1. Métricas por estágio (régua única, glossário doc 06)

| Estágio | Métrica-norte | Guard-rails | Vazamento clássico |
|---------|---------------|------------|--------------------|
| Aquisição | CAC por canal e por oferta | CTR ≥ média conta; frequência < 5 | Criativo fraco (hook), landing lenta/desalinhada |
| Ativação | CVR do funil (clique→ativação) | Tempo p/ 1ª ação < 24h; drop-off checkout < 40% | Página com 3 promessas, checkout longo, prova ausente |
| Retenção | Repurchase rate D30; churn de recorrência | Onboarding concluído > 70%; NPS | Produto entregou promessa? Copy de pós-compra vazia |
| Receita | LTV:CAC ≥ 3; MER | Payback < 30d; AOV em alta ou estável | Upsell invisível, sem programa de recorrência/referral |

## 2. Cada estágio, quem fala e o que entrega

### Aquisição — agentes 05, 06, 10
- Big idea por campanha (agent 05) + mensagem-mãe do funil (agent 06): a promessa do anúncio, da landing e da oferta é **a mesma promessa com três níveis de detalhe**. Desalinhamento de mensagem (ad vende "emagrecer", página vende "biotina") mata CVR antes do produto entrar em campo.
- Estrutura de campanha: ver `workflows/` + `templates/checklist-conta-nova.md`.

### Ativação — agentes 06, 09
- Página de destino: headline = promessa do anúncio (paráfrase, não copy-paste), 1 CTA, prova hierárquica (números > vídeo-testemunho > texto > autoridade), remoção de navegação, velocidade < 2.5s LCP.
- Checkout: campos mínimos, garantia visível, forma de pagamento local, pedido mínimo friccional.
- Oferta (agent 09): estrutura completa em doc 05.
- DM/VSL curta: script de 30s (problema agudo → mecanismo único → oferta + risco zero → CTA único).

### Retenção — agentes 07, 08
- **Onboarding em 3 toques:** D0 (entrega + "o que esperar"), D3 (caso de sucesso + dica de uso), D7 (pergunta de valor + próximo passo).
- **Recuperação:** carrinho abandonado (3 toques: lembrete → prova → urgência com motivo), inatividade D14/D30 (oferta de reativação — não discount aleatório: motivo + novidade).
- **Comunidade (07):** grupo/DM com cadência de conteúdo, ritual semanal, resposta < 1h em horário comercial; UGC pedido com gancho específico ("me manda print do seu resultado que eu mostro ao vivo").

### Receita — agentes 08, 09, 10
- **Order bump** (+15–30% de itens/ordem), **upsell 1** (lógica complementar, 1 clique), **downsell** (recusa graciosa, 50–60% do preço).
- **Recorrência/clube:** assinatura ou clube de recompra para nichos de reposição; LTV medido com janela de 90d mínima.
- **Referral (07+10):** mecânica de 2 lados (indica ganha, indicado ganha), acionada no momento de pico de satisfação (pós-resultado, não pós-compra).

## 3. O teste por estágio (regra de ouro)

Melhorar o funil inteiro de uma vez **mata a atribuição**. Protocolo:
1. Medir baseline 14d (ou 28d se volume baixo).
2. Escolher **um** estágio com o maior vazamento absoluto (ex.: 40% perdem no checkout > 10% churn de onboarding).
3. Testar ali (EXP-XXXX, tamanho de amostra documentado — ver `templates/registro-experimentos.md`).
4. Só migrar pro próximo estágio com vencedor declarado.

## 4. Sinal de que o funil está saudável

- Aquisição barata demais + Ativação fraca = criativo atrai curioso, oferta não converte: problema de **promessa**, não de mídia.
- Ativação ótima + Retenção morta = problema de **entrega de valor** (produto/experiência) — parar de escalar mídia e fixar retenção antes (escalar mídia sobre fundação rachada = queimar mais).
- Receita plana com LTV subindo = **oportunidade**: aumentar teto de CAC aceitável e voltar a escalar com o novo ROAS break-even.
