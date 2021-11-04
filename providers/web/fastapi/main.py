import uvicorn
from fastapi import FastAPI, Request

from domain.jobs.repositories import JobRepository
from providers.web.fastapi.config import APP_HOST, APP_PORT, IS_DEBUG
from providers.web.fastapi.routers import jobs
from providers.web.fastapi.templates import TemplateResponse

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    jobs = JobRepository().list()
    print(jobs)
    return TemplateResponse("index.html", {"request": request, 'jobs': jobs})


app.include_router(jobs.router)

if __name__ == "__main__":
    uvicorn.run(
        "providers.web.fastapi.main:app",
        host=APP_HOST,
        port=APP_PORT,
        log_level='debug' if IS_DEBUG else 'info',
        reload=IS_DEBUG,
    )
