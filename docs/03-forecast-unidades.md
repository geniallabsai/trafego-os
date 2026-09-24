# Forecast de custos e vendas — a matemática que sustenta a decisão

Todo forecast deste repositório é **três coisas ao mesmo tempo**: um modelo de funil, uma calibração contra a conta real e uma banda de erro explícita. Número sem banda de erro é achismo com calculadora.

## 1. O funil-base (unidades)

```
Budget (R$) ──▶ Impressões  = Budget / (CPM/1000)
Impressões   ──▶ Cliques    = Impressões × CTR
Cliques      ──▶ Leads     = Cliques × CVR_lead        (se funil tem lead)
Leads        ──▶ Vendas    = Leads × Taxa_fechamento
(Via direta) Vendas        = Cliques × CVR_directo
Vendas       ──▶ Receita   = Vendas × Ticket_médio
Receita      ──▶ Lucro c/ variável = Receita × Margem_bruta − Budget
```

Métricas derivadas:
- **CAC** = Budget / Vendas
- **ROAS** = Receita / Budget
- **ROAS break-even** = 1 / Margem_bruta (ex.: margem 60% → ROAS_BE = 1.67)
- **LTV** = Ticket × Margem_bruta × (1 + f_repurchase) — onde f_repurchase = soma dos fatores de recompra ponderados (ex.: 1 recompra média a 70% do ticket → f = 0.7)
- **LTV:CAC** ≥ 3 saudável para mídia paga; payback < 30 dias para escala agressiva.
- **MER** = Receita total / Gasto total em mídia (a régua de verdade; ROAS isolado pode ser bonito com atribuição generosa).

## 2. De onde vêm os parâmetros (hierarquia R8)

1. **Conta real (28 dias, ponderada por gasto)** — sempre que existir histórico suficiente.
2. **Teste ativo recente** — quando o teste mede exatamente o parâmetro em falta (ex.: novo criativo testa CTR).
3. **Benchmark de mercado** — intervalo por plataforma/placement/nicho/região (ver tabela abaixo). Usar o **pessimista** para plano e o **base** para conversa; nunca o otimista como promessa.
4. **Analogia de conta gêmea** — outra conta da agência com mesmo funil/preço/região (documentar semelhança).

### Benchmarks de referência (Brasil; calibrar sempre — rótulo "benchmark" obrigatório no relatório)

| Parâmetro | Faixa típica | Nota |
|-----------|--------------|------|
| CPM Meta BR | US$ 10–35 (nicho info/educação tende ao topo na alta temporada) | Sazonalidade pesa: Black Friday/11 eleva leilão geral |
| CPM Meta US | US$ 15–45 | |
| CTR Feed Facebook | 0.8–1.4% | Abaixo de 0.6% = criativo problemático em cold |
| CTR Reels/Stories (criativo nativo forte) | 1.2–2.5% | |
| CTR Search Google non-brand | 1.5–4% | Brand: 5–15% |
| CVR landing EC | 1.5–3% | Checkout 1-página + urgência empurra ao topo |
| CVR info white ticket | 3–6% | Oferta boa + página focada |
| CVR lead gen local | 5–12% | |
| Fechamento lead→venda (outbound humano) | 10–40% | Depende de SLA de atendimento (< 5 min ajuda muito) |
| Frequência cold sustentável | < 4–5 antes de fatigue visível | Cruzar com índice de fatigue do agente 11 |

## 3. Sazonalidade e mercado

- **Calendário:** Black Friday (outubro-leilão já sobe em setembro), virada do ano (segurança, planejamento), fevereiro (retornos/padrinhos de ano novo — pico de CPM), julho (calor de recesso: CPM cai), dias de evento macro (câmbio, política econômica → intenção de compra).
- **Alvo:** para cada mês do ano, guardar multiplicadores sazonais **observados na própria conta** (ex.: "set/2026 CPM = 1.3× média anual"). Sem histórico próprio, usar multiplicador setorial conservador e marcar `benchmark-sazonal`.
- **Concorrente:** entrada/saída de grandes players no leilão muda CPM rápido — o agente 03 alimenta o radar semanalmente.

## 4. Os três cenários (obrigatório)

Toda projeção sai em **3 cenários**:
- **Pessimista:** CPM +20%, CTR −15%, CVR −20%.
- **Base:** parâmetros calibrados hierarquicamente.
- **Otimista:** CPM −10%, CVR +10% (só com fundamento documentado: novo ângulo validado, oferta testada).

Entrega padrão (formato do agente 12):

```
FORECAST 30D — Conta X
Base:      rev R$ 84.0k · ROAS 2.10 · CAC R$ 58 · margem c/ var R$ 21.3k
Pess.:     rev R$ 66.4k · ROAS 1.58 · CAC R$ 76
Otimista:  rev R$ 96.2k · ROAS 2.61 · CAC R$ 49
Desvio vs realidade (últimos 28d): MAPE 11% | tendência: estável
Ajustes:   CPM observado subiu 14% s/w — recalibrei base para +12% (sazonal outono, fonte: conta 28d)
```

## 5. Calibração contínua (o loop passado→futuro)

1. Todo dia: desvio_dia = (real − previsto)/previsto por métrica-chave (CPM, CTR, CVR, receita).
2. Rolling 7d/28d: se |desvio| > 15% por 3 dias seguidos, o forecast é recalibrado e **a causa é investigada pelo agente 04** (leilão? criativo? checkout? sazonal? mudança de plataforma?).
3. Mensal: MAPE por parâmetro; parâmetros com MAPE > 25% entram em revisão (fontes erradas ou mercado mudou).
4. Toda DEC-XXXX que muda a realidade (nova oferta, nova campanha) gera um "patch" de forecast na hora — o modelo não fica cego do que o time causou.

## 6. Quando NÃO há dados da conta

Conta nova: primeiro forecast usa benchmark pessimista como plano de mídia (não como promessa), com **plano de aprendizado** explícito: semanas 1–2 rodando estrutura mínima (2 campanhas × 3 criativos), coleta de sinais, e recalibração completa no dia 14 e no dia 28. Promessa ao cliente nessa fase é sobre **velocidade de aprendizado**, não ROAS.
