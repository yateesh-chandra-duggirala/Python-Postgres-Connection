# import the psycopg2 library
import psycopg2

# Establish a connection
conn = psycopg2.connect(
    database= 'mydb',
    user = 'postgres',
    password = 'postgres'
)

# Set the Auto Commit to True
conn.autocommit = True

# Create a Cursor Object using the Cursor() method
cursor = conn.cursor()

# Retrieving the Rows in a specific order.
cursor.execute("SELECT * FROM employee ORDER BY Age")
print(cursor.fetchall())

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()