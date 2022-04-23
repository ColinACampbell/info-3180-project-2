"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import json
from pkg_resources import require
from flask import render_template, request, jsonify, send_file, g
import jwt
from app.models import User, Favourite, Car
import os
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, CreateUserForm, AddCarForm
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from functools import wraps
from datetime import date


def createToken(user):
    return jwt.encode({'id': user.id}, app.config['SECRET_KEY'],
                      algorithm='HS256')


# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # or request.cookies.get('token', None)
        auth = request.headers.get('Authorization', None)

        if not auth:
            return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

        parts = auth.split()

        if parts[0].lower() != 'bearer':
            return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
        elif len(parts) == 1:
            return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
        elif len(parts) > 2:
            return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

        token = parts[1]
        try:
            payload = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
        except jwt.DecodeError:
            return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

        g.current_user = user = payload
        return f(*args, **kwargs)

    return decorated

###
# Routing for your application.
###


@app.route('/')
@requires_auth
def index():
    return send_file(os.path.join('../dist/', 'index.html'))

###
# The functions below should be applicable to all Flask apps.
###


@app.route("/api/auth/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for("index"))


@app.route("/api/auth/login", methods=["POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
                encoded_jwt = createToken(user)
                return {"message": [], "token": encoded_jwt}
            else:
                return {"message": ['Incorrect credentials']}
    else:
        return {
            "message": form_errors(form)
        }


@app.route('/api/register', methods=['POST'])
def register():
    createUserForm = CreateUserForm()
    if (createUserForm.validate_on_submit()):

        username = createUserForm.username.data
        password = createUserForm.password.data
        name = createUserForm.name.data
        email = createUserForm.email.data
        location = createUserForm.location.data
        bio = createUserForm.bio.data
        photo = createUserForm.photo.data

        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(photo.filename))
        photo.save(file_path)

        if User.query.filter_by(username=username).first() == None and User.query.filter_by(email=email).first() == None:

            user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'), name=name,
                        email=email, location=location, biography=bio, photo=file_path, date_joined=date.today())
            db.session.add(user)
            db.session.commit()

            encoded_jwt = createToken(user)

            return {"message": [], "token": encoded_jwt}
        else:
            return {"message": ['User exists']}
    else:
        return {
            "message": form_errors(createUserForm)
        }


@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/cars/<car_id>', methods=['GET'])
def cardetail(car_id):
    return jsonify(Car.query.filter_by(id=car_id).first())

@app.route('/api/cars', methods=['GET'])
def returncars():
    return  jsonify(Car.query.all())


@app.route('/api/cars', methods=['POST'])
@requires_auth
def addcars():

    addCarForm = AddCarForm()

    if request.method == 'POST':
        if addCarForm.validate_on_submit():

            # Collect the data from the form
            make = addCarForm.make.data
            description = addCarForm.description.data
            model = addCarForm.model.data
            colour = addCarForm.colour.data
            year = addCarForm.year.data
            transmission = addCarForm.transmissionType.data
            carType = addCarForm.carType.data
            price = addCarForm.price.data
            carPhoto = addCarForm.carPhoto.data

            filename  = os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(carPhoto.filename))

            carPhoto.save(filename)

            mycar = Car(g.current_user['id'],description,make,model,colour,year,transmission,carType,price,filename)
            db.session.add(mycar)
            db.session.commit()

            return jsonify(Car.query.filter_by(id=mycar.id).first())
        else:
            return {
                'message': form_errors(addCarForm)
            }


@app.route('/api/cars/{car_id}/favourites', methods=['POST'])
def favcar():
    return car


@app.route('/api/searh', methods=['GET'])
def searchcars():
    return car


@app.route('/api/users/{user_id}', methods=['GET'])
def userdetails():
    return car


@app.route('/api/users/{user_id}/favourites', methods=['GET'])
def userfavs():
    return car

# Here we define a function to collect form errors from Flask-WTF
# which we can later use


def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            )
            error_messages.append(message)

    return error_messages


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
