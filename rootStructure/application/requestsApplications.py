from fastapi import APIRouter


applicationRouter = APIRouter(
    prefix='/application'
)


@applicationRouter.get('/undefined')
async def start():
    return {'start': 'ok'}