from sharpify import httpGet, httpPost, View;
import datetime, jwt, inspect;
from flask import session, request, redirect, render_template, url_for;
from app import app;
from app.models.dbContext import insert_user, get_user;
from utility import redirect_if_logged_in, authenticate_with_session


class AuthenticateController():

    @httpPost
    @httpGet
    @redirect_if_logged_in
    def Login():

        # Check if user is already logged in
        #auth_token = get_jwt();
        #if(decode_jwt(get_jwt()) == True):
            #return "<h1>You are already logged in</h1>";

        print(request.headers.get("Authorization"));

        # Return log in view
        if(request.method == "GET"):
            return View();

        # Create jwt token and store it
        if(request.method == "POST"):
            username = request.form["username"];
            password = request.form["password"];

            # VALIDATE WITH DB
            user_to_find = get_user(username.lower());
            if(user_to_find is None):
                return View(error = "Cant find a user with the provided information");

            if(user_to_find["password"] != password):
                return View(error = "Password does not match the username");
            
            session["logged_in"] = user_to_find["_id"];
            
            #auth_token = encode_jwt(username);
            #session["auth_token"] = auth_token;
            

            return redirect("/");

    @httpPost
    @httpGet
    def Register():
        if(request.method == "GET"):
            return View();

        if(request.method == "POST"):
            username = request.form["username"];
            password = request.form["password"];

            try:
                insert_user(username.lower(), password);
            except Exception:
                return View(error = "User already exists");

            user_to_find = get_user(username.lower());

            session["logged_in"] = user_to_find["_id"];

            return redirect("/");

    @httpGet
    def Logout():
        try:
            session.pop("logged_in");
        except:
            pass;

        return redirect("/Authenticate/Login");








