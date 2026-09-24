# Workflow — TikTok Ads: criação de conta e estrutura

## 0. Conexão
- TikTok Marketing API: Access Token (Business Center) com permissões de leitura (fase 1) e gestão (fase 2); Organization (Business Center) com o perfil orgânico vinculado (pré-requisito de Spark Ads).
- MCP: servidor MCP TikTok Ads (campaigns, adgroups, ads, creatives, stats) quando disponível.
- Sem API: export de relatórios em `data/raw/`.

## 1. Fundação
1.1 Business Center: organização → conta de anúncio (1 por cliente) → vínculo com perfil orgânico/creator (para Spark).
1.2 Pixel TikTok + Events API (server-side): eventos Purchase (valor), AddToCart, CompletePayment, Lead; matching hash (email/phone). Verificar dedupe pixel×API.
1.3 Conversões com valor; objetivo de otimização: CompletePayment/Purchase com valor para ofertas; Lead para serviços.

## 2. Estrutura (padrão house — creative-first)
```
Organização → Conta
├── CAMP-COLD-[OFERTA]   (CBO; adsets: ampla + 1 cluster de interesse opcional)
│     Cada adgroup: 3–5 criativos nativos (UGC-like, hook falado + escrito, som nativo, subtítulo)
├── CAMP-WARM-[OFERTA]   (públicos de engajamento/vídeo via Custom Audiences)
└── SPARK-COLD           (posts orgânicos/creator performantes promovidos — social proof + distribuição)
```
Regras:
- Criativo é a segmentação (doc 02 §3): lote mínimo 3 criativos por adgroup desde o dia 1 (R3).
- Formato nativo: vertical 9:16, 15–34s, hook nos 2 primeiros segundos (falado E escrito), CTA único.
- Spark Ads: usar posts com engajamento orgânico > média (top 10% dos últimos 30 dias) — promover organic que já provou.
- Budget: cold 70–80%, warm 20–30%; bidding CBO padrão; tCPA somente com histórico.
- Comentários sob o post são sinal: o 07 responde em < 1h comercial; perguntas recorrentes viram hooks novos (05).

## 3. Primeiros 14 dias
- Dia 0–3: delivery iniciando? eventos chegando? learning phase ok (volume de conversão)?
- Dia 3–7: criativos: thumbstop 1s/3s, VCR; cortar os 2 piores do lote (não o adgroup inteiro — R4 respeitada em espírito: 48h mínimos por criativo ativo).
- Dia 7–14: escala dos vencedores (+20%/dia R5); entrada de novo lote mantendo pipeline do 11.
- `DEC-0003` registra estrutura.

## 4. Checklist de saída
- [ ] Business Center + vínculo perfil orgânico · [ ] Pixel + Events API validados (dedupe ok) · [ ] Objetivo de otimização com valor · [ ] CBO + lotes R3 no ar · [ ] Spark ativo com posts top · [ ] SLA de comentários (07) definido · [ ] DEC-0003 · [ ] Forecast dia 0 publicado
