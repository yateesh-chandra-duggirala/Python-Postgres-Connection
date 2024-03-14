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

# Fetch one result from the execution.
# result = cursor.fetchone()
# print(result)

# Fetch all Results from the execution
# result = cursor.fetchall()

# Fetch Many results from the execution
result = cursor.fetchmany(size=2)
print(result)

# Close the Connection
conn.close()