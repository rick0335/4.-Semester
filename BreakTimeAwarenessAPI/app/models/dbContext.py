from pymongo import MongoClient;

cluster = MongoClient("mongodb+srv://rickifunk:test12345@cluster0-s6yxl.mongodb.net/sample_training?retryWrites=true&w=majority");
db = cluster.sample_training;

def get_student(id):
    
    unique_class_ids = db["grades"].find({"student_id":int(id)}).distinct("class_id");
    student_data = {};
    student_data["student_id"] = int(id);
    student_data["classes"] = [];

    for class_id in unique_class_ids:
        classes = db["grades"].find({"student_id":int(id), "class_id":class_id});
        class_dict = {};
        class_dict["class_id"] = int(class_id);
        for grade in classes:
            class_dict["exam_score"] = grade["scores"][0]["score"];
            class_dict["quiz_score"] = grade["scores"][1]["score"];
            class_dict["homework1_score"] = grade["scores"][2]["score"];
            class_dict["homework2_score"] = grade["scores"][3]["score"];

        student_data["classes"].append(class_dict);

    return student_data;

  




    

    