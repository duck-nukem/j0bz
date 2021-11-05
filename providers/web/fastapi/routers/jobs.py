from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from domain.jobs.actions import view_job
from providers.web.fastapi.templates import TemplateResponse

router = APIRouter(
    prefix="/j",
    tags=["jobs"],
)


@router.get("/{job_id}", response_class=HTMLResponse)
async def detail_job(request: Request, job_id: int):
    return TemplateResponse("job_detail.html", {'request': request, 'job': view_job(job_id)})
