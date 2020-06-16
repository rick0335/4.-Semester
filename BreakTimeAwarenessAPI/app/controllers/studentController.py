from sharpify import httpGet;
from flask import jsonify;
from app.models.dbContext import get_student;

 
class StudentController:

    @httpGet
    def Get(id):
        student = get_student(id);
        return jsonify(student);