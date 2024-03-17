# import the mysql.connector library
import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    database= 'mydb',
    user = 'root',
    password = '03072001'
)

# Create a Cursor Object using the Cursor() method
cursor = conn.cursor()

# Retrieving the Rows in an ascending order of Age.
cursor.execute("SELECT * FROM employee ORDER BY Age")
age_result_asc = cursor.fetchall()
print(age_result_asc)

# Retrieving the Rows in a descending order by Salary.
cursor.execute("Select * from employee order by income desc")
income_result_desc = cursor.fetchall()
print(income_result_desc)

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()