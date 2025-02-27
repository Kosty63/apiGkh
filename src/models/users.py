from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base

"""
User model (Пользователи)
id (Primary Key) - Уникальный идентификатор услуги.
phone_number - Номер телефона
email - адрес электронной почты
"""


class UsersOrm(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_number: Mapped[str] = mapped_column(String(15))
    email: Mapped[str]
