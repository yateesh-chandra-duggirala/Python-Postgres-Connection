import pymongo

client = pymongo.MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

print("The Collections before dropping :")

for coll in db.list_collection_names():
    print(coll)
print("\n")

collection.drop()
print("The Collection is dropped from the Database..!")

print("The Collections list after dropping :")

for coll in db.list_collection_names():
    print(coll)
