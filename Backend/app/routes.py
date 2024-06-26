from app import app, db
from flask import Flask, jsonify,request,make_response
from flask_cors import CORS
from app.models import Application,Categories,Resource
from app.helperfunctions import create_categories, get_lat_long,scrape_img_from_provided_website,seedResources,seed_applications

CORS(app)


#Generates SQL lite DB
@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()
        create_categories()
        seed_applications()
        seedResources()

#Test route
@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "All good"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200

@app.route("/seedandclear", methods=["GET"])
def seed():
    db.drop_all()
    create_categories()
    seedResources()
    seed_applications()
    return jsonify({"message": "DB Cleared and Seeded"}), 200

@app.route("/", methods=["POST", "GET"])
def createuser():
    response = {"message": "All good"}
    #response and status code (200 is good 400 is bad request)
    return jsonify(response), 200



@app.route("/postapplications", methods=["POST", "OPTIONS"])
def postapplications():
    if request.method == "POST":
        data = request.json
        application = Application(
            organization=data.get("organization"),
            description=data.get("description"),
            address=data.get("address"),
            phoneNumber=data.get("phoneNumber"),
            email=data.get("email"),
            website=data.get("website"),
            category_id=data.get("category_id"),
            tags=data.get("tags")
        )
        db.session.add(application)
        db.session.commit()
        response = jsonify({"message": "Application created"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200
        
    elif(request.method == "OPTIONS"):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response, 200
    
    return jsonify({"message": "Application not created"}), 400

if __name__ == "__main__":
    app.run(debug=True)

#get categories for drop down lists
@app.route("/getcategories", methods=["GET"])
def getcategories():
    categories = Categories.query.all()
    categories_list = []
    for category in categories:
        categories_list.append({'id': category.id, 'name': category.name})
    return jsonify(categories_list), 200

#get applications 
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
            'category_id': application.category_id,
            'tags': application.tags
        })
    return jsonify(applications_list), 200

#approve application logic
@app.route("/approveapplication/<id>", methods=["POST"])
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
        category_id=application.category_id,
        tags=application.tags
    )
    
    coordinates = get_lat_long(application.address)
    if coordinates:
        reasource.lat = coordinates[0]
        reasource.lon = coordinates[1]
    
    img = scrape_img_from_provided_website(application.website)
    if img:
        reasource.img = img
    else:
        reasource.img = "https://aspr.hhs.gov/at-risk/PublishingImages/At-Risk-Categories.png"
    db.session.add(reasource)
    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application approved"}), 200


@app.route("/deleteapplication/<id>", methods=["DELETE"])
def deleteapplication(id):
    application = Application.query.filter_by(id=id).first()
    if not application:
        return jsonify({"message": "Application not found"}), 404
    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application deleted"}), 200


#Get resources
@app.route("/getresources", methods=["GET"])
def getresources():
    resources = Resource.query.all()
    resources_list = []
    for resource in resources:
        resources_list.append({
            'id': resource.id,
            'name': resource.name,
            'description': resource.description,
            'address': resource.address,
            'phoneNumber': resource.phoneNumber,
            'email': resource.email,
            'website': resource.website,
            'category_id': resource.category_id,
            'lat': resource.lat,
            'lon': resource.lon,
            'tags': resource.tags,
            'img': resource.img
        })
    return jsonify(resources_list), 200

#Get resources by category
@app.route("/getresourcesbycategory/<category_id>", methods=["GET"])
def getresourcesbycategory(category_id):
    resources = Resource.query.filter_by(category_id=category_id).all()
    resources_list = []
    for resource in resources:
        resources_list.append({
            'id': resource.id,
            'name': resource.name,
            'description': resource.description,
            'address': resource.address,
            'phoneNumber': resource.phoneNumber,
            'email': resource.email,
            'website': resource.website,
            'category_id': resource.category_id,
            'lat': resource.lat,
            'lon': resource.lon,
            'tags': resource.tags,
            'img': resource.img
        })
    return jsonify(resources_list), 200


#Get reasource by id
@app.route("/getreasource/<fid>", methods=["GET"])
def getreasource(fid):
    ##Broken
    resource = Resource.query.filter_by(id=fid).first()
    jsonresource = {
        'id': resource.id,
        'name': resource.name,
        'description': resource.description,
        'address': resource.address,
        'phoneNumber': resource.phoneNumber,
        'email': resource.email,
        'website': resource.website,
        'category_id': resource.category_id,
        'lat': resource.lat,
        'lon': resource.lon,
        'tags': resource.tags,
        'img': resource.img
    }
    return jsonify(jsonresource), 200

@app.route("/password/<password>", methods=["GET"])
def getpassword(password):
    if password == "123":
        return jsonify({"message": "good to go"}), 200
    return jsonify({"message": "not good"}), 400