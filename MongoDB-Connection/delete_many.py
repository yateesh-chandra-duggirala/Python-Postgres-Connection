import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

collection.delete_many({"age" : {"$lt" : 20}})
print("Deleted the documents less than 20 years age..!")

for doc in collection.find():
    print(doc)