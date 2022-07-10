from fastapi import APIRouter, Depends
from sqlmodel import Session


from ..dataModels.operationsMadel import UserRegistration, SecretCode, Token_vk, Phone_number
from ..databaseStructure.connectionBase import get_dbsession
from .operationsUser import registration_processing, confirmation_number
from .authorization import login_via_vk, checking_the_phone, end_registration


routerUser = APIRouter(
    prefix='/user'
)


@routerUser.post('/beg_registration')
async def registration_user(users: UserRegistration, session: Session = Depends(get_dbsession)):
    """Функция начальной регистрации пользователя"""
    beg_registration = await registration_processing(users, session)
    return beg_registration


@routerUser.post('/end_registration')
async def registration_user(code: SecretCode, session: Session = Depends(get_dbsession)):
    """Функция окончания регистрации пользователя"""
    end_registration = await confirmation_number(code, session)
    return end_registration


@routerUser.post('/entrancevk')
async def entrance_vk(token: Token_vk):
    """Функция проверки токена пользователя VK"""
    result = await login_via_vk(token)
    return result


@routerUser.post('/confirmation_phone')
async def confirmation_phone(number: Phone_number, session: Session = Depends(get_dbsession)):
    """Функция запроса номера телефона пользователя"""
    result = await checking_the_phone(number, session)
    return result


@routerUser.post('/end_registration_vk')
async def end_registration_vk(code: SecretCode, session: Session = Depends(get_dbsession)):
    """Функция завершения регистрации через VK"""
    result = await end_registration(code, session)
    return result
