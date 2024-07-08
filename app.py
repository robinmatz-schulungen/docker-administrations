import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"

@app.route("/stage")
def get_stage():
    stage = os.getenv("APP_STAGE", "dev")
    return {"stage": stage}
