from app import app, db
from flask import Flask, jsonify
from flask_cors import CORS
CORS(app)

#Generates SQL lite DB
@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

#Test route
@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "Received data successfully"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200


@app.route("/")
def home():
    return "Hello, World!"
