# Import the psycopg2 library.
import psycopg2

# Establishing the connection with a database named hospital (which exists in my database).
conn = psycopg2.connect(
    database = 'hospital',
    user = 'postgres',
    password = 'postgres',
    host = "localhost",
    port = "5432"
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Execute a query using the execute() method.
cursor.execute("select version()")

# Fetch a single row
data = cursor.fetchone()

# Print the message
print("Connection established to :\n", data)

# Closing the connection
conn.close()