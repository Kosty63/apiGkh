from sqlalchemy.orm import Mapped, mapped_column


from src.database import Base


"""
Services Model (Услуги)
id (Primary Key) - Уникальный идентификатор услуги.
service_name - Название услуги.
description - Описание услуги.
tariff - Тариф за единицу услуги.
unit - Единица измерения (например, "м³", "Гкал")
"""

class ServicesOrm(Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True)
    service_name: Mapped[str]
    description: Mapped[str]
    tariff: Mapped[int]
    unit: Mapped[str]