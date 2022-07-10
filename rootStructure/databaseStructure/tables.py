import sqlalchemy as sa
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# таблица данных для записной книги
class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.VARCHAR, nullable=True)
    last_name = sa.Column(sa.VARCHAR, nullable=True)
    phone = sa.Column(sa.BigInteger, nullable=True)
    password = sa.Column(sa.VARCHAR, nullable=True)
    role_id = sa.Column(sa.Integer, sa.ForeignKey("user_role.id"))
    active = sa.Column(sa.Boolean, default=False)
    admin_comment = sa.Column(sa.TEXT)
    code_confirm_phone = sa.Column(sa.Integer)
    blocked = sa.Column(sa.Boolean, default=False)
    phone_confirm = sa.Column(sa.Boolean, default=False)
    phone_confirm_attempts = sa.Column(sa.Integer)
    dt_created = sa.Column(sa.Date, default=datetime.utcnow(), nullable=False)
    dt_updated = sa.Column(sa.Date, default=datetime.utcnow(), nullable=False)
    dt_deleted = sa.Column(sa.Date, default=None)


class User_role(Base):
    __tablename__ = 'user_role'
    id = sa.Column(sa.Integer, primary_key=True)
    role_name = sa.Column(sa.VARCHAR)
    permission = sa.Column(sa.VARCHAR)


class User_bonus(Base):
    __tablename__ = 'user_bonus'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    balance = sa.Column(sa.Float, default=0.0)
    bonus_percent = sa.Column(sa.Integer, default=1)
    active = sa.Column(sa.Boolean, default=True)
    dt_created = sa.Column(sa.Date, default=datetime.utcnow(), nullable=False)
    dt_update = sa.Column(sa.Date, default=datetime.utcnow(), nullable=False)


class Calendar(Base):
    __tablename__ = 'calendar'
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Integer)
    month = sa.Column(sa.Integer)
    year = sa.Column(sa.Integer)
    day_of_the_week = sa.Column(sa.VARCHAR)
    weekend = sa.Column(sa.Boolean, default=False)


class Calendar_vacant_time(Base):
    __tablename__ = 'calendar_vacant_time'
    id = sa.Column(sa.Integer, primary_key=True)
    date_id = sa.Column(sa.Integer, sa.ForeignKey("calendar.id"))
    vacant_time_start = sa.Column(sa.VARCHAR(5))
    vacant_time_end = sa.Column(sa.VARCHAR(5))
    free = sa.Column(sa.Boolean, default=True)


class Services_category(Base):
    __tablename__ = 'services_category'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.VARCHAR)
    item = sa.Column(sa.Integer)


class Services(Base):
    __tablename__ = 'services'
    id = sa.Column(sa.Integer, primary_key=True)
    category_id = sa.Column(sa.Integer, sa.ForeignKey("calendar.id"), nullable=True)
    name = sa.Column(sa.VARCHAR)
    cost = sa.Column(sa.JSON)
    color = sa.Column(sa.VARCHAR)


class Records(Base):
    __tablename__ = 'records'
    id = sa.Column(sa.Integer, primary_key=True)
    vacant_time_id = sa.Column(sa.Integer, sa.ForeignKey("calendar_vacant_time.id"))
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    services_id = sa.Column(sa.Integer, sa.ForeignKey("services.id"))
    total_cost = sa.Column(sa.Integer)


class Settings(Base):
    __tablename__ = 'settings'
    id = sa.Column(sa.Integer, primary_key=True)
    time_interval = sa.Column(sa.Integer)
    time_start = sa.Column(sa.Integer)
    time_last_vacant = sa.Column(sa.Boolean)
    bonus_percent_start = sa.Column(sa.Integer)
















