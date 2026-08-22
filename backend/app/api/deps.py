"""Compatibilidade: use app.api.dependencies."""

from app.api.dependencies import (
    get_auth_service,
    get_current_admin,
    get_current_user,
    get_optional_refresh_token,
)

__all__ = [
    "get_auth_service",
    "get_current_admin",
    "get_current_user",
    "get_optional_refresh_token",
]
