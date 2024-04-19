from sqlalchemy import create_engine, MetaData, String, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import Optional, List

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")
meta_data = MetaData()

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    address : Mapped[List["Address"]] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"User( Id : {self.id!r}, Name : {self.name!r}, full_name : {self.full_name!r})"

class Address(Base):
    __tablename__ = "address"

    id : Mapped[int] = mapped_column(primary_key= True)
    email : Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user : Mapped[User] = relationship(back_populates="address")

    def __repr__(self) -> str:
        return f"Address( Id : {self.id!r}, Email : {self.email!r}, User_Id : {self.user_id!r})"

with Session(engine) as sess:
    res = sess.execute(
        select(User.name, Address.email).where(User.id == Address.user_id).order_by(Address.email)
    )
    print(res.all())