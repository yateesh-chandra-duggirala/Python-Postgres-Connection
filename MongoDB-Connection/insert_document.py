# Importing the connector
import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

coll = db['example']

doc1 = {
    "name" : "Ramu",
    "age" : 26,
    "city" : "Hyderabad"
}

coll.insert_one(doc1)
print(coll.find_one())

