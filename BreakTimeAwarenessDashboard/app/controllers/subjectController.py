from flask import request, make_response;
from sharpify import httpGet, View;
from app.controllers.authenticateController import authenticate_with_session;
from utility import get_jwt;
import requests, json, datetime
from plotly import graph_objects as go;
import plotly;

class SubjectController:

    @httpGet
    @authenticate_with_session
    def Index():
        # Setup request
        payload = {
            "API_TOKEN":get_jwt().decode("utf-8")
        }
        url = "http://localhost:5001/Student/Get/";
        r = requests.post(url, data=json.dumps(payload), headers={"Content-Type":"application/json"});
        data = r.json();
        students_dict = json.loads(data);

        # prepare and format data
        subjects_student_amount_dict = {};
        subjects_individual_amount_dict = {};
        for student in students_dict:
            grade = student["grade"];
            gender = student["gender"];
            if grade["subject"] not in subjects_student_amount_dict:
                subjects_student_amount_dict[grade["subject"]] = 1;
            else:
                subjects_student_amount_dict[grade["subject"]] = subjects_student_amount_dict[grade["subject"]] + 1;

            if grade["subject"] not in subjects_individual_amount_dict:
                subjects_individual_amount_dict[grade["subject"]] = [0, 0];

            gender_list = subjects_individual_amount_dict[grade["subject"]];
            if gender == "male":
                gender_list[0] = gender_list[0] + 1;
                subjects_individual_amount_dict[grade["subject"]] = gender_list;
            else:
                gender_list[1] = gender_list[1] + 1;
                subjects_individual_amount_dict[grade["subject"]] = gender_list;

        #region subjects_student_amount
        subjects_student_amount = go.Figure(
            data=[go.Pie(
                labels=["Chemistry", "Physics", "P.E", "Communication", "English", "Engineering", "Science", "Biology", "Mathematics"],
                values=[
                    subjects_student_amount_dict["Chemistry"], 
                    subjects_student_amount_dict["Physics"], 
                    subjects_student_amount_dict["P.E"], 
                    subjects_student_amount_dict["Communication"], 
                    subjects_student_amount_dict["English"], 
                    subjects_student_amount_dict["Engineering"], 
                    subjects_student_amount_dict["Science"], 
                    subjects_student_amount_dict["Biology"], 
                    subjects_student_amount_dict["Mathematics"], 
                ]
            )]
        )

        subjects_student_amount.update_layout(
            title={
                "text": "Students across subjects",
                "y": 0.9,
                "x": 0.5
            },
        )
        subjects_student_amount_graph = json.dumps(subjects_student_amount, cls=plotly.utils.PlotlyJSONEncoder);
        #endregion
        print(subjects_individual_amount_dict);
        #region subjects_individual_amount
        subjects_individual_amount = go.Figure(
            data=[
                go.Bar(
                    name="Male",
                    x=["Chemistry", "Physics", "P.E", "Communication", "English", "Engineering", "Science", "Biology", "Mathematics"],
                    y=[
                        subjects_individual_amount_dict["Chemistry"][0],
                        subjects_individual_amount_dict["Physics"][0],
                        subjects_individual_amount_dict["P.E"][0],
                        subjects_individual_amount_dict["Communication"][0],
                        subjects_individual_amount_dict["English"][0],
                        subjects_individual_amount_dict["Engineering"][0],
                        subjects_individual_amount_dict["Science"][0],
                        subjects_individual_amount_dict["Biology"][0],
                        subjects_individual_amount_dict["Mathematics"][0],
                    ]
                ),

                go.Bar(
                    name="Female",
                    x=["Chemistry", "Physics", "P.E", "Communication", "English", "Engineering", "Science", "Biology", "Mathematics"],
                    y=[
                        subjects_individual_amount_dict["Chemistry"][1],
                        subjects_individual_amount_dict["Physics"][1],
                        subjects_individual_amount_dict["P.E"][1],
                        subjects_individual_amount_dict["Communication"][1],
                        subjects_individual_amount_dict["English"][1],
                        subjects_individual_amount_dict["Engineering"][1],
                        subjects_individual_amount_dict["Science"][1],
                        subjects_individual_amount_dict["Biology"][1],
                        subjects_individual_amount_dict["Mathematics"][1],
                    ]
                ),
            ]
        )

        subjects_individual_amount.update_layout(
            title={
                "text": "Gender across subjects",
                "y": 0.9,
                "x": 0.5
            },
        )

        subjects_individual_amount_graph = json.dumps(subjects_individual_amount, cls=plotly.utils.PlotlyJSONEncoder);
        #endregion

        return View(graphs={
            "subjects_student_amount_graph":subjects_student_amount_graph,
            "subjects_individual_amount_graph":subjects_individual_amount_graph
        });
