from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

"""
Owners model (Владельц)
id (Primary Key) - Уникальный идентификатор владельца.
first_name - Имя владельца.
last_name - Фамилия владельца.
"""


class OwnersOrm(Base):
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
