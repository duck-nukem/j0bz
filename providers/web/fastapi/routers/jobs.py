from fastapi import APIRouter, Request

from domain.jobs.repositories import JobRepository
from providers.web.fastapi.templates import TemplateResponse

router = APIRouter()


@router.get("/j/{job_id}", tags=["jobs"])
async def view_job(request: Request, job_id: int):
    job = JobRepository().get(job_id)
    return TemplateResponse("job_detail.html", {'request': request, 'job': job})
