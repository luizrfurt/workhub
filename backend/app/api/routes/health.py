from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.exceptions import AppError
from app.db.session import get_db

router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/db", summary="Health do banco")
def health_db(db: Session = Depends(get_db)) -> dict[str, str]:
    try:
        db.execute(text("SELECT 1"))
    except Exception:
        raise AppError("Banco de dados indisponível.", status_code=503)
    return {"status": "ok"}
