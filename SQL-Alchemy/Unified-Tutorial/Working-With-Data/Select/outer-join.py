from sqlalchemy import create_engine, MetaData, select, Table

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)
address_table = Table("address", meta, autoload_with=engine)

# Left Outer Join
# stmt = select(user_table).join(address_table, isouter=True)

# Full Outer Join
stmt = select(user_table).join(address_table, full=True)

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())