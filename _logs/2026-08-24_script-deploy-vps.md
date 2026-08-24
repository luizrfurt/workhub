# Log — script de deploy na VPS

**Data:** 2026-08-24  
**Sessão:** `deploy.sh` com git pull + rebuild do Docker

---

## ✅ O que foi feito

- Script na raiz: `git pull && docker compose up -d --build`, a partir da pasta do script.
- HOSTINGER aponta para `./deploy.sh`; Alembic continua separado.

## 📁 Arquivos criados

- `deploy.sh` — pull + compose build
- `_logs/2026-08-24_script-deploy-vps.md` — este log

## ✏️ Arquivos modificados

- `docs/HOSTINGER.md` — seção de atualizar usa o script

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- Sem `alembic` no script: o pedido era só pull + rebuild. Migration continua manual no WorkHub.
- Sem `down -v`.

## 🐛 Problemas encontrados e soluções

- —

## 📌 Pendências / próximos passos

- Na VPS: `chmod +x deploy.sh` na primeira vez.
