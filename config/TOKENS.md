# Chaves & Tokens — quién usa o quê

Regra da casa: **o time lê primeiro e escreve depois**. Chave de leitura habilita análise, previsão, relatório. Chave de escrita habilita execução (mover budget, criar/pausar anúncio) — e essa só entra quando o agente 00 passar pelo handshake do `AGENTS.md`.

## 1. Preencher

```bash
cp config/.env.example config/.env
# edite config/.env com suas chaves
```

- O `.env` **nunca** vai pro git (`.gitignore` cobre).
- Se uma chave apareceu em chat/print/log, ela é rota: **gere outra**.
- Menor privilégio: comece tudo em leitura; adicione escrita plataforma por plataforma, conforme o time ganha confiança (o 01 audita execução, não só decisão).

## 2. Quém consome cada chave

| Variável | Para quê | Agentes que usam | Fase |
|----------|----------|------------------|------|
| `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` / `OPENROUTER_API_KEY` | gerar criativos, hooks, copy, ofertas, análises em linguagem natural | 02, 03, 05, 06, 07, 08, 09, 10, 11 (05–11 são os maiores consumidores) | 1 |
| `TRAFEGO_LLM_*` | escolha de provider/modelo/temperatura por tarefa | todos (criativo quente, análise fria) | 1 |
| `META_SYSTEM_USER_TOKEN` | ler insights, campanhas, ads, diagnósticos, learning phase | 02 (dados), 04 (diagnóstico), 11 (fatigue), 12 (forecast calibrado), 13 (relatório) | 1 |
| `META_WRITE_TOKEN` | criar/pausar anúncios, mover budget, ajustar bid | 00 (execução, sempre após auditoria do 01) | 2 |
| `GOOGLE_DEVELOPER_TOKEN` + OAuth trio | ler campanhas/search terms/auction insights; executar PMax/Search | 02, 03, 04 (leitura) · 00 (escrita) | 1/2 |
| `TIKTOK_ACCESS_TOKEN` | ler stats de campanha/adgroup/creative; Spark Ads | 02, 04, 11 (leitura) · 00 (escrita) | 1/2 |
| `GITHUB_TOKEN` | push/pull dos artefatos (DEC, INSITE, REL, FORECAST) e dos scripts | pipeline (versionamento do sistema inteiro) | 1 |
| `GA4_MEASUREMENT_ID` | etapas de funil no site (ativação/engajamento) | 02, 06, 08 | 1 |
| `ERP_WEBHOOK_URL` | receita real por pedido (evita ROAS inflado de plataforma) | 02, 12, 13 | 1 |
| `FX_USD_BRL` | conversão de exports em dólar | ingest.py | 1 |

## 3. Conectando via MCP (quando disponível)

Os agentes aceitam os mesmos dados por MCP em vez de CSV. Exemplo de configuração em `config/mcp.example.json` (copie para `config/mcp.local.json`, ajuste os comandos ao servidor MCP que você roda — confira as versões atuais dos pacotes):

- `meta-ads`: expõe insights, campaigns, adsets, ads, creatives (leitura) e mutações (escrita).
- `google-ads`: expõe contas, campanhas, keywords, assets, performance.
- `tiktok-ads`: expõe campaigns, adgroups, ads, creatives, stats.

Ordem de conexão recomendada: **leitura Meta → leitura Google → leitura TikTok → escrita Meta → escrita Google → escrita TikTok**. A cada conexão: o agente 02 confere tracking ponta a ponta antes de o 00 tocar em budget (workflow 01 §1).

## 4. O que muda quando as chaves chegam

1. **Sem chave:** método 100% em modo humano-na-loop — os arquivos são o contrato, o humano executa.
2. **Chave LLM:** agentes criativos/análise geram artefatos direto (big ideas, hooks, copy, INSITE interpretados).
3. **Chave de leitura de plataforma:** o dia operacional de 08h roda sozinho: ingest → métricas → INSITE → relatório.
4. **Chave de escrita:** o anel fecha sem humano no meio — DEC aprovada pelo 01 vira mutação na conta via MCP/API, e o 12 aplica patch do forecast automaticamente.
