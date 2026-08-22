import { create } from 'zustand'

type LoaderState = {
  isLoading: boolean
  pending: number
  start: () => void
  stop: () => void
}

export const useLoaderStore = create<LoaderState>((set, get) => ({
  isLoading: false,
  pending: 0,
  start: () => {
    const pending = get().pending + 1
    set({ pending, isLoading: true })
  },
  stop: () => {
    const pending = Math.max(0, get().pending - 1)
    set({ pending, isLoading: pending > 0 })
  },
}))
