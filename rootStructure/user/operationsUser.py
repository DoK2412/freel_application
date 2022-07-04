import random

from ..dataModels.operationsMadel import user
from fastapi import HTTPException
from pyucallerapi import APIUCaller
from passlib.context import CryptContext
from sqlmodel import select


from ..settings import setting


api_Caller = APIUCaller(
    service_id=setting.service_id_ucaller,
    key=setting.sikret_key_ucaller
)

call_respones = api_Caller.init_call(
    phone='+79000000001',
    code=str(random.randrange(1000, 9999))
)

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def registration_processing(users, session):
    """
    Функция предназначена для проверки регистрации пользователя
    :param users:
    :return:
    """
    contact = session.exec(select(user).filter(user.phone == users.phone)).all()
    if contact:
        raise HTTPException(status_code=403, detail="The user is in the database")
    else:
        if users.confirmations_password == users.password:
            users.password = password_context.hash(users.password)
            if len(users.phone) == 11 or len(users.phone) == 12:
                call_respones['phone'] = str(users.phone)
                print(call_respones['phone'])
                print(call_respones['code'])
                # if call_respones.get('status', False):
                #     call_respones.get("ucaller_id")
                # else:
                #     raise HTTPException(status_code=403, detail=(call_respones.get("code"),
                #                                                  api_Caller.check_error_code(
                #                                                      call_respones.get("code"))))
            else:
                raise HTTPException(status_code=403, detail="The number does not meet the standard")
        else:
            raise HTTPException(status_code=403, detail="Passwords don't match")


async def confirmation_number(code):
    """
    Функция предназначена для окончания регистрации и подтвержения номера
    :param code:
    :return:
    """
    if code.code == call_respones['code']:
        print('номер подтвержден')






