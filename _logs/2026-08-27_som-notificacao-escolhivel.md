# Log — som de notificação escolhível

**Data:** 2026-08-27  
**Sessão:** o usuário escolhe o toque da mensagem; catálogo pronto para mais arquivos

---

## ✅ O que foi feito

- Três toques em `frontend/public/sounds/`.
- Seletor na sidebar (com botão de ouvir).
- Escolha gravada no `localStorage` por usuário.
- Nova mensagem usa o arquivo escolhido; se o play falhar, cai no beep antigo.

## 📁 Arquivos criados

- `frontend/public/sounds/toque-1.wav`
- `frontend/public/sounds/toque-2.wav`
- `frontend/public/sounds/toque-3.wav`
- `frontend/src/utils/notificationSounds.ts` — catálogo (é só acrescentar linha + arquivo)
- `frontend/src/store/notificationSound.store.ts`
- `frontend/src/components/NotificationSoundPicker.tsx`
- `_logs/2026-08-27_som-notificacao-escolhivel.md` — este log

## ✏️ Arquivos modificados

- `frontend/src/utils/alerts.ts` — toca o arquivo do catálogo
- `frontend/src/utils/storage.ts` — persistência do id do som
- `frontend/src/layouts/AppLayout.tsx` — seletor acima de Minha conta

## 🗑️ Arquivos removidos

- —

## 🔗 Dependências adicionadas

- —

## ⚠️ Decisões tomadas

- Sem backend: preferência por browser/usuário.
- Pixabay (juniorsoundays) bloqueou download automático (Cloudflare). Os três arquivos atuais são toques curtos gerados no repo, no mesmo formato que o player já aceita (WAV ou MP3).
- Para usar os MP3 do Pixabay: gravar em `frontend/public/sounds/` e apontar `file` no catálogo (ex.: `toque-1.mp3`).
- Autor pretendido: [juniorsoundays](https://pixabay.com/users/juniorsoundays-19205462/) — Pixabay Content License.

## 📌 Observações

- Não altera o visual das páginas; só entra um bloco pequeno na sidebar.
