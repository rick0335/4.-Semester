import inspect, jwt, datetime;
from app import app;
from flask import request, redirect, make_response, session


#region JWT Token methods
def get_jwt():
    auth_token = None;
    
    # See if we already have a API token
    try:
        auth_token = session["API_TOKEN"];
    except KeyError:
        pass;

    print(decode_jwt(auth_token));

    if auth_token == None or decode_jwt(auth_token) == False:
        auth_token = encode_jwt(session.get("logged_in"));
        session["API_TOKEN"] = auth_token;

    return auth_token;
    

def pop_jwt():
    try:
        session.pop("auth_token");
    except Exception:
        pass;

def encode_jwt(sub):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days = 0, seconds = 30),
        "iat": datetime.datetime.utcnow(),
        "sub": sub
    }

    return jwt.encode(payload, app.config.get("SECRET_KEY"), algorithm = "HS256");

def decode_jwt(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get("SECRET_KEY"));
        return True;
    
    except jwt.ExpiredSignatureError:
        return False;
    except jwt.InvalidTokenError:
        return False;

#endregion 

#region Decorators
def authenticate_with_session(f):
    def decorator(*args, **kwargs):
        
        user_session = None;

        try:
            user_session = session.get("logged_in");
        except:
            pass;

        # No session?
        if user_session is None:
            return redirect("/Authenticate/Login");
        
        return f(*args, **kwargs);

    decorator.__signature__ = inspect.signature(f); # This line will preserve the original signature of "f", instead of replacing it with (*args, **kwargs)

    return decorator;

def redirect_if_logged_in(f):
    def decorator(*args, **kwargs):
        
        user_session = None;

        try:
            user_session = session.get("logged_in");
        except:
            pass;

        # No session?
        if user_session != None:
            return redirect("/");
        
        return f(*args, **kwargs);

    decorator.__signature__ = inspect.signature(f); # This line will preserve the original signature of "f", instead of replacing it with (*args, **kwargs)

    return decorator;

#endregion