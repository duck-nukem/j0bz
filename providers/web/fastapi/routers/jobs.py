from fastapi import APIRouter, Request

from domain.jobs.actions import view_job
from providers.web.fastapi.templates import TemplateResponse

router = APIRouter(
    prefix="/j",
    tags=["jobs"],
)


@router.get("/{job_id}")
async def detail_job(request: Request, job_id: int):
    job = view_job(job_id)
    return TemplateResponse("job_detail.html", {'request': request, 'job': job})
