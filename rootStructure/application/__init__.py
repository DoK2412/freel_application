from fastapi import APIRouter

from ..application.requestsApplications import applicationRouter


applicRouter = APIRouter()
applicRouter.include_router(applicationRouter)