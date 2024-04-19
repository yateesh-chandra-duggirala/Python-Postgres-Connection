from sqlalchemy import select, create_engine, Table, MetaData

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

metadata_obj = MetaData()

user_table = Table("user_account", metadata_obj, autoload_with=engine)

# we can declare column names individually.
# select_stmt = select(user_table.c.name, user_table.c.full_name)

# There is another way where we can pass the column names in the form of list as follows :
select_stmt = select(user_table.c["id", "full_name"])

with engine.connect() as conn:
    res = conn.execute(select_stmt)
    print(res.all())