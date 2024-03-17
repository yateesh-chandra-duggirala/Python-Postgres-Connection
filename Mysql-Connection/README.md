# Python MySQL Connection
## Connecting from MySQL Shell
- MySQL provides its own shell to execute queries.
- To establish the connection with the MySQL database, make sure that you have installed it properly in the system.
- If you are able to connect to your database, We are good to go.

## Connecting from Python
- The connection class of the mysql.connector represents/ handles an instance of a connection.
- mysql-connector-python is a Database adapter that connects Python and MySQL

### 1. Establishing connection :
- New connections can be created using the connect() function.
- This accepts the basic connection parameters such as dbname, user, password, host, port, and returns a connection object.
- Using this function, we can establish a connection with the MySQL.
- If the database does not exist, then it will be created and finally a database object will be returned.
- Refer to [connection.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/connection.py) for better understanding

### 2. Creating database :
- The cursor class of mysql-connector provides various methods execute various MySQL Commands, fetch records and copy data.
- A cursor object can be created using the cursor() method of the connection class.
- The execute() method of this class accepts a MySQL query as a parameter and executes it.
- In order to create a database in MySQL execute the CREATE DATABASE query using this method.
- Refer the [database_creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/database_creation.py) script

### 3. Creating Table :
- Let us execute the CREATE TABLE query using execute() method.
- Before that we have to execute another query DROP Table If exists if we want to create a new table instead of the old one.
- View the [table_creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/table_creation.py) to understand the working.

### 4. Inserting Rows :
- We have to execute the INSERT Query using the execute() method.
- Also we can use executeMany() method to insert multiple Queries at a time
- For clear info, Have a look at the [insertion_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/insertion_script.py) script.

### 5. Retrieving Data :
- Read Operation means to fetch some information from the database.
- Data can be fetched using fetch() method provided by the mysql-connector
- The Cursor Class provides three methods namely fetchall(), fetchOne() and fetchMany()
a. fetchall() - This method retrieves all the rows in the result set of query and returns them as list of tuples.
b. fetchone() - This method fetches the next row in the result of a query and returns it as a tuple.
c. fetchMany() - This method is similar to fetchOne() but, it retrieves the next set of rows in the result set of a query, instead of a single row. Also, we can use the (size = 3) as parameter to retrieve certain limit of rows
**A Result Set is an object that is returned when a cursor object is used to query a table.**
- Refer to the [select_statement.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/select_statement.py)

### 6. Where Clause using Python
- To fetch the specific records from a table using the python program execute the select statement with WHERE Clause, by passing it as a parameter to the execute() method.
- Go to [conditional_select.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/conditional_select.py) script to learn the steps.

### 7. Order by Using Python 
- To retreive The records in a desired order we write the Query that sorts the order of the items to be fetched accordingly and pass it as a parameter to the execute() Method.
- Refer into [order_by.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/order_by.py) script once.

### 8. Update Script using Python
- To update the records from the table, you can just execute the update statement by passing it as a parameter to the execute() method.
- View the [update_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/update_script.py) for a better understanding

### 9. Delete Script using Python
- To Delete the records from the table, you can just execute the Delete statement by passing the query as a parameter to the execute() method.
- Once view the [delete_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/drop_table.py) to know the concept better.

### 10. Limit The Rows
- To Limit the Rows or even Offset in that aspect from a table, we can just execute the Query with limit and offset keywords as a parameter to the execute() method
- Go through the [select_limit.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/select_limit.py)

### 11. Join Tables
- We can also run the join condition over two tables and execute by Passing that Query as Parameter to the execute() method
- Study the [join.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/join.py) carefully.

### 12. Drop Table
- To drop the table from the database, you can just execute the DROP TABLE Query by passing it as a parameter to the execute() method.
- Have a look at the [drop_table.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/drop_table.py).


## Cursor Object :
- The Cursor class of the mysql.connector library provide methods to execute the MySQL commands in the database using python code.
- Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
- You can create Cursor object using the cursor() method of the Connection object/class.
- Look into [cursor.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/mysql-connection/Mysql-Connection/cursor.py)

### a. Methods provided by cursor class/ Object.

1. callProc() : This method is used to call existing procedures MySQL database.
2. close() : This method is used to close the current cursor object.
3. executemany() : This method accepts a list series of parameters list. Prepares a query and executes it with all the parameters.
4. execute() : This method accepts a query as a parameter and executes the given query.
5. fetchall() : This method retrieves all the rows in the result set of a query and returns them as list of tuples.
6. fetchone() : This method fetches the next row in the result of a query and returns it as a tuple.
7. fetchmany() : This method is similar to the fetchone() but, it retrieves the next set of rows in the result set of a query, instead of a single row.
8. fetchwarnings() : This method returns the warnings generated by the last executed query.
9. Info() : This method gives the information about the last query.

### b. Properties of cursor Object :

1. description : This is a read only property which returns the list containing the description of columns in a result-set.
2. lastrowid : This is a read only property, if there are any auto-incremented columns in the table, this returns the value generated for that column in the last INSERT or, UPDATE operation.
3. rowcount : This returns the number of rows returned/updated in case of SELECT and UPDATE operations.
4. statement : This property returns the last executed statement.
5. column_names = This is a read only property which returns the list of columns as a result set.