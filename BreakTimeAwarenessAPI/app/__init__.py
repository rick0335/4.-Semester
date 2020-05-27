from flask import Flask;
from sharpify import use_mvc;

app = Flask(__name__);
use_mvc(app, "", "");