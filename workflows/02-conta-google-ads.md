# Workflow — Google Ads: criação de conta e estrutura

## 0. Conexão
- Google Ads API: Developer Token aprovado + OAuth com perfil da conta (leitura fase 1; escrita quando o 00 receber permissão).
- Alternativa MCP: servidor MCP do Google Ads (listagem de contas, campanhas, budget, keywords, assets, performance).
- Sem API: exports do "Relatórios" (CSV) em `data/raw/`.

## 1. Fundação
1.1 Conta MCC se for agência (1 sub-conta por cliente); moeda BRL; fuso local.
1.2 Conversões: importar do pixel/CAPI (Meta) ou gtag + GA4 — ações de conversão **com valor** (Purchase R$ real); conversões secundárias: add-to-cart, lead, onboarding-concluído. Janela de atribuição cravada e documentada (padrão house: last non-direct, click 7d/view 1d) — mudar régua no meio de teste é proibido (doc 02 §4).
1.3 Exclusões geográficas de visitante (se negócio local/BR), remarketing habilitado, ajustes de dispositivo após 14d (não antes).

## 2. Estrutura de campanhas (padrão house)
```
Conta
├── SEARCH-BRAND      (exatas de marca, CPC defensivo, RSA com prova)
├── SEARCH-NONBRAND   (temas: 1 tema = 1 adgroup ≤ 15 keywords exatas/frases relacionadas; RSAs por tema)
├── PMAX-[OFERTA]     (1 PMax por oferta/oferta-família; feed + asset groups temáticos)
│     Asset groups: {headline 15, description 5, imagens 10+, logo} por tema/oferta
│     Negativas: exclusões de search keyword quando conflitar com SEARCH-NONBRAND
├── REMARKETING       (RLSA onde aplicável; públicos do funil AAAR: visitou 30d, carrinho 7d, lead 3d)
└── YTD/SHORTS (se vídeo): campanha própria, view/CPA, criativos do lote do 05 (mesmas big ideas, execução vertical)
```
Regras:
- Naming: `PLATAFORMA-NIVEL-OFERTA-TEMA-AAAAMM` (ex.: `GOOG-PMAX-BLACK-MECANISMO-2609`).
- tROAS/tCPA: habilitar somente com ≥ 30 conv/30d (tROAS) ou 15/30d (tCPA); target inicial = ROAS observado × 0.9 (não o sonho).
- Negativas de keyword: varredura semanal (o 04 roda; o 06 valida intenção).
- PMax: nunca 1 PMax gigante multi-oferta (sistema mistura mensagens e mata a atribuição de oferta).

## 3. Primeiros 14 dias
- Dia 0–3: cobertura de leilão (search terms chegando? impression share?), saúde do feed PMax.
- Dia 3–7: busca de termos → primeiras negativas; ajustar asset group temático (o que clica?).
- Dia 7–14: decisão tROAS vs maximize-conversions; rebalancear SEARCH×PMAX com base em CAC por oferta (não em spend).
- `DEC-0002` registra estrutura + premissas (linha base do forecast).

## 4. Checklist de saída
- [ ] Conversões com valor importadas e testadas · [ ] Janela de atribuição documentada · [ ] SEARCH brand/nonbrand separadas · [ ] PMax 1-offerta por grupo · [ ] Negativas iniciais aplicadas · [ ] Naming house · [ ] DEC-0002 · [ ] Forecast dia 0 publicado
