import logging
import os

from flask import Flask, request


app = Flask(__name__)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/application.log", encoding="utf-8", level=logging.DEBUG
)


@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"


@app.route("/stage")
def get_stage():
    stage = os.getenv("APP_STAGE", "dev")
    app.logger.info(f"Receiving request: {request}")
    return {"stage": stage}


@app.route("/env_values")
def env_values():
    environment_variables = os.environ.items()
    return {
        key: value for key, value in environment_variables if key.startswith("APP_")
    }
