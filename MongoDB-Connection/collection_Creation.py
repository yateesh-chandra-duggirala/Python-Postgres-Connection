from pymongo import MongoClient

# Establish the Client and connect.
client = MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

# Getting the database Instance
db = client["mydb"]

# Create a Collection
collection = db["example"]

print("Collection is created..!")
print("Collections List : ", db.list_collection_names())