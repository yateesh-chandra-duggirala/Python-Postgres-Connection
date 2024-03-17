import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

collection.update_one({"name" : "Ramu"}, {"$set": {"city" : "Ayodhya"}})
print("Updated Successfully")

for doc in collection.find():
    print(doc)