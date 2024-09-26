from sqlalchemy import insert, create_engine, MetaData, Table

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

# Create an object for the Metadata Class
metadata_obj = MetaData()

# Declare a table object fro the Table class
user_table = Table("user_account", metadata_obj, autoload_with=engine)

# Declare a variable for the insertion statement
stmt = insert(user_table).values(name = "Sandeep", full_name = "Sandeep Sahu")
# print(stmt)

# The stringified form is created by producing a Compiled form of the object which includes DB-specific SQL
# compiler = stmt.compile()

# params is used to retrieve the parameters that are available in the compiler
# print(compiler.params)

# Executing the statement
with engine.connect() as conn :
    result = conn.execute(stmt)
    conn.commit()