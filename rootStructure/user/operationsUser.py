import random

from ..dataModels.operationsMadel import user, New_user
from fastapi import HTTPException
from pyucallerapi import APIUCaller
from passlib.context import CryptContext
from sqlmodel import select


from ..settings import setting


api_Caller = APIUCaller(
    service_id=setting.service_id_ucaller,
    key=setting.sikret_key_ucaller
)

random_number = str(random.randrange(1000, 9999))
newuser = New_user()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def checking_availability_tell(phone, session):
    """
    Функция предназначена для проверки номера телефона в базе данных
    :param users: данные о пользователе
    :param session: данные подключения к базе данных
    :return: возврат результата наличия номера
    """
    for num in ['+7', '7', '8']:
        if len(phone) == 12:
            number = num + phone[2:]
            contact = session.exec(select(user).filter(user.phone == number)).all()
            if contact:
                return True
        elif len(phone) == 11:
            number = num + phone[1:]
            contact = session.exec(select(user).filter(user.phone == number)).all()
            if contact:
                return True
    else:
        return False


async def call_to_numbers(phone, random_number):
    """
    Функция предназначена для создания вызова звонка
    подтверждения номера
    :param phone: номер пользователя
    :return: результат выполнения функции
    """
    call_respones = api_Caller.init_call(
        phone=str(phone),
        code=random_number
    )
    if call_respones.get('status', False):
        return {'status': 200, 'message': 'You will receive a call to your'
                                          ' phone number, enter the'
                                          ' last 4 digits'}
    else:
        raise HTTPException(status_code=403, detail=(call_respones.get("code"),
                                                     api_Caller.check_error_code(
                                                         call_respones.get("code"))))


async def registration_processing(users, session):
    """
    Функция предназначена для проверки регистрации пользователя
    через номер телефона
    :param users: данные о пользователе полученные для работы
    :return: результат выполнения функции
    """
    contact = await checking_availability_tell(users.phone, session)
    if contact:
        raise HTTPException(status_code=403, detail="The user is in the database")
    else:
        if users.confirmations_password == users.password:

            newuser.password = password_context.hash(users.password)
            newuser.first_name = users.first_name
            newuser.last_name = users.last_name
            if len(users.phone) == 11 or len(users.phone) == 12:
                newuser.phone = users.phone
                await call_to_numbers(users.phone, random_number)
            else:
                raise HTTPException(status_code=403, detail="The number does not meet the standard")
        else:
            raise HTTPException(status_code=403, detail="Passwords don't match")


async def confirmation_number(code, session):
    """
    Функция предназначена для окончания регистрации и подтвержения номера
    :param code: секретный код полученый через звонок
    :return: результат окончания регистарации пользователя
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
        raise HTTPException(status_code=403, detail="The verification code is not correct")

