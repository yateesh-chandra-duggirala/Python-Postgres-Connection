from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta_data = MetaData()

user_table = Table("user_account", meta_data, autoload_with= engine)

select_stmt = select(user_table)

with engine.connect() as conn:
    result = conn.execute(select_stmt)
    print(result.all())