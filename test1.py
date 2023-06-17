from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://aryanpankaj0783:mongo123@cluster0.yhzsliz.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client.test
print(db)

d = {
    'name':'aryan',
    'email':'aryan@gmail.com',
    'surname':'pankaj'
}

db1 = client['mongotest']
col1 = db1['test']

col1.insert_one(d)

