from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, aliased
from typing import Optional, List

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

class Base(DeclarativeBase):
    pass

class User(Base):
    
    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    address : Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User( id : {self.id!r}, name : {self.name!r}, full_name : {self.full_name!r})"
    
class Address(Base):

    __tablename__ = "address"

    id : Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user : Mapped[User] = relationship(back_populates="address")

    def __repr__(self) -> str:
        return f"Address( id : {self.id!r}, email : {self.email!r}, user_id : {self.user_id!r})"

address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)

stmt = select(User).join_from(User, address_alias_1).where(address_alias_1.email == "yateesh.chandra@gmail.com")\
        .join_from(User, address_alias_2).where(address_alias_2.email == "yateesh.chandra@gmail.com")

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result.all())