from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Payments History Model (История платежей)
id (Primary Key) - Уникальный идентификатор платежа.
account_id (Foreign Key) - Ссылка на лицевой счет.
payment_date - Дата платежа.
amount - Сумма платежа.
payment_method - Способ оплаты (например, наличные, карта, онлайн).
"""


class PaymentsHistoryOrm(Base):
    __tablename__ = 'payments'

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[str] = mapped_column(ForeignKey('accounts.id'))
    payment_date: Mapped[str]
    amount: Mapped[str]
    payment_method: Mapped[str]
