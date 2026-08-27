# Log — canal Geral

**Data:** 2026-08-27  
**Sessão:** projeto especial só de conversa, com todos os usuários

---

## ✅ O que foi feito

- Canal **Geral** por organização: só conversa, sem tarefas.
- Todo usuário ativo entra automaticamente (criação de admin, de colaborador e no listar projetos).
- Não dá para editar, excluir nem gerenciar membros do Geral.
- Dashboard de tarefas não lista o Geral.

## 📁 Arquivos criados

- `backend/alembic/versions/004_general_channel.py`
- `backend/tests/test_general_channel.py`
- `_logs/2026-08-27_canal-geral.md` — este log

## ✏️ Arquivos modificados

- `backend/app/models/project.py` — `is_general`
- `backend/app/schemas/project.py`
- `backend/app/repositories/project_repository.py` / `user_repository.py`
- `backend/app/services/project_service.py` / `auth_service.py` / `task_service.py`
- `backend/app/api/routes/projects.py`
- `frontend/src/types/index.ts`
- `frontend/src/pages/Dashboard/DashboardPage.tsx`
- `frontend/src/pages/Project/ProjectPage.tsx`

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- Continua sendo um `Project` (reusa chat, unread, WebSocket), não uma entidade nova.
- Um Geral por organização (índice único parcial).
- Tarefas no Geral: 403 na API; aba some no front.

## 📌 Observações

- Na VPS: `./deploy.sh` e `docker compose exec workhub-api alembic upgrade head`.
- O canal aparece no primeiro `GET /projects` depois da migration.
