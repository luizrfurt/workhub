# Log — previsão de esgotamento da cota

**Data:** 2026-08-24  
**Sessão:** previsão de quando a cota de armazenamento deve encher, no dashboard

---

## ✅ O que foi feito

- Backend estima a data de esgotamento com a média de bytes dos anexos dos últimos 30 dias (ou desde o anexo mais antigo, se a conta for mais nova).
- O card de armazenamento do dashboard mantém o contador atual e ganha uma linha de previsão.
- Sem migration: usa `size` e `created_at` dos anexos já gravados.

## 📁 Arquivos criados

- `backend/app/services/storage_forecast.py` — cálculo puro da previsão
- `backend/tests/test_storage_forecast.py` — casos da média / cota cheia / sem histórico
- `frontend/src/utils/storageForecast.ts` — texto da previsão
- `_logs/2026-08-24_previsao-cota-armazenamento.md` — este log

## ✏️ Arquivos modificados

- `backend/app/repositories/message_repository.py` — soma e `created_at` mínimo na janela
- `backend/app/repositories/task_repository.py` — idem para anexos de tarefa
- `backend/app/services/project_service.py` — inclui previsão no overview e no `/storage`
- `backend/app/schemas/project.py` — campos `storage_forecast_*`
- `backend/tests/test_permissions.py` — assert do status sem histórico
- `frontend/src/types/index.ts` — tipos da previsão
- `frontend/src/pages/Overview/OverviewPage.tsx` — linha extra no card

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- Janela de 30 dias; mínimo 3 anexos na amostra e 7 dias de histórico para exibir data.
- Sem tabela de snapshot diário. Arquivos apagados deixam de entrar na média.
- Contador “X de 10 GB” e a barra permanecem iguais.

## 🐛 Problemas encontrados e soluções

- —

## 📌 Pendências / próximos passos

- —
