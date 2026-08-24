from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Literal

ForecastStatus = Literal["estimated", "insufficient_data", "quota_reached"]

WINDOW_DAYS = 30
MIN_FILES = 3
MIN_SAMPLE_DAYS = 7


@dataclass(frozen=True)
class StorageForecast:
    status: ForecastStatus
    avg_bytes_per_day: int | None
    eta_at: datetime | None


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def compute_storage_forecast(
    *,
    used_bytes: int,
    quota_bytes: int,
    bytes_in_window: int,
    files_in_window: int,
    oldest_created_at: datetime | None,
    now: datetime | None = None,
    window_days: int = WINDOW_DAYS,
    min_files: int = MIN_FILES,
    min_sample_days: float = MIN_SAMPLE_DAYS,
) -> StorageForecast:
    """Estima quando a cota enche com a média da janela recente (ou desde o anexo mais antigo)."""
    moment = _as_utc(now or datetime.now(timezone.utc))
    if quota_bytes > 0 and used_bytes >= quota_bytes:
        return StorageForecast(status="quota_reached", avg_bytes_per_day=None, eta_at=None)

    if oldest_created_at is None or files_in_window < min_files:
        return StorageForecast(status="insufficient_data", avg_bytes_per_day=None, eta_at=None)

    window_start = moment - timedelta(days=window_days)
    sample_start = max(_as_utc(oldest_created_at), window_start)
    sample_days = (moment - sample_start).total_seconds() / 86400
    if sample_days < min_sample_days:
        return StorageForecast(status="insufficient_data", avg_bytes_per_day=None, eta_at=None)

    avg = bytes_in_window / sample_days
    if avg < 1:
        return StorageForecast(status="insufficient_data", avg_bytes_per_day=None, eta_at=None)

    remaining = max(quota_bytes - used_bytes, 0)
    eta = moment + timedelta(days=remaining / avg)
    return StorageForecast(
        status="estimated",
        avg_bytes_per_day=int(round(avg)),
        eta_at=eta,
    )
