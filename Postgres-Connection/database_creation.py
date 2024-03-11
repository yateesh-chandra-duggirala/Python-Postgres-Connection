# importing the psycopg2 library.
import psycopg2

# Establishing connection.
conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "postgres",
    host = "localhost",
    port = "5432"
)

# Set the Auto Commit to true.
conn.autocommit = True

# Creating a cursor object using the cursor() method.
cursor = conn.cursor()

# Write the SQL query to create a database.
sql_query = '''CREATE database mydb'''

# Execute the query 
cursor.execute(sql_query)
print("Database Created successfully....")

# Closing the connection.
conn.close()