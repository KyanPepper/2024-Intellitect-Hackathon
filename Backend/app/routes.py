from app import app, db
from flask import Flask, jsonify
from flask_cors import CORS
from app.models import Application,Categories,Resource
from app.helperfunctions import create_categories, get_lat_long,scrape_img_from_provided_website

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



#get categories for drop down lists
@app.route("/getcategories", methods=["GET"])
def getcategories():
    categories = Categories.query.all()
    categories_list = []
    for category in categories:
        categories_list.append({'id': category.id, 'name': category.name})
    return jsonify(categories_list), 200

#get applications for appove or deny
@app.route("/getapplications", methods=["GET"])
def getapplications():
    applications = Application.query.all()
    applications_list = []
    for application in applications:
        applications_list.append({
            'id': application.id,
            'organization': application.organization,
            'description': application.description,
            'address': application.address,
            'phoneNumber': application.phoneNumber,
            'email': application.email,
            'website': application.website,
            'category_id': application.category_id
        })
    return jsonify(applications_list), 200


@app.route("/approveapplication<id>", methods=["POST"])
def approveapplication(id):
    application = Application.query.get(id)
    if not application:
        return jsonify({"message": "Application not found"}), 404
    
    reasource = Resource(
        name=application.organization,
        description=application.description,
        address=application.address,
        phoneNumber=application.phoneNumber,
        email=application.email,
        website=application.website,
        category_id=application.category_id
    )
    
    coordinates = get_lat_long(application.address)
    if coordinates:
        reasource.lat = coordinates[0]
        reasource.lon = coordinates[1]
    
    reasource.img = scrape_img_from_provided_website(application.website)
    db.session.add(reasource)
    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application approved"}), 200

