from sqlalchemy import create_engine, Table, MetaData, select, func

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)

# lower() method is used for converting a string to lower case
# stmt = select(func.lower("An UPPERCASE String"))

# upper() method is used for converting a string to upper case
# stmt = select(func.upper("A lower case string"))

#count() method is used to count the number of rows in the table
stmt = select(func.count()).select_from(user_table)

# now() method is used to return the time stamp now
stmt = select(func.localtimestamp())

with engine.connect() as conn :
    res = conn.execute(stmt)
    print(res.all())