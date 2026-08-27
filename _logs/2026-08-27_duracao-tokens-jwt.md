# Log — duração dos tokens JWT

**Data:** 2026-08-27  
**Sessão:** access 15 min e refresh 6 meses (180 dias)

---

## ✅ O que foi feito

- Access token: 15 minutos.
- Refresh token: 180 dias.

## 📁 Arquivos criados

- `_logs/2026-08-27_duracao-tokens-jwt.md` — este log

## ✏️ Arquivos modificados

- `backend/app/core/config.py` — defaults
- `backend/.env` e `backend/.env.example`
- `docs/HOSTINGER.md` — modelo da VPS
- `README.md` — texto e exemplo de `.env`

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- Seis meses = 180 dias na variável já existente `REFRESH_TOKEN_EXPIRE_DAYS`.
- Tokens já emitidos guardam o `exp` antigo até o próximo login ou refresh.

## 📌 Observações

- Na VPS, editar `backend/.env` com os mesmos valores e subir a API (`./deploy.sh`). O Compose lê o `.env`; só o código novo não basta se o `.env` da VPS continuar com 30/30.
