import jwt, json, inspect;
from app import app;
from flask import request, make_response

def authenticate_with_token(f):
    def decorator(*args, **kwargs):
        print(request.get_json());
        auth_token = request.get_json()["API_TOKEN"];
        
        try:
            payload = jwt.decode(auth_token, app.config.get("SECRET_KEY"));
            print("Authorized access");
            return f(*args, **kwargs);
        except jwt.ExpiredSignatureError:
            return make_response("Bad token", 403);
        except jwt.InvalidTokenError:
            return make_response("Bad token", 403);
        
        return f(*args, **kwargs);

    decorator.__signature__ = inspect.signature(f); # This line will preserve the original signature of "f", instead of replacing it with (*args, **kwargs)

    return decorator;