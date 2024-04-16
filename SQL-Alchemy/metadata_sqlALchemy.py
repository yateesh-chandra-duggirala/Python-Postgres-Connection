from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine

# Create Engine Variable
engine = create_engine("postgresql+psycopg2://postgres:postgres@Localhost/db", echo= True)


# Creating Object for MetaData Class
metadata_object = MetaData()

# Create a variable named user_table
user_table = Table(
    "user_account",
    metadata_object,
    Column("id", Integer, primary_key= True),
    Column("name", String(30)),
    Column("fullname", String),
)

# Returns the Table_name.column Format
# print(user_table.c.name)

# Return the Table_name Columns using .keys() method.
# print(user_table.c.keys())

# Return the primary key
# print(user_table.primary_key)

# Creating another table address
address = Table(
    "address",
    metadata_object,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable = False),
    Column("email", String, nullable=False)
)

metadata_object.create_all(engine)