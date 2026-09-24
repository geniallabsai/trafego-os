# Algoritmos das plataformas de ads — o mecanismo por baixo

Este documento é a base do agente 04. Atualizar semanalmente (versionar como `ALGO-META-vX.Y.md`). **Regra R6 vale:** números citados como benchmark são referência; a conta real (28d) é a fonte de verdade.

## 1. Meta (Facebook/Instagram) — incluindo Andromeda

### 1.1 O leilão, na mecânica
Cada leilão compara anúncios candidatos com:

```
ranking ≈ bid × valor estimado (value)
onde valor estimado ≈ eCTR (clique) × eCVR (conversão) × valor da conversão
```

- **eCTR / eCVR** são probabilidades **estimadas pelo modelo** para aquela pessoa+contexto, aprendidas dos seus sinais (pixel, CAPI, catalog).
- **Ad Relevance / qualidade** entra como multiplicador efetivo: relevância baixa degrada estimativas e encarece CPM. Os diagnósticos (ad relevance diagnostics, engagement rate below average etc.) são o termômetro disso.
- **Fase de aprendizado:** até ~**50 eventos de otimização por semana** no adset, o sistema explora mais e o CPC/CPM oscila. Cortar budget > 20% nessa fase "reinicia" parcialmente o aprendizado. Depois de sair, o adset fica estável — e mudanças grandes (objetivo, público amplo↔estrito, CBO↔ABO) voltam a explorá-lo.
- **Budget rule prática:** mudanças de ±20%/dia; escala gradual preservando o learning phase.

### 1.2 Sinais: onde o modelo aprende
- **Pixel (web) + CAPI (server-side):** eventos duplicados são deduplicados por evento ID (hash). CAPI recupera o que o browser perde (iOS/ATP, blockers) — em contas sérias, **toda conversão importante vai de server side** com dedupe.
- **Eventos que contam:** Purchase é rei (valor em moeda), AddToCart/InitCheckout são intermediários úteis para públicos frios, Lead/Contact para serviços. Configurar no **Advanced Matching** (email + telefone hashados) melhora atribuição em iOS.
- **Catalog/Commerce:** para EC com catálogo, o Advantage+ Shopping Campaign entrega por item — o feed limpo (imagens, preço, disponibilidade) é parte do algoritmo.
- **Advantage+ (público, budget, creative):** a meta é reduzir alavancas manuais; o que você controla de verdade é: **objetivo de otimização, orçamento, criativos e sinais**. Público amplo + criativo forte é a configuração padrão atual; lookalikes perderam papel central.

### 1.3 Meta Andromeda — o motor de próxima geração
Andromeda é o codinome da geração experimental do motor de ads da Meta em movimento desde 2025: leilão orientado por modelos generativos/LLM, criativos dinâmicos por pessoa (mixes automáticos de hook/CTA), e a direção de **comércio agêntico** (o assistente de IA participa da decisão de compra). Implicações práticas que já se aplicam:

1. **Volume e diversidade de criativos é o novo targeting.** Se o motor recombina e testa por você, quem fornece 20 variações por ângulo ganha contra quem fornece 3.
2. **Sinais de valor > sinais de clique.** Otimização por Purchase com valor real entra em vantagem sobre otimização por lead/clique.
3. **Nomeação limpa e metadados** (convenção de nome de campanha/adset, tags, criativos únicos com ID) deixam o sistema — e o seu time — rastreando o que funciona.
4. **Estabilidade de conta:** o motor gosta de histórico consistente; contas novas ou recriadas repetidamente chegam "cegas".
5. ⚠️ *Andromeda está em rollout contínuo — o mapa exato muda. O agente 04 revisa changelogs oficiais semanalmente e versiona `ALGO-META`. Se o que estiver aqui divergir do oficial, o oficial vence e este doc é atualizado.*

### 1.4 Diagnóstico rápido de entrega
| Sintoma | Mecanismo provável | Ação |
|---------|--------------------|------|
| CPM subiu sem causa sua | Leilão mais disputado (sazonal/concorrente) ou qualidade dos criativos caiu | Checar seasonality (doc 03) + fatigue (agent 11); não culpar "algoritmo" sem medir |
| Gasto baixo no adset | Learning phase, bid abaixo do leilão, ou budget do adset limitado | Verificar status de aprendizado; subir bid 10–15%; checar cap de budget |
| CPA subiu pós-escala | Exploração maior com budget novo (esperado) ou audiência esgotada | Dar 72h; se persistir, novos criativos > novo público |
| Reach estagnado, frequência alta | Público satura | Abrir targeting / novo criativo; frequência > 4–5 no cold já é cheiro de cansaço |

