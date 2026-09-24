# Estruturas de campanha validadas (blueprints house)

Quatro estruturas com status de **validada** neste sistema: Meta CBO, Meta ABO, Google PMax, Google Search. Cada uma tem quando usar, árvore exata, regras de budget/bid, critérios de saída/escala e erros que a matam. Versões de máquina em `data/estruturas/` (JSON) — o agente carrega e monta.

## Matriz de escolha (qual estrutura, para quê)

| Cenário | Estrutura | Por quê |
|---------|-----------|---------|
| Escalar oferta validada, entrega estável | **Meta CBO** | O orçamento otimizado da campanha deixa o sistema alocar onde o eCTR×eCVR paga menos; menos mão no volante = menos learning phase reiniciada |
| Testar ângulos/hooks/públicos com veredito controlado | **Meta ABO** | Isolamento de variável: budget fixo por braço, mesma duração, veredito numérico; escala o vencedor de volta para CBO |
| EC com catálogo, todas as superfícies | **Google PMax** | Feed + assets cobrem YouTube/Search/Discovery/Gmail com otimização por item/oferta |
| Defesa de marca + captura de demanda ativa | **Google Search** | Intenção explícita; brand barateia defesa, non-brand mede desejo |
| Social nativo, criativo-first | TikTok (workflow 03) | CBO + lotes R3 + Spark Ads — já documentado em workflows/03 |

Regra geral: **CBO é o padrão de escala; ABO é a exceção com prazo (teste termina); PMax nunca multi-oferta; Search sempre separa brand/non-brand.**

---

## A. META CBO — escala (padrão house)

```
Conta
├── CAMP-COLD-[OFERTA]          objetivo: Sales · otimização: Purchase c/ valor · CBO
│   ├── AS-COLD-AMPLA           Advantage+/ampla (sem interesses)
│   │     └── 3–5 ads (lote R3: 1 big idea × 3–5 hooks)
│   ├── AS-COLD-CLUSTER (opcional, só se AMPLA perder após 14d) 1 cluster de interesse alto
│   └── (ads novos entram em AS-AMPLA em lote; nunca 1 ad órfão)
├── CAMP-WARM-[OFERTA]          objetivo: Sales · CBO
│   └── AS-WARM-COMBO           engajamento 30d + vídeo 25–97% + site 7d não-comprador
│         └── 2–3 ads (prova + objeção)
└── CAMP-HOT-[OFERTA]           objetivo: Sales · CBO
    └── AS-HOT-URG              carrinho 7d + checkout 7d + lead 3d
          └── 1–2 ads (urgência c/ motivo + garantia)
```

**Regras**
- Objetivo de otimização: **Purchase com valor real** (CAPI validada, workflow 01 §1). Sem valor, o sistema otimiza quantidade, não receita.
- Bid: começar em **Lowest Cost** (fase de construção); migrar para **Cost Cap** (teto = CPA-alvo × 1.2) somente com ≥ 30 conv/semana na campanha.
- Budget: mínimo diário da campanha COLD ≥ 2× CPA-alvo (senão não alimenta o aprendizado); mudanças **±20%/dia** (R1/R5); realocação cold/warm/hot somente em DEC com data.
- Distribuição inicial: cold 60–70% · warm 15–25% · hot 10–15% (rebalancear com dado do 02 em 14d).
- Learning phase: cortar budget > 20% reinicia; mudança de objetivo/público CBO↔ABO também — registrar em DEC.
- Nomeação: `CAMP-COLD-BLACK-MEC-2609` / `AS-COLD-AMPLA-2609` / `CR-NNN-ang-hook` (obrigatória; o nome é metadados).

**Critérios**
- Escala: ROAS ≥ break-even por 3d e CPA ≤ 1.2× alvo → +20%/dia, máx 3 passos, revisão 72h.
- Pausar campanha: sem vencedor em 14d OU CPA > 2× alvo por 7d.
- Pausar ad: fatigue < 0.7 OU CPA > 1.5× por 48h (R4) — adset segue, lote novo em 48h (pipeline do 11).

**Erros que matam CBO**
1. Micro-budget "para testar" (morre sem aprender — teste de verdade é ABO com duração declarada).
2. Mover 40% do budget numa DEC (reinicia aprendizado e o time culpa o "algoritmo").
3. Múltiplos objetivos de otimização na mesma conta (Purchase + Lead misturados).
4. Criativo único em adset (sem lote, não há veredito).

---

## B. META ABO — teste controlado (exceção com prazo)

**Quando:** testar ângulos, hooks, públicos, bids ou ofertas com veredito numérico confiável. Sempre com: variável única, duração máxima declarada, tamanho de amostra estimado (template EXP).

```
CAMP-TEST-[OFERTA]-[VARIÁVEL]-YYYYMM   ABO (budget por adset)
├── AS-CTRL (controle: criativo/ângulo vigente)   budget X/dia · 3 ads
├── AS-VAR1 (variação 1)                          budget X/dia · 3 ads
└── AS-VAR2 (variação 2)                          budget X/dia · 3 ads
```

