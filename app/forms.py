from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])
    biography = TextAreaField('biography', validators=[InputRequired()])
    userPhoto = FileField('userPhoto', validators=[FileRequired(FileAllowed(['jpg', 'png', 'jpeg', 'Images only!']))])
