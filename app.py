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

@app.route("/env_values")
def env_values():
    environment_variables = os.environ.items()
    return {key: value for key, value in environment_variables if key.startswith("APP_")}
