# Account --> name , type , amount ,
from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class TimeStampMixin:
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), Nullable=False
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
    )


class Base(DeclarativeBase):
    pass


class Ledger(TimeStampMixin, Base):
    __tablename__ = "ledger"

    id: Mapped[int] = mapped_column(primary_key=True)

    user: Mapped["User"] = relationship(back_populates="ledger")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    account: Mapped[list["Account"]] = relationship(back_populates="ledger")

    category: Mapped[list["Catalog"]] = relationship(back_populates="ledger")


class User(TimeStampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_code: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    ledger: Mapped[list["Ledger"]] = relationship(back_populates="user")


class Catalog(TimeStampMixin, Base):
    __tablename__ = "catalog"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("catalog.id"))
    parent: Mapped[Optional["Catalog"]] = relationship(
        back_populates="children", remote_side=[id]
    )
    children: Mapped[list["Catalog"]] = relationship(back_populates="parent")

    ledger_id: Mapped[int] = mapped_column(ForeignKey("ledger.id"))
    ledger: Mapped["Ledger"] = relationship(back_populates="catalog")


class Account(TimeStampMixin, Base):
    __tablename__ = "account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    deposit: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)

    type_of_id: Mapped[int] = mapped_column(ForeignKey("catalog.id"))
    type_of: Mapped["Catalog"] = relationship(foreign_keys=[type_of_id])

    currency_id: Mapped[int] = mapped_column(ForeignKey("catalog.id"))
    currency: Mapped["Catalog"] = relationship(foreign_keys=[currency_id])

    ledger: Mapped["Ledger"] = relationship(back_populates="account")
    ledger_id: Mapped[int] = mapped_column(ForeignKey("ledger.id"))
    transaction: Mapped[list["Transaction"]] = relationship(back_populates="account")


class Transaction(TimeStampMixin, Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(60))
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=0)

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"))
    account: Mapped["Account"] = relationship(back_populates="transaction")
