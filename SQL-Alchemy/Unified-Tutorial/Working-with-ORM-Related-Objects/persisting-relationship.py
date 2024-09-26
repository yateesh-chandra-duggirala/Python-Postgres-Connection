from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import Optional, List

URL = "postgresql+psycopg2://postgres:postgres@localhost/db"

engine = create_engine(URL)

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    addresses : Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name  = {self.name!r}, full_name = {self.full_name!r})"

class Address(Base) :
    __tablename__ = "address"

    id : Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user : Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id : {self.id!r}, email = {self.email!r}, user_id = {self.user_id!r})" 

u1 = User(name = "Hemanth", full_name = "Mahesh Hemanth")

# When we try to execute the addresses attribute from u1 object, we will get empty list
print(u1.addresses)

# Let us try to append the address to the Address of the User
a1 = Address(email = "mahemanth@gmail.com")
u1.addresses.append(a1)
print(u1.addresses)

with Session(engine) as sess : 
    # sess.add(u1)
    # sess.commit()
    print(sess.execute(select(User)).all())
    print(sess.execute(select(Address)).all())