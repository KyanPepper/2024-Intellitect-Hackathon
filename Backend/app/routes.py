from app import app, db
from app.models import *
from flask import Flask, jsonify
import requests
from flask_cors import CORS
CORS(app)


@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()


@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "Received data successfully"}
    return jsonify(response), 200


