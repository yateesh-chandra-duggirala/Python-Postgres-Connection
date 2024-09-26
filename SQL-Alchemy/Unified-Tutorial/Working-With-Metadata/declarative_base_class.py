from sqlalchemy.orm import DeclarativeBase

# The Declarative Base refers to a Metadata collection thay is created for us automatically
# Assuming that we did not provide one from the outside.
# This Metadata collection is accessible via the DeclarativeBase.metadata class-level attribute
class Base(DeclarativeBase):
    pass

# As we create new mapped classes, they will reference a Table within this Metadata Collection.
print(Base.metadata)

print(Base.registry)