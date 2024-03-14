# import library psycopg2
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    database = 'mydb',
    user = 'root',
    password = '03072001',
    port = '3306'
)

# create an object for cursor.
cursor = conn.cursor()

# define the variable with select statement
select_sql = "select * from employee"

# Execute the Query
cursor.execute(select_sql)
print(cursor.fetchall())
print(cursor.column_names)
# Check the row count
result = cursor.rowcount
print(result)

# Close the Connection
conn.close()