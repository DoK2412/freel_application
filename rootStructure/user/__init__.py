from fastapi import APIRouter
from ..user.requestsUser import routerUser

userRouter = APIRouter()
userRouter.include_router(routerUser)
