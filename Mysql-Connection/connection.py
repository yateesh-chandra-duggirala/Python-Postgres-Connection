# After installing mysql-connector-python, Import the mysql.connector library.
import mysql.connector as mysql_conn

# Establishing the connection with a database named employee (which exists in my database).
conn = mysql_conn.connect(
    database = 'employee',
    user = 'root',
    password = '03072001',
    host = "127.0.0.1",
    port = "3306"
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Execute a query using the execute() method.
cursor.execute("select version()")

# Fetch a single row
data = cursor.fetchone()

# Print the message
print("Connection established to : ", data[0] + " MySQL Version")

# Closing the connection
conn.close()