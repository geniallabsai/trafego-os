# Dicionário de métricas (régua única do repositório)

Regra R6: citar a origem de cada número. Fonte padrão: `conta-28d` (ponderado por gasto), `conta-7d`, `benchmark`, `teste-XXXX`, `forecast`.

| Métrica | Fórmula | Nota operacional |
|---------|---------|------------------|
| CPM | Spend ÷ Impressões × 1000 | Custo do leilão bruto |
| CPC | Spend ÷ Cliques | CPM/(1000×CTR) |
| CTR | Cliques ÷ Impressões | Vital do criativo; comparar sempre com média da conta |
| CPA | Spend ÷ Conversões | A régua tática; alvo definido por oferta |
| CAC | Spend ÷ Vendas | CAC blended soma paid + promoções atribuídas |
| CVR | Conversões ÷ Cliques | Por landing/oferta; separar cold de retargeting |
| ROAS | Receita atribuída ÷ Spend | Atribuição cravada antes do teste (doc 03 §1) |
| ROAS break-even | 1 ÷ Margem_bruta | O número que separa crescer de sangrar |
| MER | Receita total ÷ Mídia total | A régua de verdade anti-atribuição-generosa |
| AOV | Receita ÷ Pedidos | Alvo do agente 09 (bump/upsell/downsell) |
| LTV | Ticket × margem × (1+f_repurchase) | Janela mínima 90d; 12m ideal |
| LTV:CAC | LTV ÷ CAC | ≥ 3 saudável; > 5 sugere sub-investimento |
| Payback | Dias para o lucro contributivo pagar o CAC | < 30d p/ escala agressiva |
| Frequência | Impressões ÷ Reach | Cold > 4–5 = cheiro de cansaço (combinar c/ fatigue) |
| Fatigue index | CTR_ultimos3d ÷ CTR_primeiros3d | < 0.7 = renovar (agente 11); ≥ 1.0 criativo rejuvenescendo (novo público) |
| eCTR/eCVR | Estimativas de clique/conversão do modelo | Não visíveis diretamente — inferidas por diagnósticos |
| MAPE | Média dos \|erro\| relativos do forecast | < 15% bom; > 25% recalibrar parâmetro |
| HCR (hook rate) | Views ≥ 3s ÷ Impressões (Meta) | Vital do hook; alvo ≥ 25–30% em frio |
| Thumbstop | Views 3s ÷ Views 1s | Primeiros 3 segundos do vídeo |
| VCR (video) | Views 25–75% ÷ Impressões | Vital do corpo de vídeo |
| MER-safeguard | MER ≥ 2× ROAS_be | Regra de segurança contra ROAS inflado |
