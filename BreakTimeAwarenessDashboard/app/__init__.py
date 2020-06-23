import datetime, jwt;
from flask import Flask, session;
from sharpify import use_mvc, use_htmlAttributes;
from app.models.dbContext import getLastDocumentId;

app = Flask(__name__);
app.config["SECRET_KEY"] = "\x84L6\x04\xb3\xcd\xfdk\xdd\xda\xd4y\x023+n\xf0P\x08)\x99\xb3\xb3";
app.config["SESSION_PERMANENT"] = True;
use_mvc(app, "StudentController", "Index");
use_htmlAttributes();