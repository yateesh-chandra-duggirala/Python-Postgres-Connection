# Import the library
import psycopg2

# Establish the connection to the postgres
conn = psycopg2.connect(
    database = 'mydb',
    user = 'postgres',
    password = 'postgres',
    port = '5432'
)

# Set the auto commit to true
conn.autocommit = True

# Create a cursor object
cursor = conn.cursor()

# Define a where clause
select_sql = "SELECT * FROM EMPLOYEE WHERE AGE > 25"

# Execute the Statement Query
cursor.execute(select_sql)
print(cursor.fetchall())

# Commit the changes
conn.commit()

# Close the connection
conn.close()

