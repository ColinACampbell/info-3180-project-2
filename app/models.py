import string
from xmlrpc.client import DateTime
from app import db
from werkzeug.security import generate_password_hash
from datetime import date
from dataclasses import dataclass


@dataclass
class Car(db.Model):
    id: int
    userId: int
    description: string
    make: string
    model: string
    color:  string
    year: int
    transmission:  string
    car_type: string
    price: int
    photo: string

    __tablename__ = 'app_cars'

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


@dataclass
class Favourite(db.Model):

    id:int
    carId:int

    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    carId = db.Column(db.Integer)

    def __init__(self, userId, carId):
        self.userId = userId
        self.carId = carId


@dataclass
class User(db.Model):

    __tablename__ = 'app_users'

    id :int
    username :string
    name:string
    email :string
    location:string
    biography :string
    photo:string
    date_joined : DateTime

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(300))
    name = db.Column(db.String(80))
    email = db.Column(db.String(100))
    location = db.Column(db.String(500))
    biography = db.Column(db.String(500))
    photo = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)

    def _init__(self, username, password, name, email, location, biography, photo, date_joined):
        self.username = username
        self.password = generate_password_hash(
            password, method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = date_joined
