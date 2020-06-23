from flask import request, make_response;
from app.controllers.authenticateController import authenticate_with_session;
from utility import get_jwt;
import requests, json, datetime
from plotly import graph_objects as go;
import plotly;
from sharpify import *;
from app.controllers.authenticateController import authenticate_with_session;

class StudentController():
    
    @httpGet
    @authenticate_with_session
    def Index(id:int = None):
        # Setup request
        payload = {
            "API_TOKEN":get_jwt().decode("utf-8")
        }
        url = "http://localhost:5001/Student/Get/";
        if id != None:
            url = url + id + "/";
        r = requests.post(url, data=json.dumps(payload), headers={"Content-Type":"application/json"});
        data = r.json();

        if(id != None):
            # One student
            return View();
        else:
            # All students
            students_dict = json.loads(data);
            
            #region Students over time
            students_over_time = go.Figure(
                data=go.Scatter(
                    x = [ datetime.datetime(year=2010, month=1, day=1), 
                            datetime.datetime(year=2011, month=1, day=1), 
                            datetime.datetime(year=2012, month=1, day=1), 
                            datetime.datetime(year=2013, month=1, day=1), 
                            datetime.datetime(year=2014, month=1, day=1), 
                            datetime.datetime(year=2015, month=1, day=1), 
                            datetime.datetime(year=2016, month=1, day=1), 
                            datetime.datetime(year=2017, month=1, day=1), 
                            datetime.datetime(year=2018, month=1, day=1), 
                            datetime.datetime(year=2019, month=1, day=1), 
                            datetime.datetime(year=2020, month=1, day=1), ],
                    y = [364, 425, 485, 535, 583, 650, 725, 812, 859, 912, 1000],
                )
            )

            students_over_time.update_layout(
                title={
                        "text": "Students from 2010 - 2020",
                        "y": 0.9,
                        "x": 0.5
                    },
            )
            students_over_time_graph = json.dumps(students_over_time, cls=plotly.utils.PlotlyJSONEncoder);
            #endregion
            
            #region Male and females
            maleCount = 0;
            femaleCount = 0;
            for student in students_dict:
                if(student["gender"] == "male"):
                    maleCount += 1;
                else:
                    femaleCount += 1;
            
            students_male_female = go.Figure(
                data=go.Bar(
                    x = ["Male", "Female"],
                    y = [maleCount, femaleCount]
                )
            )

            students_male_female.update_layout(
                title={
                    "text": "Students gender",
                    "y": 0.9,
                    "x": 0.5
                }
            )
            students_male_female_graph = json.dumps(students_male_female, cls=plotly.utils.PlotlyJSONEncoder);
            return View(graphs = 
            {"students_over_time_graph": students_over_time_graph, 
            "students_male_female_graph": students_male_female_graph});