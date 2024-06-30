from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True
)

session_f = sessionmaker(sync_engine)


class Base(DeclarativeBase):

   pass