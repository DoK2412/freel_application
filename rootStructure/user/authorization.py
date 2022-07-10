import requests
import random

from fastapi import HTTPException

from ..dataModels.operationsMadel import New_user, user
from ..user.operationsUser import checking_availability_tell, call_to_numbers

from passlib.context import CryptContext


newuser = New_user()
random_number = str(random.randrange(1000, 9999))

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def login_via_vk(token):
    """
    Функция обработки VK токена
    :param token: токен пользователя
    :return: возвращает результат выполненного образения к токену
    """
    response = requests.get('https://api.vk.com/method/users.get?access_token={0}&v=5.85'.format(token.token))
    result = response.json()
    if result.get('response'):
        newuser.first_name = result['response'][0]['first_name']
        newuser.last_name = result['response'][0]['last_name']
        newuser.password = password_context.hash(str(result['response'][0]['id']))
        return {'status': 200, 'message': 'Your VK account is successfully'
                                          ' found and connected. Enter the'
                                          ' phone number to confirm it.'}
    else:
        raise HTTPException(status_code=403, detail="VK token is not valid")


async def checking_the_phone(number, session):
    """
    Функция проверка номера и запроса вызова подтверждения
    :param number: номер телефона пользователя
    :param session: сессия подключения к базе дланных
    :return: результат работы функции
    """
    if len(number.phone) == 11 or len(number.phone) == 12:
        check_number = await checking_availability_tell(number.phone, session)
        print(check_number)
        if check_number is False:
            newuser.phone = str(number.phone)
            challenge = await call_to_numbers(number.phone, random_number)
            return challenge
    else:
        raise HTTPException(status_code=403, detail="The number does not meet"
                                                    " the standard +7, 8, 7"
                                                    " and 10 digits per line")


async def end_registration(code, session):
    """
    Функция подтверждения номера и ркончания регистрации
    :param code: секретный код полученый через звонок
    :param session: сессия подключения к базе данных
    :return: результат выполнения регистрации
    """
    if code.code == random_number:
        newuser.active = True
        newuser.code_confirm_phone = random_number
        newuser.blocked = False
        newuser.phone_confirm = True
        newuser.role_id = 1
        newuser.admin_comment = 'ок'
        newuser.phone_confirm_attempts = 1
        reg_subscriber = user.from_orm(newuser)
        session.add(reg_subscriber)
        session.commit()
        session.refresh(reg_subscriber)
        return {'status': 200, 'message': 'You have successfully registered'}
    else:
        raise HTTPException(status_code=403, detail="Confirmation keys are not correct")
