import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from providers.web.fastapi.config import APP_HOST, APP_PORT, IS_DEBUG

app = FastAPI()
templates = Jinja2Templates(directory="/opt/app/providers/web/fastapi/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(
        "providers.web.fastapi.main:app",
        host=APP_HOST,
        port=APP_PORT,
        log_level='debug' if IS_DEBUG else 'info',
        reload=IS_DEBUG,
    )
