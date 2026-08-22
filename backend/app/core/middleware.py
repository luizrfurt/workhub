"""Middleware de logging HTTP."""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.core.logger import get_logger

logger = get_logger("app.http")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        logger.info("%s %s %s", request.method, request.url.path, response.status_code)
        return response
