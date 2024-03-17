import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

# Retrieving the first Document from the collection.
print(collection.find_one())

# Retrieving the specific record from the collection
print(collection.find_one({"name" : "Sita"}))

# Retrieving all records using find() method
for doc in collection.find():
    print(doc)

print("\n")

# Retrieving the documents from the collection whose age is greater than 18
for doc1 in collection.find({"age" : {"$gt" : 16}}):
    print(doc1)

