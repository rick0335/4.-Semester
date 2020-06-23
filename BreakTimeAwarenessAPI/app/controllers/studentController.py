from sharpify import httpGet, httpPost;
from flask import jsonify, request, make_response;
from app.models.dbContext import get_student, get_students;
from app.utility import authenticate_with_token;
from bson.json_util import dumps, loads

class StudentController:

    @httpPost
    @authenticate_with_token
    def Get(id = None):

        if id != None:
            student = get_student(id);
            print(student);
            return jsonify(student);
        
        else:
            students = get_students();
            students_dumps = dumps(students);
            return jsonify(students_dumps);

