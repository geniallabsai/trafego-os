# O Método Socrático — POR QUE · COMO · QUANDO · ONDE

Todo agente deste repositório é obrigado a responder quatro perguntas antes de qualquer ação, mais uma quinta que decide se é decisão ou teimosia.

## As cinco perguntas

### 1. POR QUE? (causa)
Qual é a hipótese causal? O "porque" tem que nomear o **mecanismo**, não o sintoma.

- ❌ "O anúncio está gastando pouco." (sintoma)
- ✅ "O anúncio saiu da fase de aprendizado porque cortamos 40% do budget no dia 3; o leilão voltou a exigir mais volume de conversões para estabilizar eCTR/eCVR." (mecanismo)

Nível aceitável de "porquê": a afirmação deve ser **falsificável**. Se nenhum dado poderia provar errado, é opinião vestida de análise.

### 2. COMO? (execução)
Passo a passo, em magnitude:
- Quanto: "+20% do budget diário", não "aumentar o budget".
- Onde dentro da conta: qual campanha/adset/criativo exatamente.
- Em que cadência: "3 dias seguidos, verificar CPA após cada etapa".
- Plano B: "se CPA passar 1.4× alvo na etapa 2, voltar ao valor anterior".

### 3. QUANDO? (tempo)
- Janela de observação mínima antes de julgar o efeito (ex.: 48h; para mudanças de bid, 72h).
- Data-hora de revisão marcada.
- Condição de entrada: "só executo após o corte de dados das 08h".
- Condição de saída: o que encerra o teste, e quando ele vira decisão permanente.

### 4. ONDE? (escopo)
- Plataforma, conta, campanha, placement, público, região, horário.
- Escopo de replicação: isso vale só pra essa conta ou vira padrão? Padrão só com 2 contas confirmando.

### 5. O que me faria mudar de ideia?
A pergunta que separa o analista do apostador. Exige:
- Uma métrica observável (CPA, CVR, ROAS, fatigue…).
- Um limiar numérico (CPA > 1.5× alvo).
- Uma consequência explícita ("reverso a escala na hora, sem drama").

## Aplicação por tipo de decisão

| Decisão | Respostas mínimas exigidas |
|---------|---------------------------|
| Escalar budget | POR QUE: ROAS ≥ break-even 3d + CPA ≤ 1.2× alvo · COMO: +20%/dia · QUANDO: revisar em 72h · ONDE: adset específico · MUDAR IDEIA se CPA > 1.4× alvo por 48h |
| Pausar criativo | POR QUE: fatigue index < 0.7 OU CPA 1.5× por 48h · COMO: pausar o ad, manter adset · QUANDO: após corte 08h · ONDE: ad id X · MUDAR IDEIA se CVR subir 24h após troca de hook |
| Testar ângulo novo | POR QUE: lacuna de evidência no funil (stair-step de ângulos) · COMO: lote de 3–5 ads, budget mínimo de aprendizado · QUANDO: 5–7 dias · ONDE: adset dedicado 10–15% do budget · MUDAR IDEIA se CTR lote < 0.8× média da conta |
| Mudar bid (tROAS/tCPA) | POR QUE: desvio do target > 20% por 7d · COMO: ajuste ≤ 15% de uma vez · QUANDO: janela de 72h pós-mudança · ONDE: adset com ≥ 50 conv/semana |

## Anti-padrões que o agente 01 rejeita na hora

1. **Sobrevivência:** "está funcionando, então continua." (Só resta o que sobreviveu — por quê? Qual seleção fez?)
2. **Um dia de dado como tese:** qualquer conclusão sobre tendência exige ≥ 3 pontos temporais fora de pico.
3. **Correlação vestida de causa:** CPM subiu quando lançamos vídeo novo → e daí? Mecanismo proposto: "leilão mais disputado por causa da Black Friday chegando" (sazonalidade documentada) vs. "nosso vídeo".
4. **Sem limiar:** "vou ver como anda" não é plano.
5. **Escopo difuso:** "otimizar a conta" não é ação. Nome a conta, o objeto, o parâmetro.

## Ritual diário do Guardião (agente 01)

Toda DEC-XXXX é auditada nesta ordem. Se qualquer campo falhar, devolve com a pergunta específica em falta — nunca com "parece pouco fundamentado". O formato da devolução é fixo:

```
DEC-0042 REJEITADA
Faltou: QUANDO (sem data de revisão)
Exigir: revisar em 2026-09-27 09h com limiar de CPA ≤ R$ 87
```
