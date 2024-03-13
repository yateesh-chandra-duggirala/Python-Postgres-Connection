# import library mysql.connector
from mysql.connector import connection

# Establish the connection
conn = connection.MySQLConnection(
    user = 'root',
    password = '03072001',
    port = '3306'
)

conn.autocommit = True

# create an object for cursor.
cursor = conn.cursor()

# define the variable with drop query statement
drop_sql = "DROP DATABASE IF EXISTS mydb"

# Execute the Query
cursor.execute(drop_sql)

# define a variable that holds the CREATE DATABASE statement
create_db = "CREATE DATABASE mydb"

cursor.execute(create_db)
print("Database is successfully created")

cursor.execute("SHOW DATABASES")
print(" The List of the databases ",cursor.fetchall())

# Close the Connection
conn.close()