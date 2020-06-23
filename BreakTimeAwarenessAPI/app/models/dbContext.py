from pymongo import MongoClient;

cluster = MongoClient("mongodb+srv://rickifunk:test12345@cluster0-s6yxl.mongodb.net/sample_training?retryWrites=true&w=majority");
db = cluster.sample_training;

def get_student(id):
    return db.students.find_one({"_id": int(id)});

def get_students():
    return db.students.find({});
    

  




    

    