"""
Application FastAPI
"""

import json
import os
from fastapi import FastAPI  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore
from app.router.health import health  # type: ignore
from app.router.route import route  # type: ignore
from dotenv import load_dotenv  # type: ignore

# ═══════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

load_dotenv()

ALLOWED_ORIGINS = json.loads(os.getenv("ALLOWED_ORIGINS", "[]"))

APP_CONFIG = {
    "title":       os.getenv("APP_CONFIG_TITLE"),
    "description": os.getenv("APP_CONFIG_DESCRITPION"),
    "version":     os.getenv("APP_CONFIG_VERSION"),
    "docs_url":    "/docs",
    "openapi_url": "/openapi.json",
}

CORS_CONFIG = {
    "allow_origins":     ALLOWED_ORIGINS,
    "allow_credentials": True,
    "allow_methods":     json.loads(os.getenv("CORS_ALLOW_METHODS", '["GET","POST"]')),
    "allow_headers":     ["*"],
}

ROUTER_CONFIG = [
    {"router": route, "prefix": "/api", "tags": ["Exemple Api"]},
    {"router": health,    "prefix": "/api", "tags": ["Health Check"]},
]


def create_app() -> FastAPI:
    app = FastAPI(**APP_CONFIG)
    _setup_middleware(app)
    _setup_routers(app)
    _setup_root_routes(app)
    return app


def _setup_middleware(app: FastAPI) -> None:
    app.add_middleware(CORSMiddleware, **CORS_CONFIG)


def _setup_routers(app: FastAPI) -> None:
    for config in ROUTER_CONFIG:
        app.include_router(
            config["router"], prefix=config["prefix"], tags=config["tags"]
        )


def _setup_root_routes(app: FastAPI) -> None:
    @app.get("/", tags=["Root"])
    async def root():
        return {
            "message": APP_CONFIG["title"],
            "version": APP_CONFIG["version"],
            "status":  "Operationnel",
        }


app = create_app()
