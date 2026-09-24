# Contribuindo com o trafego-os

Regra de ouro: **nenhum prompt, agente ou playbook entra neste repositório sem exemplo de saída esperada.** Se não dá para mostrar o formato do artefato que ele produz, ele não está pronto.

## Fluxo
1. Fork + branch `feat/|fix/|doc/ — assunto`.
2. Se tocar em agente: manter a estrutura de `AGENT.md` (missão, protocolo socrático, input, output, rotina, regras duras, ferramentas, prompt de ativação).
3. Se tocar em número (benchmark, limiar): citar fonte e data da observação.
4. Teste do que for código: `python3 scripts/metrics.py data/exemplos/meta-daily-exemplo.csv` continua passando.
5. PR descreve: o que mudou, por quê (mecanismo), como testou.

## Convenções
- Português (BR) como língua do repositório; termos técnicos em inglês quando são padrão do setor (CBO, tROAS, learning phase).
- Métricas definidas em `docs/06-glossario-metricas.md`; conflito de definição perde para o glossário.
- Nomenclatura de artefatos segue `AGENTS.md` (REL-, DEC-, EXP-, INSITE-, FORECAST-, ALGO-).

## Onde cada coisa vive
| Tipo | Pasta |
|------|-------|
| Novo agente | `agents/NN-nome/AGENT.md` |
| Regra de operação | `AGENTS.md` (regras duras) ou `docs/01-socratismo.md` (método) |
| Benchmark | `docs/02` (plataforma) ou `docs/03` (economia) — com data e fonte |
| Playbook de campanha | `docs/07-estruturas-validadas.md` + JSON em `data/estruturas/` |
| Prompt de uso | `prompts/` |
| Template de artefato | `templates/` |
| Código | `scripts/` (stdlib apenas — dependência nova precisa de justificativa no PR) |
