import type { Overview, StorageUsage } from '../types'
import { formatBytes } from './format'

type StorageForecastSource = Pick<
  Overview | StorageUsage,
  'storage_avg_bytes_per_day' | 'storage_quota_eta_at' | 'storage_forecast_status'
>

export function storageForecastLabel(source: StorageForecastSource): string {
  if (source.storage_forecast_status === 'quota_reached') {
    return 'Cota atingida.'
  }
  const avgPerDay = source.storage_avg_bytes_per_day
  const etaAt = source.storage_quota_eta_at
  if (source.storage_forecast_status !== 'estimated' || avgPerDay == null || !etaAt) {
    return 'Sem tendência recente o bastante para estimar.'
  }

  const weekly = avgPerDay * 7
  const eta = new Date(etaAt)
  const days = (eta.getTime() - Date.now()) / 86_400_000
  const rate = `~${formatBytes(weekly)}/semana`

  if (days > 3650) {
    return `No ritmo atual (${rate}), a cota deve levar mais de 10 anos para encher.`
  }
  if (days < 1) {
    return `No ritmo atual (${rate}), a cota deve encher em menos de um dia.`
  }

  const month = eta.toLocaleDateString('pt-BR', { month: 'short' }).replace('.', '').trim()
  return `No ritmo atual (${rate}), a cota deve encher por volta de ${month}/${eta.getFullYear()}.`
}
