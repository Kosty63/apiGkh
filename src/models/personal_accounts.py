from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Personal Account Model (Лицевые счета)
id (Primary Key) - Уникальный идентификатор лицевого счета.
user_id (Foreign Key) - Ссылка на зарегистрированного пользователя.
owner_id (Foreign Key) - Ссылка на владельца квартиры.
addresses_id (Foreign Key) - Ссылка на адрес дома и квартиры.
balance - Текущий баланс счета.
debt - Сумма долга.
"""


class PersonalAccountsOrm(Base):
    __tablename__ = 'personal_accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner_id: Mapped[int] = mapped_column(ForeignKey("owners.id"))
    addresses_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    balance: Mapped[int]
    debt: Mapped[int]
