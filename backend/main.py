from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

from app.api.router import api_router
from app.core.config import get_settings
from app.core.exceptions import AppError, app_error_handler, unhandled_error_handler
from app.core.logger import configure_logging
from app.core.middleware import RequestLoggingMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

settings = get_settings()
configure_logging()

app = FastAPI(
    title="WorkHub",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def validation_error_handler(_request: Request, _exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": "Dados inválidos."})


app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)
app.add_exception_handler(Exception, unhandled_error_handler)
# Caddy de produção já prefixa /api; as rotas da app ficam na raiz (/auth, /projects, /ws).
app.include_router(api_router)
