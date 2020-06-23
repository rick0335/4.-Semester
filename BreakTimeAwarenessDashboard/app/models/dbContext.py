from pymongo import MongoClient;

cluster = MongoClient("mongodb+srv://rickifunk:test12345@cluster0-s6yxl.mongodb.net/dashboard?retryWrites=true&w=majority");
db = cluster.dashboard;

def getLastDocumentId(collection):
    cursor = collection.find({}).sort([("_id", -1)]).limit(1);
    if cursor.count() == 0:
        return -1;

    return cursor[0]["_id"];


def get_user(name:str):
    return db.users.find_one({"username":name});


def insert_user(name:str, password:str):
    userToFind = get_user(name);
    if userToFind != None:
        raise Exception("User already exists");

    user = {
        "_id": int(getLastDocumentId(db.users)) + 1,
        "username": name,
        "password": password
    }

    db.users.insert_one(user);

    return True;