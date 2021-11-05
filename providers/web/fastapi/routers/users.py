from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from domain.users.actions import view_user
from providers.web.fastapi.templates import TemplateResponse

router = APIRouter(
    prefix="/u",
    tags=["users"],
)


@router.get("/{user_id}", response_class=HTMLResponse)
async def detail_user(request: Request, user_id: int):
    return TemplateResponse("user_detail.html", {'request': request, 'user': view_user(user_id)})
