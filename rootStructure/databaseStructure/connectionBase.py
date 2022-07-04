from ..settings import setting
from sqlmodel import Session, create_engine


engin = create_engine(
    setting.database_url
)


async def get_dbsession():
    with Session(engin) as session:
        return session
