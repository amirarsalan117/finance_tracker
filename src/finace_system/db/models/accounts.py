# Account --> name , type , amount ,
from decimal import Decimal
from typing import Optional

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_code: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)


class Catalog(Base):
    __tablename__ = "catalog"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("catalog.id"))
    parent: Mapped[Optional["Catalog"]] = relationship(remote_side="Catalog.id")


class Account(Base):
    __tablename__ = "account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    deposit: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)

    type_of_id: Mapped[int] = mapped_column(ForeignKey("catalog.id"))
    type_of: Mapped["Catalog"] = relationship(foreign_keys=[type_of_id])

    currency_id: Mapped[int] = mapped_column(ForeignKey("catalog.id"))
    currency: Mapped["Catalog"] = relationship(foreign_keys=[currency_id])
