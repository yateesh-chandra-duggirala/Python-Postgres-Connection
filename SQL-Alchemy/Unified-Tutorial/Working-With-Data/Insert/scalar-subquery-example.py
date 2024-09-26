from sqlalchemy import create_engine, MetaData, Table, select, bindparam, insert

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo= True)

metadata_obj = MetaData()

user_table = Table("user_account", metadata_obj, autoload_with=engine)
address_table = Table("address", metadata_obj, autoload_with=engine)

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

with engine.connect() as conn :
    result = conn.execute(
        insert(address_table).values(user_id = scalar_subq),
        [
            {
                "username" : "Yateesh",
                "email" : "yateesh.chandra@gmail.com"
            },
            {
                "username" : "Priya",
                "email" : "priya.yanapu@gmail.com"
            },
        ],
    )
    conn.commit()