from sqlalchemy import create_engine

# Create an object for the create_engine class.
engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

# The String URL passed as an argument is main one.
# 1. This String URL contains sqlite, which links in SQLAlchemy to an object known as dialect
# 2. The Python DBAPI is a third party driver that SQLAlchemy uses to interact with a particular database.
#    Here we are using pysqlite, which in modern Python use is the sqlite standard library interface for SQLite.
# 3. Our URL indicates the phrase /:memory:, which is an indicator to the SQLite module that we will be using an
#    in-memory-only Database.
# 4. This kind of database is perfect is perfect for experimenting as it does not require any server nor does it
#    need to create new files.