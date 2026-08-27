import { useEffect } from 'react'
import { Volume2 } from 'lucide-react'

import { useAuth } from '../contexts/AuthContext'
import { useNotificationSoundStore } from '../store/notificationSound.store'
import { playNotificationSound } from '../utils/alerts'
import { NOTIFICATION_SOUNDS } from '../utils/notificationSounds'
import { Button } from '@/components/ui/button'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

export function NotificationSoundPicker() {
  const { user } = useAuth()
  const soundId = useNotificationSoundStore((state) => state.soundId)
  const hydrate = useNotificationSoundStore((state) => state.hydrate)
  const select = useNotificationSoundStore((state) => state.select)

  useEffect(() => {
    if (user) {
      hydrate(user.id)
    }
  }, [hydrate, user])

  if (!user) {
    return null
  }

  return (
    <div className="grid gap-1.5">
      <span className="text-[0.72rem] text-muted-foreground">Som de notificação</span>
      <div className="flex items-center gap-1.5">
        <Select
          value={soundId}
          onValueChange={(value) => {
            select(user.id, value)
          }}
        >
          <SelectTrigger className="min-h-0 flex-1 py-2 text-[0.82rem]" size="sm">
            <SelectValue />
          </SelectTrigger>
          <SelectContent position="popper" align="start">
            {NOTIFICATION_SOUNDS.map((sound) => (
              <SelectItem key={sound.id} value={sound.id}>
                {sound.label}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
        <Button
          type="button"
          variant="ghost"
          size="icon-sm"
          aria-label="Ouvir som selecionado"
          onClick={() => playNotificationSound(soundId)}
        >
          <Volume2 />
        </Button>
      </div>
    </div>
  )
}
