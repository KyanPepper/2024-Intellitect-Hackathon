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
    name = db.Column(db.String(100), nullable=False)


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', backref=db.backref('applications', lazy=True))


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Categories', backref=db.backref('resources', lazy=True))
    lon = db.Column(db.Float, nullable=True)
    lat = db.Column(db.Float, nullable=True)
    img = db.Column(db.String(1000), nullable=True)