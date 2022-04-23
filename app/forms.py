# Add any form classes for Flask-WTF here
import email
from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class CreateUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    bio = TextAreaField('bio', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png', 'jpeg', 'Images only!'])])

    class Meta:
        csrf = False


class AddCarForm(FlaskForm):
    make = StringField('make', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    colour = StringField('colour', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    transmissionType = StringField('transmissionType', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    carType = StringField('carType', validators=[DataRequired()])
    carPhoto = FileField('carPhoto', validators=[FileRequired(), FileAllowed(
        ['jpg', 'png', 'jpeg', 'Please upload images only.'])])

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    class Meta:
        csrf = False
