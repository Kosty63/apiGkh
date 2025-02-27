from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Personal Account Model (Лицевые счета)
id (Primary Key) - Уникальный идентификатор лицевого счета.
user_id (Foreign Key) - Ссылка на зарегистрированного пользователя.
owner_id (Foreign Key) - Ссылка на владельца квартиры.
address_id (Foreign Key) - Ссылка на адрес дома и квартиры.
balance - Текущий баланс счета.
debt - Сумма долга.
"""


class PersonalAccountOrm(Base):
    __tablename__ = 'personal_account'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    owner_id: Mapped[int] = mapped_column(ForeignKey("owner.id"))
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
    balance: Mapped[int]
    debt: Mapped[int]
