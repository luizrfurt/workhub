from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import get_logger

logger = get_logger("app.errors")


class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code


class UnauthorizedError(AppError):
    def __init__(self, message: str = "Não autenticado.") -> None:
        super().__init__(message, status_code=401)


class ForbiddenError(AppError):
    def __init__(self, message: str = "Acesso negado.") -> None:
        super().__init__(message, status_code=403)


class NotFoundError(AppError):
    def __init__(self, message: str = "Recurso não encontrado.") -> None:
        super().__init__(message, status_code=404)


class ConflictError(AppError):
    def __init__(self, message: str = "Conflito de dados.") -> None:
        super().__init__(message, status_code=409)


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    logger.warning("%s %s -> %s %s", request.method, request.url.path, exc.status_code, exc.message)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )


async def unhandled_error_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Erro não tratado em %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content={"message": "Erro interno do servidor."},
    )
