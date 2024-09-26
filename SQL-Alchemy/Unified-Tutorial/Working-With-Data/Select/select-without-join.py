from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)
address_table = Table("address", meta, autoload_with=engine)

# This is casual Join
# stmt = select(user_table.c.name, address_table.c.email).join_from(user_table, address_table)

# This is used for the Right join
stmt = select(user_table.c.name, address_table.c.email).join(user_table)

with engine.connect() as conn :
    res = conn.execute(stmt)
    print(res.all())

print(stmt)