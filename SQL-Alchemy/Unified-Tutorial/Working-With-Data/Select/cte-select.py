from sqlalchemy import create_engine, Table, MetaData, select, func

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)
address_table = Table("address", meta, autoload_with=engine)

subq = (select(func.count(address_table.c.id).label("count"), address_table.c.user_id).group_by(address_table.c.user_id).cte())

stmt = select(user_table.c.name, user_table.c.full_name, subq.c.count).join_from(user_table, subq)
print(stmt)