## 2. Google Ads

### 2.1 O leilão
`Ad Rank = Bid × Qualidade (histórico CTR esperado, relevância do anúncio, qualidade da landing) × Impacto esperado dos extension/assets × Contexto.`

- **Search:** QS por palavra-chave (1–10) multiplica o custo real. Qualidade alta = pagar menos pelo mesmo leilão. Negativas de keyword são manutenção semanal, não luxo.
- **PMax (Performance Max):** feed + assets; o sistema combina formatos (YouTube, Search, Discovery, Gmail). Estrutura correta: 1 PMax por objetivo de oferta (não 1 gigante); assets em blocos por tema/oferta; exclusões de search keywords onde conflitar com campanhas de marca.
- **Targets:** tROAS exige ~30 conversões/30d (ideal ~50+) para funcionar; tCPA exige ~15/30d. Abaixo disso, o sistema oscila — e tROAS agressivo demais faz o sistema buscar conversões baratas de baixa qualidade (compras pequenas).
- **Brand vs non-brand:** separar sempre; brand com CPC baixo protege marca, non-brand mede desejo.

### 2.2 Sinais e conversões
- Ações de conversão com **valor** (não só quantidade) habilitam tROAS inteligente.
- Importância: marcar conversões secundárias (cadastre-se, onboarding, compra recorrente) e definir **janela de atribuição** consistente com o CRM.
- Landing Page Experience é componente real do rank: velocidade (Core Web Vitals) e mensagem-match com a keyword/âncora do criativo.

### 2.3 Rotina do 04 no Google
- Semanal: auction insights (marca, sobreposição), busca de termos (negativas), saúde do feed PMax, drift de tROAS.
- Mensal: re-testar RSA campeões (fatigue também mata em Search — CTR caindo = trocar headlines).

## 3. TikTok Ads

### 3.1 O mecanismo
- **Creative-first:** não existe público mágico; o criativo filtra a audiência. O sistema modela interesses a partir de quem engaja com seus formatos (som, vertical, UGC-like).
- **Spark Ads:** usar posts orgânicos/creator com permissão — social proof + distribuição combinadas.
- **Learning phase:** similar em espírito (volume de conversão mínimo por campanha); abaixo disso, delivery oscila.
- **Bidding:** CBO (campaign budget) é padrão; targets de CPA/volume funcionam melhor com histórico; Creative-first significa rodar 3–5 criativos por campanha desde o dia 1.

### 3.2 O que mata conta TikTok
Criativo com cara de anúncio (polish high de TV perde para UGC nativo), hook fraco nos 2 primeiros segundos, som silenciado (subtítulo obrigatório), CTA genérico ("saiba mais" < "garanta o desconto de hoje"), e ignorar comentários (o algoritmo lê o engajamento sob o post como sinal de intenção).

## 4. Outras plataformas (mapa mínimo)

- **LinkedIn:** Sponsored Content + Matched Audiences; tCPA existe; CPM elevado (US$ 30–80 típico) — vale para B2B/tickets altos; objetivo claro de lead, não tráfego.
- **Pinterest:** Smart Bids / objetivos por valor; visual first; útil em nichos de home, moda, beleza, gastronomia; intenção de busca forte ("vou fazer" não "estou vendo").
- **YouTube (YouTube Ads / Shorts):** view goals e in-stream com skip-after-5s; o primeiro segundo decide; Shorts Ads herdam a lógica TikTok-like.
- **Canais conversacionais (WhatsApp/DM/Telegram):** não são plataforma de mídia no leilão, são **extensões de canal**: anúncio → DM automatizado → humanização; medidos como etapa de conversão (lead qualificado), não como CAC isolado.

## 5. Regras transversais (todas as plataformas)

1. **Estabilidade > heroísmo:** contas com rotina consistente de sinais vencem contas que reinventam estrutura toda semana.
2. **Criativo é o novo (e quase único) alavanca de segmentação:** target amplo + criativo que "conversa" com o segmento certo.
3. **Dados de valor em dinheiro** sempre que possível (rotação, recorrência, LTV por segmento).
4. **Atribuição: cravar a régua antes** (última não-direct? janela de 7d click/1d view?) e nunca trocar de régua no meio de teste.
5. **Benchmark descreve o mercado; a conta descreve a sua conta.** (Regra R8.)
6. Toda mudança relevante fica registrada em `DEC-XXXX` com o mecanismo esperado — é assim que o 12 aprende o que o modelo ainda não sabe.
