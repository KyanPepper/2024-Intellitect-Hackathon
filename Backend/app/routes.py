from app import app, db
from flask import Flask, jsonify
from flask_cors import CORS
from app.models import Application,Categories
from app.helperfunctions import create_categories

CORS(app)

#Generates SQL lite DB
@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()
        create_categories()

#Test route
@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "All good"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200


@app.route("/", methods=["POST", "GET"])
def createuser():
    response = {"message": "All good"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200

@app.route("/postapplications", methods=["POST"])
def postapplications(request):
    data = request.json
    application = Application(
        organization=data.get("organization"),
        description=data.get("description"),
        address=data.get("address"),
        phoneNumber=data.get("phoneNumber"),
        email=data.get("email"),
        website=data.get("website"),
        category_id=data.get("category_id")
    )
    db.session.add(application)
    db.session.commit()
    return jsonify({"message": "Application created"}), 200

