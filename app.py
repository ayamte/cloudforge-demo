from flask import Flask
import os

app = Flask(__name__)
@app.route("/")
def hello():
    return "Bienvenue sur CloudForge Demo"

@app.route("/health")
def healthy():
    return "OK"


@app.route("/version")
def version():
    return os.getenv("APP_VERSION", "dev")

