from flask import Flask;
from sharpify import use_mvc;

app = Flask(__name__);
app.config["JSON_SORT_KEYS"] = False;
use_mvc(app, "", "");

