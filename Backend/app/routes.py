from app import app, db
from flask import Flask, jsonify
from flask_cors import CORS
from app.models import User

CORS(app)
url = "https://nominatim.openstreetmap.org/search"

#Generates SQL lite DB
@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

#Test route
@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "All good"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/createuser", methods=["POST", "GET"])
def createuser():
    User1 = User(username="test", email="asdasd", lastname="asdasd")
    db.session.add(User1)
    db.session.commit()

    response = {"message": "User created"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200

