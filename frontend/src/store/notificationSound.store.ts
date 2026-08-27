import { create } from 'zustand'

import {
  DEFAULT_NOTIFICATION_SOUND_ID,
  getNotificationSound,
} from '../utils/notificationSounds'
import { loadNotificationSoundId, saveNotificationSoundId } from '../utils/storage'

interface NotificationSoundState {
  soundId: string
  hydrate: (userId: number) => void
  select: (userId: number, soundId: string) => void
}

export const useNotificationSoundStore = create<NotificationSoundState>((set) => ({
  soundId: DEFAULT_NOTIFICATION_SOUND_ID,
  hydrate: (userId) => {
    set({ soundId: getNotificationSound(loadNotificationSoundId(userId)).id })
  },
  select: (userId, soundId) => {
    const next = getNotificationSound(soundId).id
    saveNotificationSoundId(userId, next)
    set({ soundId: next })
  },
}))
