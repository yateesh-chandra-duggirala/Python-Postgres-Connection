import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client["mydb"]

collection = db["example"]

for doc in collection.find().sort("age", -1):
    print(doc)