**Regras**
- Budget por adset idêntico; voo simultâneo; mesmo horário de ativação (mesmo dia, mesma hora — evita sesgo de horário).
- Duração: **5–7 dias OU N conversões** (N = amostra mínima do EXP, o que ocorrer depois); data de morte no EXP antes de ligar.
- 1 variável por campanha-teste. Ângulo + hook + público juntos = não saber o que venceu.
- Métrica de decisão por tipo de teste: criativo → CTR+HCR (leading) e CPA (lagging); público → CPA; oferta → CVR×AOV (margem contributiva).
- Veredito: vencedor = superioridade com confiança ≥ 95% OU consistência 7d com amplitude confortável (template EXP). Empate técnico → decidir por custo de produção/escala, documentar.
- Pós-veredito: vencedor vai para **CBO de escala** (nova DEC); perdedores vão para o LABORATÓRIO do 05 com motivo (post-mortem resumido).

**Erros que matam ABO**
1. Testar com budget tão baixo que nenhum braço sai do ruído (amostra infinita).
2. ABO sem data de morte (teste vira campanha eterna de micro-spend).
3. Conferir no dia 2 e "ajustar" (matou o teste; leu o ruído).

---

## C. GOOGLE PMAX — catálogo e todas as superfícies

**Quando:** EC com catálogo saudável; quando Search non-brand já valida demanda e se quer expandir para vídeo/discovery. 1 PMax **por oferta/família de oferta** — nunca 1 gigante multi-oferta.

```
Conta
├── PMAX-[OFERTA-A]        conversões: Purchase c/ valor (importadas) · exclusões configuradas
│   ├── ASSET-GROUP: tema principal da oferta (15 headlines, 5 descriptions, 10 imagens, 1 logo)
│   ├── ASSET-GROUP: mecanismo/prova
│   └── ASSET-GROUP: oferta/urgência (se aplicável)
└── PMAX-[OFERTA-B]        (idem, oferta separada)
```

**Regras**
- Feed: SKU, preço real, disponibilidade sincronizada diariamente (feed morto = PMax cega).
- Exclusões: search keywords de campanhas SEARCH ativas (evita disputa interna); públicos negativos se houver lista de clientes (decidir por oferta).
- Bid timeline: **Maximize Conversions (volume)** nas primeiras 2–4 semanas para construir histórico → **tROAS** somente com ≥ 30 conv/30d, iniciando em **ROAS observado × 0.9** (tROAS agressivo cedo = sistema vai caçar conversões pequenas).
- Ajuste de tROAS: ≤ 15% de cada vez, janela de 72h, DEC registrada.
- Search terms e asset report semanais (04): o que clica, o que converte, o que excluir.
- Budget: PMax e SEARCH não disputam o mesmo centavo por acidente — a divisão vem da leitura de CAC por superfície (DEC), não de palpites.

**Erros que matam PMax**
1. Multi-oferta num PMax (mensagem misturada, atribuição morta).
2. tROAS de sonho no dia 1.
3. Assets genéricos sem tema (o asset group É a segmentação criativa do PMax).
4. Comparar PMax com Search por ROAS bruto sem olhar sobreposição de conversões (o mesmo pedido pode aparecer nos dois — régua de atribuição cravada, workflow 02 §1.2).

---

## D. GOOGLE SEARCH — brand + non-brand

**Quando:** sempre que existe marca buscável (brand) e intenção ativa no nicho (non-brand). Defesa + demanda.

```
Conta
├── SEARCH-BRAND        match: exatas (+ frases curtas) de marca e variações
│   └── 1–2 adgroups · RSA: promessa + prova + CTA defensivo
└── SEARCH-NONBRAND     1 tema por adgroup (≤ 15 keywords relacionadas)
    ├── ASG: [dor/principal intenção]
    ├── ASG: [comparação/mechanism-related]
    └── ASG: [compra direta]
        RSA por tema (15 headlines ≤ 30ch, 4 descriptions ≤ 90ch, CTA dominante)
```

**Regras**
- Brand e non-brand **sempre separadas** (métrica de defesa ≠ métrica de desejo; budget e leitura diferentes).
- Match types: exatas + frases primeiro; broad **somente** com negativas sob controle (auditoria semanal de search terms pelo 04; negativas entram toda semana, sem exceção).
- Landing com **message match**: keyword/âncora do grupo aparece na headline da página; LCP < 2.5s (componente real do Ad Rank).
- QS é multiplicador de custo: relevância de anúncio + landing pagam o tráfego; adgroup com QS médio < 6 por 2 semanas revisa keywords/RSAs.
- Bid: máximo com teto (brand) / maximize conversions com valor → tCPA com ≥ 15–30 conv/30d.
- Negativas estruturais (info/gratuito/concorrente quando não queremos) mantidas em lista viva do 04.

**Erros que matam Search**
1. Broad sem rotina de negativas (burn em termos que não convertem).
2. Adgroup-sopa (5 temas juntos → QS diluído, RSA sem message match).
3. Brand e non-brand juntas (não dá para dizer o quanto a marca está sendo defendida).
4. Ignorar auction insights em disputa de marca (quem está leiloando junto?).

---

## Regras transversais (todas as estruturas)
1. Naming house obrigatória (metadados pelo nome).
2. 1 objetivo de otimização por conta/plataforma até 30d de maturidade.
3. Toda estrutura nasce com DEC-ESTRUTURA (premissas + gatilhos de revisão dia 3/7/14).
4. Toda mudança estrutural passa pelo 01 (Sócrates) — "mover para CBO porque ABO tá caro" sem amostra é feeling.
5. A estrutura serve ao funil AAAR: COLD/WARM/HOT correspondem a aquisição→ativação→receita; warm/hot sem criativo próprio (prova/urgência) é desperdício.
