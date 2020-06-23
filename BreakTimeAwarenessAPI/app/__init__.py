from flask import Flask;
from sharpify import use_mvc;

app = Flask(__name__);
app.config["JSON_SORT_KEYS"] = False;
app.config["SECRET_KEY"] = "\x84L6\x04\xb3\xcd\xfdk\xdd\xda\xd4y\x023+n\xf0P\x08)\x99\xb3\xb3";
use_mvc(app, "", "");

@app.route("/Test/<id>")
def Test(id:int):
    return f"<h1>{id}</h1>";

