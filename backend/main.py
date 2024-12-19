import uvicorn
from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from backend.config import settings
from backend.api.dependencies import azure_scheme
from backend.api.api import api_router_hello, api_router_get_members, api_router_get_organization


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Load OpenID config on startup.
    """
    await azure_scheme.openid_config.load_config()
    yield


app = FastAPI(
    swagger_ui_oauth2_redirect_url="/oauth2-redirect",
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True,
        "clientId": settings.OPENAPI_CLIENT_ID,
        "scopes": settings.SCOPE_NAME,
    },
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(
    api_router_hello,
    prefix=settings.API_V1_STR,
    dependencies=[Security(azure_scheme, scopes=["user_impersonation"])],
)

app.include_router(
    api_router_get_organization,
    prefix=settings.API_V1_STR,
    dependencies=[Security(azure_scheme, scopes=["user_impersonation"])],
)

app.include_router(
    api_router_get_members,
    prefix=settings.API_V1_STR,
    dependencies=[Security(azure_scheme, scopes=["user_impersonation"])],
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
