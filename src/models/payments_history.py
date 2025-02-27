from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Payments History Model (История платежей)
id (Primary Key) - Уникальный идентификатор платежа.
personal_account_id (Foreign Key) - Ссылка на лицевой счет.
payment_date - Дата платежа.
amount - Сумма платежа.
payment_method - Способ оплаты (например, наличные, карта, онлайн).
"""


class PaymentsHistoryOrm(Base):
    __tablename__ = 'payments_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    personal_account_id: Mapped[int] = mapped_column(ForeignKey("personal_accounts.id"))
    payment_date: Mapped[str]
    amount: Mapped[str]
    payment_method: Mapped[str]
