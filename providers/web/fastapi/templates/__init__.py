from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="/opt/app/providers/web/fastapi/templates")

TemplateResponse = templates.TemplateResponse