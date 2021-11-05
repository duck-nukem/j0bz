from fastapi import APIRouter, Request

from domain.jobs.repositories import JobRepository
from domain.users.actions import view_user
from providers.web.fastapi.templates import TemplateResponse

router = APIRouter(
    prefix="/p",
    tags=["users"],
)


@router.get("/{user_id}")
async def detail_user(request: Request, user_id: int):
    user = view_user(user_id)
    return TemplateResponse("user_detail.html", {'request': request, 'user': user})
