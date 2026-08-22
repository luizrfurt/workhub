import { create } from 'zustand'

import { fetchMe, login as loginRequest, logout as logoutRequest } from '../services/auth'
import type { User } from '../types'
import { clearSession, getAccessToken, getRefreshToken, getStoredUser, setSession } from '../utils/storage'

interface AuthState {
  user: User | null
  loading: boolean
  login: (username: string, password: string) => Promise<User>
  logout: () => Promise<void>
  applyUser: (user: User) => void
  hydrate: () => void
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  loading: true,
  login: async (username: string, password: string) => {
    const data = await loginRequest(username, password)
    setSession(data.access_token, data.refresh_token, JSON.stringify(data.user))
    set({ user: data.user })
    return data.user
  },
  logout: async () => {
    const refresh = getRefreshToken()
    try {
      await logoutRequest(refresh)
    } catch {
      // session is cleared locally regardless of API result
    }
    clearSession()
    set({ user: null })
  },
  applyUser: (next: User) => {
    set({ user: next })
    const access = getAccessToken()
    const refresh = getRefreshToken()
    if (access && refresh) {
      setSession(access, refresh, JSON.stringify(next))
    }
  },
  hydrate: () => {
    const token = getAccessToken()
    const stored = getStoredUser()
    if (stored) {
      set({ user: JSON.parse(stored) as User })
    }
    if (!token) {
      set({ loading: false })
      return
    }
    fetchMe()
      .then((current) => {
        set({ user: current })
        const refresh = getRefreshToken()
        if (refresh && token) {
          setSession(token, refresh, JSON.stringify(current))
        }
      })
      .catch(() => {
        clearSession()
        set({ user: null })
      })
      .finally(() => set({ loading: false }))
  },
}))
