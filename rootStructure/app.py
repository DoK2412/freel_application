from fastapi import FastAPI

from .user import userRouter
from .application import applicRouter


app = FastAPI()
app.include_router(userRouter)
app.include_router(applicRouter)
