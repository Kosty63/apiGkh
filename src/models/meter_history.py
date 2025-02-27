from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Meter History Model (История показаний)
id (Primary Key) - Уникальный идентификатор показания.
meter_id (Foreign Key) - Ссылка на счетчик.
reading_date - Дата показания.
value - Значение показания.
"""


class MeterHistoryOrm(Base):
    __tablename__ = 'meter_history'

    id: Mapped[int] = mapped_column(primary_key=True)
    meter_id: Mapped[int] = mapped_column(ForeignKey('meter.id'))
    reading_date: Mapped[int]
    value: Mapped[int]
