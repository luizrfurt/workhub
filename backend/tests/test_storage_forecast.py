from datetime import datetime, timedelta, timezone

from app.services.storage_forecast import compute_storage_forecast


def test_forecast_quota_reached():
    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    result = compute_storage_forecast(
        used_bytes=10,
        quota_bytes=10,
        bytes_in_window=10,
        files_in_window=5,
        oldest_created_at=now - timedelta(days=40),
        now=now,
    )
    assert result.status == "quota_reached"
    assert result.eta_at is None


def test_forecast_insufficient_without_history():
    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    result = compute_storage_forecast(
        used_bytes=0,
        quota_bytes=10 * 1024**3,
        bytes_in_window=0,
        files_in_window=0,
        oldest_created_at=None,
        now=now,
    )
    assert result.status == "insufficient_data"


def test_forecast_uses_oldest_when_newer_than_window():
    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    oldest = now - timedelta(days=10)
    used = 10 * 1024 * 1024
    result = compute_storage_forecast(
        used_bytes=used,
        quota_bytes=20 * 1024 * 1024,
        bytes_in_window=used,
        files_in_window=5,
        oldest_created_at=oldest,
        now=now,
    )
    assert result.status == "estimated"
    assert result.avg_bytes_per_day is not None
    assert result.eta_at is not None
    # 10 MB em 10 dias → 1 MB/dia; restam 10 MB → ~10 dias
    assert abs(result.avg_bytes_per_day - 1024 * 1024) < 2000
    assert abs((result.eta_at - now).total_seconds() - 10 * 86400) < 120


def test_forecast_ignores_files_older_than_window_for_rate():
    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    oldest = now - timedelta(days=90)
    result = compute_storage_forecast(
        used_bytes=100 * 1024 * 1024,
        quota_bytes=200 * 1024 * 1024,
        bytes_in_window=30 * 1024 * 1024,
        files_in_window=8,
        oldest_created_at=oldest,
        now=now,
    )
    assert result.status == "estimated"
    # 30 MB em 30 dias → 1 MB/dia; restam 100 MB → ~100 dias
    assert result.eta_at is not None
    assert 95 <= (result.eta_at - now).days <= 105
