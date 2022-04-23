"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from flask import render_template, request, jsonify, send_file
from app.models import User, Favourite, Car
import os
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm, CreateUserForm, AddCarForm
from app.models import User
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
###
# Routing for your application.
###


@app.route('/')
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
    if request.method == "POST" and form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
                login_user(user)
                flash("Successful login! ", "success")
                return redirect(url_for(""))
            else:
                flash("Login denied. Try again!", "danger")

            return redirect(url_for("index"))
    return render_template("login.html", form=form)


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
            user = User(username=username, password=password, name=name,
                        email=email, location=location, biography=bio, photo=file_path)
            db.session.add(user)
            db.session.commit()

            return {"message": ['Ok']} 
        else : 
            return {"message": ['User Exists']} 
    else:
        return {
            "message": form_errors(createUserForm)
        }

    return {"message": []}

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/cars', methods=['GET'])
def returncars():
    return car


@app.route('/api/cars', methods=['POST'])
def addcars():
    addcar = AddCarForm()

    if request.method == 'POST':
        if addcar.validate_on_submit():

            # Collect the data from the form
            make = request.addcar['make']
            description = request.addcar['description']
            model = request.addcar['model']
            colour = request.addcar['colour']
            year = request.addcar['year']
            transmission = request.addcar['transmission']
            cartype = request.addcar['cartype']
            price = request.addcar['price']
            file = request.files['photo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            mycar = Car(make, description, model, colour, year,
                        transmission, cartype, price, filename)
            db.session.add(mycar)
            db.session.commit()

            flash('New car has been successfully added!', 'success')
            return redirect(url_for(''))
        else:
            flash("Error!")
            return render_template('', form=addcar)
    elif request.method == 'GET':
        return render_template('', form=addcar)


@app.route('/api/cars/{car_id}', methods=['GET'])
def cardetail():
    return car


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
