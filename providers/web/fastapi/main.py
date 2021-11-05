import locale

import uvicorn
from fastapi import FastAPI, Request
from fastapi_contrib.auth.backends import AuthBackend
from fastapi_contrib.auth.middlewares import AuthenticationMiddleware

from domain.jobs.actions import list_jobs
from providers.web.fastapi.config import APP_HOST, APP_PORT, IS_DEBUG
from providers.web.fastapi.routers import jobs, users
from providers.web.fastapi.templates import TemplateResponse
from providers.web.middleware_functions import infer_user_language_from_header

app = FastAPI()


@app.on_event('startup')
async def startup():
    locale.setlocale(locale.LC_ALL)
    app.add_middleware(AuthenticationMiddleware, backend=AuthBackend())


@app.middleware("http")
async def set_locale(request: Request, call_next):
    language_header = request.headers.get('accept-language')
    request.state.language = infer_user_language_from_header(language_header)
    return await call_next(request)


@app.get("/")
def read_root(request: Request):
    return TemplateResponse("job_list.html", {"request": request, 'jobs': list_jobs()})


app.include_router(jobs.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(
        "providers.web.fastapi.main:app",
        host=APP_HOST,
        port=APP_PORT,
        log_level='debug' if IS_DEBUG else 'info',
        reload=IS_DEBUG,
    )
