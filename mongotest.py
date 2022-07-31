import pymongo

client = pymongo.MongoClient("mongodb+srv://andanm:Andan7026@andan.8cn4bt2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
