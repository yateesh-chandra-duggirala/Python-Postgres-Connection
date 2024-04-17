from sqlalchemy import create_engine, MetaData, Table, insert

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo = True)

metadata_object = MetaData()

user_table = Table("user_account", metadata_object, autoload_with = engine)

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name" : "Mohan", "full_name" : "Mohan Sharma"},
            {"name" : "Priya", "full_name" : "Priyanvita"},
        ],
    )
    conn.commit()