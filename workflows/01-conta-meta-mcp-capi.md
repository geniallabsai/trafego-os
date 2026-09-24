# Workflow — Meta: criação de conta e estrutura via token/MCP

Objetivo: com acesso concedido (token ou MCP), o sistema cria/organiza a conta Meta do zero à estrutura de campanha operacional. Rodar de cima a baixo; cada etapa confere a anterior antes de avançar (tracking errado é o erro nº 1 — doc 02 §1.4).

## 0. O que precisa ser conectado
- **MCP:** servidor MCP do Graph API/Marketing API com permissões: `ads_read`, `ads_management`, `pages_manage_ads`, `business_management` (leitura) — escrita só quando o 00 receber permissão de execução.
- **Ou token (fine-grained PAT/OAuth):** escopos `ads_read`, `ads_management` (fase 2), `read_insights`, `pages_read_engagement`.
- **Sem nada:** export manual via CSV em `data/raw/` — o método idêntico, execução humana.

## 1. Fundação (Business Manager → app → pixel)
1.1 Business Manager: nome da agência/cliente, moeda (BRL/USD), fuso (America/Sao_Paulo), domínio verificado (verificação de domínio é pré-requisito de CAPI e do Advantage+).
1.2 App de anúncio (ou ad account dedicada por cliente — regra da casa: **1 conta de anúncio por cliente**, nunca conta compartilhada entre clientes: histórico e aprendizado se misturam).
1.3 Criar Pixel + Conversions API:
   - Event ID padrão: `{{order_id}}_{{timestamp}}` — dedupe obrigatório.
   - Advanced Matching v2: email + telefone (hash SHA-256), sempre enviados no CAPI; UTM opcionais.
   - Eventos configurados na ordem de importância: **Purchase (com valor real)** > AddToCart > InitCheckout > Lead > ViewContent. Teste de evento no Events Manager (≥ 95% de correspondência web×server para Purchase antes de escalar).
1.4 Catalog (se EC): feed com SKU, título, descrição, preço, disponibilidade, imagem ≥ 1080px; sincronização diária (webhook/cron).
1.5 Validação ponta a ponta: evento de teste de R$ 1 (compra sandbox) rastreando pixel + CAPI deduplicados no mesmo evento ID.

## 2. Estrutura de campanha (padrão house)
```
Conta
├── COLD-[OFERTA]        (objetivo: Sales, otimização: Purchase c/ valor)
│   ├── AS-COLD-AMPLA    ( Advantage+ audience / público amplo, sem interesses)
│   │     └── ads: lote do agente 05 (R3: 3–5 hooks × big idea)
│   ├── AS-COLD-INTERESSE (opcional: 1 cluster de interesse alto, só se o amplo perder)
├── WARM-[OFERTA]        (objetivo: Sales; audiences: engajamento 30d + video 25–97% + site 7d não-comprador)
│   └── AS-WARM-COMBO    (ads: criativo de prova + objeção do 05/06)
├── HOT-[OFERTA]         (objetivo: Sales; audiences: cart 7d + checkout 7d + lead 3d)
│   └── AS-HOT-URG       (ads: urgência com motivo + garantia)
└── BRAND (defesa)        (Search/brand quando aplicável — Google lida; Meta brand raro)
```
Regras de estrutura:
- **CBO** (budget de campanha) nas campanhas COLD/WARM/HOT; ABM quando precisar isolar aprendizado por adset (ex.: teste de ângulo controlado).
- Naming convention (obrigatória, alimenta o 02): `NÍVEL-OFERTA-VARIÁVEL-YYYYMM`, ex.: `ADSET-COLD-A-BIG05HOOK03-2609`. Criativo: `CR-NNN-[ângulo]-[hook]`.
- Budget inicial cold = 60–70% do total, warm 15–25%, hot 10–15% (ajustar com dado do 02 em 14d).
- 1 objetivo de otimização por conta (Purchase c/ valor) — não misturar Lead e Purchase na mesma conta antes de 30d.

## 3. Pós-criação (primeiros 14 dias)
- Dia 0–3: checar learning phase, gasto real vs planejado, eventos chegando (CAPI log).
- Dia 3–7: primeira leitura do 02 (insuficiente para decisão, suficiente para anomalia técnica).
- Dia 7–14: primeira decisão estrutural (rebalancear budget cold/warm/hot, pausar adset sem 3 conv/dia após 7d).
- Registro: `DEC-0001` (estrutura criada) com as premissas — é a linha base de todo forecast posterior.

## 4. Checklist de saída
- [ ] Domínio verificado · [ ] Pixel+CAPI com dedupe validado (eventos teste batem) · [ ] Purchase com valor real nos dois lados · [ ] Nomeação house aplicada · [ ] Estrutura COLD/WARM/HOT no ar · [ ] Lote R3 em produção · [ ] `DEC-0001` registrada · [ ] Forecast dia 0 (benchmark pessimista) publicado pelo 12
