# Python PostgreSQL Connection
## Connecting from PSQL Shell
- PostgreSQL provides its own shell to execute queries.
- To establish the connection with the postgresql database, make sure that you have installed it properly in the system.
- If you are able to connect to your database, We are good to go.

## Connecting from Python
- The connection class of the psycopg2 represents/ handles an instance of a connection.
- psycopg2 (Psychotic Postgres 2.0) is a Database adapter that connects Python and Postgres

### 1. Establishing connection :
- New connections can be created using the connect() function.
- This accepts the basic connection parameters such as dbname, user, password, host, port, and returns a connection object.
- Using this function, we can establish a connection with the postgreSQL.
- If the database does not exist, then it will be created and finally a database object will be returned.
- Refer to [connection.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/connection.py) for better understanding

### 2. Creating database :
- The cursor class of psycopg2 provides various methods execute various postgreSQL Commands, fetch records and copy data.
- A cursor object can be created using the cursor() method of the connection class.
- The execute() method of this class accepts a postgresql query as a parameter and executes it.
- In order to create a database in postgreSQL execute the CREATE DATABASE query using this method.
- Refer the [database_creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/database_creation.py) script

### 3. Creating Table :
- Let us execute the CREATE TABLE query using execute() method.
- Before that we have to execute another query DROP Table If exists if we want to create a new table instead of the old one.
- View the [table_creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/table_creation.py) to understand the working.

### 4. Inserting Rows :
- We have to execute the INSERT Query using the execute() method.
- For clear info, Have a look at the [insertion_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/insertion_script.py) script.

### 5. Retrieving Data :
- Read Operation means to fetch some information from the database.
- Data can be fetched using fetch() method provided by the psycopg2
- The Cursor Class provides three methods namely fetchall(), fetchOne() and fetchMany()
a. fetchall() - This method retrieves all the rows in the result set of query and returns them as list of tuples.
b. fetchone() - This method fetches the next row in the result of a query and returns it as a tuple.
c. fetchMany() - This method is similar to fetchOne() but, it retrieves the next set of rows in the result set of a query, instead of a single row.
**A Result Set is an object that is returned when a cursor object is used to query a table.**
- Refer to the [select_statement.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/select_statement.py)

### 6. Where Clause using Python
- To fetch the specific records from a table using the python program execute the select statement with WHERE Clause, by passing it as a parameter to the execute() method.
- Go to [conditional_select.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/conditional_select.py) script to learn the steps.

### 7. Update Script using Python
- To update the records from the table, you can just execute the update statement by passing it as a parameter to the execute() method.
- View the [update_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/update_script.py) for a better understanding

### 8. Delete Script using Python
- To Delete the records from the table, you can just execute the Delete statement by passing the query as a parameter to the execute() method.
- Once view the [delete_script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/delete_script.py) to know the concept better.

### 9. Drop Table
- To drop the table from the table, you can just execute the DROP TABLE Query by passing it as a parameter to the execute() method.
- Have a look at the [drop_table.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/drop_table.py).

### 10. Limit The Rows
- To Limit the Rows or even Offset in that aspect from a table, we can just execute the Query with limit and offset keywords as a parameter to the execute() method
- Go through the [select_limit.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/select_limit.py)

### 11. Join Tables
- We can also run the join condition over two tables and execute by Passing that Query as Parameter to the execute() method
- Study the [join.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/join.py) carefully.

## Cursor Object :
- The Cursor class of the psycopg library provide methods to execute the PostgreSQL commands in the database using python code.
- Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
- You can create Cursor object using the cursor() method of the Connection object/class.
- Look into [cursor.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/cursor.py)

### a. Methods provided by cursor class/ Object.

1. callProc : This method is used to call existing procedures PostgreSQL database.
2. close() : This method is used to close the current cursor object.
3. executemany() : This method accepts a list series of parameters list. Prepares a query and executes it with all the parameters.
4. execute() : This method accepts a query as a parameter and executes the given query.
5. fetchall() : This method retrieves all the rows in the result set of a query and returns them as list of tuples.
6. fetchone() : This method fetches the next row in the result of a query and returns it as a tuple.
7. fetchmany() : This method is similar to the fetchone() but, it retrieves the next set of rows in the result set of a query, instead of a single row.

### b. Properties of cursor Object :

1. description : This is a read only property which returns the list containing the description of columns in a result-set.
2. astrowid : This is a read only property, if there are any auto-incremented columns in the table, this returns the value generated for that column in the last INSERT or, UPDATE operation.
3. rowcount : This returns the number of rows returned/updated in case of SELECT and UPDATE operations.
4. closed : This property specifies whether a cursor is closed or not, if so it returns true, else false.
5. connection : This returns a reference to the connection object using which this cursor was created.
6. name : This property returns the name of the cursor.
7. scrollable : This property specifies whether a particular cursor is scrollable.