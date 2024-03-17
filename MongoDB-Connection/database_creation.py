# import library pymongo
import pymongo

# Establish the connection
client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

# Create a new database.
db = client["mydb"]
print("Database created successfully.")

# Fetch The List of Databases from the Client
print("The List of Databases : \n", client.list_database_names())
