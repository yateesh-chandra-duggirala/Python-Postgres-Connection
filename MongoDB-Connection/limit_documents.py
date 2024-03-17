import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
)

db = client['mydb']

collection = db["example"]

# Displaying limited documents 
for doc in collection.find().limit(3):
    print(doc)

print("\n")

# Displaying the limited documents after sorting
for doc in collection.find().sort("age").limit(2):
    print(doc)