import gettext
from random import randint

from babel.dates import format_date
from babel.numbers import format_currency
from fastapi.templating import Jinja2Templates
from jinja2.ext import i18n

templates = Jinja2Templates(directory="/opt/app/providers/web/fastapi/templates")
templates.env.extensions["jinja2.ext.i18n"] = i18n(templates.env)
templates.env.install_gettext_translations(gettext)

templates.env.filters['datetime'] = format_date
templates.env.filters['currency'] = format_currency

themes = [
    {'light': '#a7a6f5', 'dark': '#191320'},
    {'light': '#dad9fb', 'dark': '#064fdf'},
    {'light': '#6b8496', 'dark': '#08132c'},
    {'light': '#c1f134', 'dark': '#6711c8'},
    {'light': '#faf54e', 'dark': '#a21fe7'},
]

templates.env.globals['get_random_theme'] = lambda: themes[randint(0, len(themes) - 1)]

TemplateResponse = templates.TemplateResponse
