import gettext

from babel.dates import format_date
from babel.numbers import format_currency
from fastapi.templating import Jinja2Templates
from jinja2.ext import i18n

templates = Jinja2Templates(directory="/opt/app/providers/web/fastapi/templates")
templates.env.extensions["jinja2.ext.i18n"] = i18n(templates.env)
templates.env.install_gettext_translations(gettext)

templates.env.filters['datetime'] = format_date
templates.env.filters['currency'] = format_currency

TemplateResponse = templates.TemplateResponse
