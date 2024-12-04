from sqlalchemy import create_engine,MetaData, Table, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta_data = MetaData()

user_table = Table("user_account", meta_data, autoload_with=engine)

# Normal Condition Statement
# stmt = select(user_table).where(user_table.c.name == "Yateesh")

# AND Statement
# Method 1
# stmt = select(user_table).where(user_table.c.name == "Yateesh", user_table.c.id == 1)

# Method 2
stmt = select(user_table).where(user_table.c.name == "Yateesh").where(user_table.c.id == 1)

print(stmt)

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result.all())