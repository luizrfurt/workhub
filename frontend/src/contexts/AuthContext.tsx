import { useEffect, type ReactNode } from 'react'

import { useAuthStore } from '../store/auth.store'

export function AuthProvider({ children }: { children: ReactNode }) {
  const hydrate = useAuthStore((state) => state.hydrate)

  useEffect(() => {
    hydrate()
  }, [hydrate])

  return children
}

export function useAuth() {
  const user = useAuthStore((state) => state.user)
  const loading = useAuthStore((state) => state.loading)
  const login = useAuthStore((state) => state.login)
  const logout = useAuthStore((state) => state.logout)
  const applyUser = useAuthStore((state) => state.applyUser)
  return { user, loading, login, logout, applyUser }
}
