from fastapi import FastAPI
from starlette.responses import RedirectResponse

from taskana_api.config import settings
from taskana_api.routes.api import v1_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    debug=settings.DEBUG
)
app.include_router(v1_router, prefix=settings.API_V1_STR)


@app.get('/')
async def redirect_to_docs():
    return RedirectResponse('/docs')
