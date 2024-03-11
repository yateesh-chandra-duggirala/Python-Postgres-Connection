# import the library psycopg2
import psycopg2

# Establish a connection with the postgres
conn = psycopg2.connect(
    database = 'mydb',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)

# Set the auto commit to True.
conn.autocommit = True

# Create a cursor Object
cursor = conn.cursor()

# Define a SQL Query with Insertion statements.
insertion_sql = '''
                INSERT INTO EMPLOYEE VALUES
                ('Ramya', 'Rama priya', 27, 'F', 9000),
                ('Vinay', 'Battacharya', 20, 'M', 6000),
                ('Sharukh', 'Sheik', 25, 'M', 8300),
                ('Sarmista', 'Sharma', 26, 'F', 10000),
                ('Tripthi', 'Mishra', 24, 'F', 6000)
                '''

# Execute the Query with the help of the cursor object.
cursor.execute (insertion_sql)

# Commit the changes in the database
conn.commit()
print("Inserted Rows Successfully...")

# Close the connection.
conn.close()