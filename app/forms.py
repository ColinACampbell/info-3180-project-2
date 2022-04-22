# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired

class CreateUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    emailaddress = StringField('emailaddress', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    bio = TextAreaField('bio', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'Images only!'])])

class AddCarForm(FlaskForm):
    make = StringField('make', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    colour = StringField('colour', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    transmission = SelectField('Transmission Type', choices=[
                         ('Manual', 'Manual'), ('Automatic', 'Automatic')], validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    cartype = SelectField('Transmission Type', choices=[
                         ('SUV', 'SUV'), ('Sedan', 'Sedan'),('Hatchback', 'Hatchback'), ('Pickup Truck', 'Pickup Truck'),
                         ('Coupe', 'Coupe'), ('Convertible', 'Convertible'),('Minivan', 'Minivan'),
                         ('Crossover', 'Crossover'), ('Van', 'Van')], validators=[DataRequired()])
    carphoto = FileField('carphoto', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'Please upload images only.'])])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
