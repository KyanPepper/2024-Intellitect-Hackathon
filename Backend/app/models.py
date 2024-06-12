from app import db

class Categories(db.Model):
    categories = [
    'Elderly',
    'Youth',
    'People with Disabilities',
    'Homeless',
    'Refugees and Asylum Seekers',
    'Veterans',
    'Recovering Addicts'
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phoneNumber = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    website = db.Column(db.String(100), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    category = db.relationship('Categories', backref=db.backref('applications', lazy=True))


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phoneNumber = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(100), nullable=True)
    tags = db.Column(db.String(500), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    category = db.relationship('Categories', backref=db.backref('resources', lazy=True))
    lon = db.Column(db.Float, nullable=True)
    lat = db.Column(db.Float, nullable=True)
    img = db.Column(db.String(1000), nullable=True)