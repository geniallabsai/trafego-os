# Roadmap

## Feito (v1.0–v1.1)
- [x] 14 agentes com protocolo socrático, rotinas, KPIs e prompt de ativação
- [x] Metodologia: socratismo, algoritmos (Meta·Andromeda/Google/TikTok), forecast, AAAR, direct response + black/white, glossário
- [x] Workflows de criação de conta (Meta MCP/CAPI, Google, TikTok) e pipeline bruto→insight
- [x] Estruturas validadas: Meta CBO/ABO, Google PMax/Search (doc 07 + JSON)
- [x] Scripts stdlib: metrics / ingest / forecast + dados de exemplo
- [x] Configuração de chaves: `config/.env` + mapa de consumo por agente + exemplo MCP
- [x] Logo

## Próximo (v1.2 — conectores)
- [ ] Conector Meta via MCP/API com leitura automática 08h (cron)
- [ ] Conector Google Ads (PMax + Search) com export diário
- [ ] Conector TikTok Ads
- [ ] Webhook ERP → `data/raw/` automático

## Depois (v1.3 — operação autônoma)
- [ ] Loop diário completo sem humano: ingest → INSITE → DEC → auditoria → execução → patch de forecast
- [ ] Dashboard simples (relatório semanal gerado em Markdown + gráfico)
- [ ] Multi-conta: parâmetros por cliente em `data/perfis/`
- [ ] Banco vivo automatizado: kills/valores do LABORATÓRIO alimentando o 05 no próprio repositório (PR automático)

## Estrelas (plano separado)
- Ver `GO-TO-STARS.md`.
