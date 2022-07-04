from fastapi import APIRouter, Depends
from sqlmodel import Session, select


from ..dataModels.operationsMadel import UserRegistration, SecretCode
from ..databaseStructure.connectionBase import get_dbsession
from .operationsUser import registration_processing, confirmation_number


routerUser = APIRouter(
    prefix='/user'
)


@routerUser.post('/begregistration')
async def registration_user(users: UserRegistration, session: Session = Depends(get_dbsession)):
    beg_registration = await registration_processing(users, session)
    return beg_registration

@routerUser.post('/endregistration')
async def registration_user(code: SecretCode):
    end_registration = await confirmation_number(code)
    return end_registration
