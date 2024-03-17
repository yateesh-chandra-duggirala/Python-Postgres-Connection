# importing the library psycopg2
import psycopg2

# Establish a connection between the Python and Postgres
conn = psycopg2.connect(
    database = "mydb",
    user = "postgres",
    password = "postgres",
    host = "localhost",
    port = "5432"
)

# Create a cursor object
cursor = conn.cursor()

# Drop the table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Creating Table Creation Query in a variable
sql = ''' CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    GENDER CHAR(1),
    INCOME FLOAT
)
'''

try:
    # Execute the Query
    cursor.execute(sql)
    print("Table succssfully created successfully...!")
    
    # Commit the changes to the database.
    conn.commit()

except psycopg2.errors.SyntaxError as e:
    print(f"Syntax Error : {e}")

# Close the connection.
conn.close()