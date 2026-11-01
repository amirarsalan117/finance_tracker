# Account --> name , type , amount , 

from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase , Mapped , MappedColumn, mapped_column , relationship

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "account"
    id : Mapped[int] = mapped_column(primary_key=True)



class catalog(Base):
    __tablename__ = 'catalog'

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]= mapped_column(String(30))
    code : Mapped[str] = mapped_column(unique=True , nullable=False)
    parent_id :Mapped[Optional[int]] = mapped_column(ForeignKey('catalog.id'))
    parent: Mapped[Optional['catalog']] = relationship(remote_side="Catalog.id")
