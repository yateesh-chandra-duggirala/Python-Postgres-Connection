# import library psycopg2
import psycopg2

# Establish the connection
conn = psycopg2.connect(
    database = 'mydb',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

# Set the Autocommit to True.
conn.autocommit = True

# create an object for cursor.
cursor = conn.cursor()

# define the variable with select statement
select_sql = "select * from employee"

# Execute the Query
cursor.execute(select_sql)

# Fetch one result from the execution.
result = cursor.fetchone()
print(result)

# Fetch all Results from the execution
# result = cursor.fetchall()

# Fetch Many results from the execution
result = cursor.fetchmany()
print(result)

# Commit the changes to the database.
conn.commit()

# Close the Connection
conn.close()