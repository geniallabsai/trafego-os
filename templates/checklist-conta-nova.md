# Checklist — Conta Nova (Meta / Google / TikTok)

> 100% preenchido = conta liberada para budget real. Item sem evidência = item aberto. Workflow completo: `workflows/01|02|03`.

## Fundação
- [ ] Business Manager / MCC / Business Center criado (nome: {{NOME}})
- [ ] Moeda: {{MOEDA}} | Fuso: America/Sao_Paulo
- [ ] Conta de anúncio **dedicada ao cliente** (1 cliente = 1 conta)
- [ ] Domínio verificado (Meta) / tracking ID único (Google/TikTok)
- [ ] Usuários com papéis definidos: admin agência, admin cliente, operador (somente leitura até DEC-ESTRUTURA)

## Tracking
- [ ] Pixel instalado e validado (Event Test > 95% correspondência)
- [ ] CAPI/Events API ativa com dedupe por event ID (teste ponta a ponta: 1 compra de R$1 batendo nos dois lados)
- [ ] Advanced Matching v2 (email+telefone hash)
- [ ] Eventos na ordem de valor: Purchase(valor) > AddToCart > InitCheckout > Lead > ViewContent
- [ ] Ações de conversão com VALOR REAL configuradas (não "conversão=1")
- [ ] Janela de atribuição cravada e documentada: {{JANELA}} (padrão house: last non-direct, click 7d/view 1d)
- [ ] Conversões secundárias mapeadas (onboarding, lead, recorrente)

## Estrutura
- [ ] Naming house aplicado (ver convention no workflow da plataforma)
- [ ] COLD / WARM / HOT criadas com objetivos corretos por funil
- [ ] CBO nas campanhas principais; adsets com volume mínimo de aprendizado
- [ ] Públicos definidos (ampla primeiro; interesses só como fallback documentado)
- [ ] Budget inicial: cold {{X}}% · warm {{Y}}% · hot {{Z}}%
- [ ] Catálogo/feed sincronizado (se EC)

## Criativos & Copy
- [ ] Lote R3 em produção (mínimo 3–5 hooks × big idea aprovada)
- [ ] MSGN-MAE publicada + consistência anúncio×página×checkout auditada (agente 06)
- [ ] Oferta vigente confirmada com o 09 (escassez com motivo real)
- [ ] Página testada em mobile (LCP < 2.5s)
- [ ] Checkout testado com pagamento real (teste) — carrinho, bump, upsell funcionando

## Governança
- [ ] DEC-000X (estrutura) registrada com premissas
- [ ] FORECAST dia 0 publicado (3 cenários, parâmetros com origem R8)
- [ ] Cronograma de revisão: dia 3 (técnica) · dia 7 (primeira leitura) · dia 14 (estrutura)
- [ ] Relatório diário agendado (09h)
