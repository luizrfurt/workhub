"""Compatibilidade: use app.db.session."""

from app.db.session import SessionLocal, engine, get_db

__all__ = ["SessionLocal", "engine", "get_db"]
