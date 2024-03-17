# Python Mongodb Connection
## Connecting MongoDB from Python
- The connection class of the pymongo represents/ handles an instance of a connection.
- pymongo is a Python Distribution which provides tools to work with Mongo DB database from python Database adapter that connects Python and MongoDB

### 1. Creating database :
- Unlike other Databases, Mongo DB Does not provide the Special command to create Databases.
- Inorder to create a database, We just Run The USE Database commmand. By running this command, If the database already exists, It gets connected to it or else it just creates a new Database and connects.
- Refer the [database_creation.py]() script

### 2. Creating Collections :
- A Collection is analogous to a table in relational Database.
- A Collection can be created using the createCollection() method. This method accepts a String value representing the name of the collection to be created and an options parameter.
- View the [collection_Creation.py]() to understand the working.

### 3. Inserting Single Document :
- Documents can be stored into MongoDB using the insert() method.
- Actually this method accepts a JSON Document as a parameter.
- Pymongo provides a method named insert_one() to insert a mongodb, And we need to a pass a dictionary as an input
- Another method is also provided by PyMango to insert many documents at once, It is insert_many().
- Have a look at the [insert_document.py]() for insert_one() and [insert_multiple_docs.py]() for insert_many().

### 4. Retrieving Documents :
- Stored Documents can be read/ retrieved from MongoDB using the find() method.
- This method retrieves the displays all documents in a non-structured way.
- The Find_one() method is used to retrieve a single document based on the query.
- In case of no matches, this method returns nothing and if you do not use any query it returns the first document from the collection
- Refer to the [find_document.py]()

- Some of the operators used along with the queries are as follows :

a. Equality	            :   {"key" : "value"}
b. Less Than	        :   {"key" :{$lt:"value"}}
c. Less Than Equals	    :   {"key" :{$lte:"value"}}
d. Greater Than	        :   {"key" :{$gt:"value"}}
e. Greater Than Equals	:   {"key" {$gte:"value"}}
f. Not Equals	        :   {"key":{$ne: "value"}}

### 5. Sort the Contents :
- While retrieving the contents of a collection, you can sort and arrange them in ascending and descending order using sort() method. -1 for ascending order by
- A number should be passed as an argument representing the number of documents needed as a result.
- Refer into [sort_document.py]() script once.

### 6. Update Script :
- Contents of an existing document can be modified by using update() or save() methods.
- The difference is that update() just modifies the document whereas the save() method replaces existing document with new one.
- Also, we can update a single document using update_one() or else we can update multiple documents at once using the update_many() method.
- View the [update_document.py]() and [update_many.py]() for a better understanding.

### 7. Limit Documents :
- While retrieving the contents of a collection you can limit the number of documents in the result using the limit() method.
- This method accepts the number value representing the number of required documents in the result.
- Once view the [limit_documents.py]() to know the concept better.

### 8. Delete Documents :
- To delete the documents from a collection of MongoDB, We can use delete_one() or delete_many().
- These methods accept a query object specifying the condition for deleting the documents.
- The delete_one() method deletes a single document, in case of a match. If no query is specified , This method deletes the first document from the collection.
- Study the [delete_document.py]() and [delete_many.py]() carefully.

### 10. Drop Collection :
- To drop the collection from the database, you can just use the drop() method
- Have a look at the [drop_collection.py]().


## Cursor Object :
- The Cursor class of the MongoDB.connector library provide methods to execute the MongoDB commands in the database using python code.
- Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
- You can create Cursor object using the cursor() method of the Connection object/class.
- Look into [cursor.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/MongoDB-connection/MongoDB-Connection/cursor.py)

### a. Methods provided by cursor class/ Object.

1. callProc() : This method is used to call existing procedures MongoDB database.
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