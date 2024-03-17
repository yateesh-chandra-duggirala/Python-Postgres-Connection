# Importing the connector
import mysql.connector

# Establishing the connection to the mysql database
conn = mysql.connector.connect(
    user = 'root',
    password = '03072001',
    database = 'mydb',
    host = 'localhost',
    port = '3306'
)

# Creating a curosr object
cursor = conn.cursor()

# Defining a Insert Statement
insert_statement = """INSERT INTO EMPLOYEE(
   FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try :
    # Execute the insert statement
    cursor.execute(insert_statement)
    print("successfully inserted") 
    
    # Commit in case of no errors
    conn.commit()

except :
    # Rollback in case of any errors
    conn.rollback()

# Finally close the connection
conn.close()