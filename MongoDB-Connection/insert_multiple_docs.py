from pymongo import MongoClient

client = MongoClient("mongodb+srv://yateesh:03072001@atlascluster.obmo7xb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

db = client['mydb']

collection = db['example']

doc_2 = [
{
    "name" : "Sita",
    "age" : 19,
    "city" : "Mithila"
},
{
    "name" : "Hanumanth",
    "age" : 17,
    "city" : "Maruthi Nagar"
},
{
    "name" : "Krishna",
    "age" : 16,
    "city" : "Madhura"
}
]

result = collection.insert_many(doc_2)
print("The Documents are successfully inserted")
print(result.inserted_ids)