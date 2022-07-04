import datetime


from datetime import date
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from typing import List, Optional


class UserRegistration(BaseModel):
    first_name: str
    last_name: str
    phone: str
    password: str
    confirmations_password: str


class SecretCode(BaseModel):
    code: str


class user(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name: str
    phone: str
    password: str
    salt: int
    role_id: int
    active: bool
    admin_comment: str
    code_confirm_phone: int
    blocked: bool
    phone_confirm: bool
    phone_confirm_attempts: int
    dt_created: Optional[datetime.date] = date.today()
    dt_updated: Optional[datetime.date] = date.today()
    dt_deleted: Optional[datetime.date]
