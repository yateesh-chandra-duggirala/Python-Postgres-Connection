import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

collection.update_many({}, {"$set": {"city" : "Lanka"}})
print("Updated Many Documents Successfully")

for doc in collection.find():
    print(doc)