from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from src.database import Base

"""
Meters Model (Счетчики)
id (Primary Key) - Уникальный идентификатор счетчика.
personal_account_id (Foreign Key) - Ссылка на лицевой счет.
meter_type - Тип счетчика (например, тепловой, водяной и т.д.).
installation_date - Дата установки счетчика.
last_check_date - Дата последней проверки.
"""


class MetersOrm(Base):
    __tablename__ = 'meters'

    id: Mapped[int] = mapped_column(primary_key=True)
    personal_account_id: Mapped[int] = mapped_column(ForeignKey("personal_accounts.id"))
    meter_type: Mapped[str]
    installation_date: Mapped[str]
    last_check_date: Mapped[str]