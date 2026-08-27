export type NotificationSound = {
  id: string
  label: string
  file: string
}

/**
 * Lista de toques. Para incluir outro: coloque o MP3 em
 * `frontend/public/sounds/` e acrescente uma entrada aqui.
 * MP3: Pixabay Content License, juniorsoundays.
 */
export const NOTIFICATION_SOUNDS: NotificationSound[] = [
  { id: 'ui-57', label: 'UI Sound 57', file: 'juniorsoundays-ui-sound-57-527851.mp3' },
  { id: 'ui-86', label: 'UI Sound 86', file: 'juniorsoundays-ui-sound-86-527854.mp3' },
  { id: 'ui-107', label: 'UI Sound 107', file: 'juniorsoundays-ui-sound-107-532190.mp3' },
]

export const DEFAULT_NOTIFICATION_SOUND_ID = NOTIFICATION_SOUNDS[0].id

export function notificationSoundSrc(sound: NotificationSound): string {
  return `/sounds/${sound.file}`
}

export function getNotificationSound(id: string | null | undefined): NotificationSound {
  return NOTIFICATION_SOUNDS.find((item) => item.id === id) ?? NOTIFICATION_SOUNDS[0]
}
