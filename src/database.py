from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from src.config import settings

engine = create_engine(settings.DB_URL)

async_session = sessionmaker(engine, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
