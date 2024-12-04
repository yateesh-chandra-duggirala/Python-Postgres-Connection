from sqlalchemy import create_engine, MetaData, Table,delete, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta_data = MetaData()

user_table = Table("user_account", meta_data, autoload_with=engine)

with engine.connect() as conn :
    conn.execute(delete(user_table).where(user_table.c.id == 3))
    conn.commit()
    result = conn.execute(select(user_table))
    print(result.all())