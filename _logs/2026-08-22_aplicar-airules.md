# Log — aplicar airules frontend e backend

**Data:** 2026-08-22  
**Sessão:** adaptação do WorkHub às airules sem mudar visual nem funcionalidades

---

## ✅ O que foi feito

- Backend: `app/db/` (session/base), `app/api/dependencies/`, logger, middleware HTTP, ReDoc, escape de `%` no Alembic.
- Frontend: HTTP em `src/services/`, Zustand (`auth` + loader), `GlobalLoader` (barra fina no topo), interceptors Axios inalterados no comportamento (JWT + refresh).
- `src/api/` reexporta os services para não quebrar imports existentes.
- `.gitignore` alinhado; `_logs/` versionado.

## 📁 Arquivos criados

- `backend/app/db/base.py` / `session.py`
- `backend/app/api/dependencies/auth.py`
- `backend/app/core/logger.py` / `middleware.py`
- `frontend/src/services/*`
- `frontend/src/store/auth.store.ts` / `loader.store.ts`
- `frontend/src/components/GlobalLoader.tsx`
- `_logs/2026-08-22_aplicar-airules.md` — este log

## ✏️ Arquivos modificados

- `backend/main.py` — logging, ReDoc, middleware
- `backend/app/core/exceptions.py` — loga erros (JSON `{message}` igual)
- `backend/alembic/env.py` — `.replace("%", "%%")`
- rotas/scripts/testes — imports `db` / `dependencies`
- `backend/app/database/*` e `app/api/deps.py` — shims de compatibilidade
- `frontend/src/contexts/AuthContext.tsx` — hidrata o store Zustand
- `frontend/src/App.tsx` — GlobalLoader
- `frontend/src/types/index.ts` — tipo `ApiResponse`
- `frontend/package.json` — `zustand`
- `.gitignore`

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- `zustand` — estado global de auth e loader

## ⚠️ Decisões tomadas

- **Não** envelopar respostas em `{data,error}`: o front já consome o JSON atual; mudaria o contrato.
- **Não** prefixar `/api/v1` na app: o Caddy já usa `/api` (`VITE_API_URL=.../api`). Duplicar quebraria WS e o proxy.
- **Não** JWT extra / e-mail / forgot-password / switch-tenant: o produto é interno, usuário criado pelo admin, um `organization_id` por usuário. Troca de senha autenticada já existia.
- **Não** pandas: sem agregação tabular em memória.
- Visual das páginas intacto; só uma barra de progresso no topo durante requests.

## 🐛 Problemas encontrados e soluções

- Interceptor + retry 401 poderia deixar o loader preso → `start()` só se não for `_retry`.

## 📌 Pendências / próximos passos

- Commit/push quando pedido.
- VPS: pull + rebuild frontend/backend. Sem `down -v`.
- Testes de backend dependem do Postgres do `.env` (não rodados até o fim nesta sessão).
