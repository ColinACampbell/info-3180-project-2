from app import db


class Car(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    description = db.Column(db.String(300))
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    color = db.Column(db.String(80))
    year = db.Column(db.String(80))
    transmission = db.Column(db.String(80))
    car_type = db.Column(db.String(80))
    price = db.Column(db.Float)
    photo = db.Column(db.String(100))

    def __init__(self, userId, description, make, model, color, year,
                 transmission, car_type, price, photo):
        self.userId = userId
        self.description = description
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo


class Favourites(db.Model):

    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    carId = db.Column(db.Integer)

    def __init__(self, userId, carId):
        self.userId = userId
        self.carId = carId


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(100))
    location = db.Column(db.String(500))
    biography = db.Column(db.String(500))
    photo = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)

    def _init__(self, username, password, name, email, location, biography, photo):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        # date_joined = db.Column(db.DateTime) set the date joined when the constructor is called
