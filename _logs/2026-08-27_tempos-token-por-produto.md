# Log — tempos de token (WorkHub vs ClockUp)

**Data:** 2026-08-27  
**Sessão:** WorkHub permanece 15 min de access e 180 dias de refresh

---

## ✅ O que foi feito

- Sem mudança de duração: access 15 min, refresh 180 dias.
- HOSTINGER deixa explícito que o refresh é revogável no banco.

## 📁 Arquivos criados

- `_logs/2026-08-27_tempos-token-por-produto.md` — este log

## ✏️ Arquivos modificados

- `docs/HOSTINGER.md` — nota de que o refresh está no banco

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- WorkHub: 15 min / 6 meses, porque o refresh é opaco, rotaciona e o logout revoga.
- ClockUp ficou em 15 min / 30 dias (JWT sem revogação).
