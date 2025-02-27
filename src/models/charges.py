from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Charges Model (Начисления)
id (Primary Key) - Уникальный идентификатор начисления.
personal_account_id (Foreign Key) - Ссылка на лицевой счет.
charge_date - Дата начисления.
amount - Сумма начисления.
service_id (Foreign Key) - Ссылка на услугу.
volume - Объем потребления
unit - Единица измерения
"""


class ChargesOrm(Base):
    __tablename__ = 'charges'

    id: Mapped[int] = mapped_column(primary_key=True)
    personal_account_id: Mapped[int] = mapped_column(ForeignKey("personal_accounts.id"))
    charge_date: Mapped[int]
    amount: Mapped[int]
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    volume: Mapped[int]
    unit: Mapped[str]