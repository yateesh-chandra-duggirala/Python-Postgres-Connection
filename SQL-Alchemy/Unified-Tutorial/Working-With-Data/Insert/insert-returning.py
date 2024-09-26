from sqlalchemy import MetaData, create_engine, Table, insert

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

metadata_obj = MetaData()

user_table = Table("user_account", metadata_obj, autoload_with=engine)

stmt = insert(user_table).values(name = "Praveen", full_name = "Praveen Kruthiventi")\
        .returning(user_table.c.id, user_table.c.name)

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result)
    print(result.fetchone())
    conn.commit()