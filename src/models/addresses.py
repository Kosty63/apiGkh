from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base

"""
Address Model (Адреса)
id (Primary Key) - Уникальный идентификатор адреса.
city - Город.
street - Название улицы.
house_number - Номер дома.
apartment_number - Номер квартиры (если применимо).
postal_code - Почтовый индекс.
"""


class AddressesOrm(Base):
    __tablename__ = 'addresses'

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(50))
    street: Mapped[str] = mapped_column(String())
    house_number: Mapped[str] = mapped_column(String(10))
    apartment_number: Mapped[str] = mapped_column(String(10))
    postal_code: Mapped[str] = mapped_column(String(50))
