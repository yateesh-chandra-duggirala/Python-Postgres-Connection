# Import the library
import mysql.connector

# Establish the connection to the Mysql Database
conn = mysql.connector.connect(
    database = 'mydb',
    user = 'root',
    password = '03072001',
    port = '3306'
)

# Create a cursor object
cursor = conn.cursor()

# Create a table by dropping if it already exists.
cursor.execute("DROP Table if exists EMPLOYEE")

# Define a where clause
create_table = """
                CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
                )
                """

# Execute the Create table Statement Query
cursor.execute(create_table)

# Inserting the values all at once.
insert_statement = "INSERT INTO EMPLOYEE VALUES(%s, %s, %s, %s , %s)"
data = [('Krishna', 'Sharma', 19, 'M', 2000), ('Raj', 'Kandukuri', 20, 'M', 7000),
('Ramya', 'Ramapriya', 25, 'F', 5000),('Mac', 'Mohan', 26, 'M', 2000)]

cursor.executemany(insert_statement, data)

# Commit the changes
conn.commit()

# Let us select specific records using the where clause.
select_clause = "SELECT * From EMPLOYEE Where AGE > 23"
cursor.execute(select_clause)

print(cursor.fetchall())

# Close the connection
conn.close()