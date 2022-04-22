"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db, login_manager
from flask import render_template, request, jsonify,url_for, send_file, redirect,flash
import os
from app import app 
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm,CreateUserForm, PicForm,AddCarForm
from app.models import UserProfile
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

@app.route("/api/auth/login", methods=[ "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data

            user = UserProfile.query.filter_by(username=username).first()

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
    createuser = CreateUserForm()
   
    if request.method == 'POST':
        createuser.username.data = request.form['username']
        createuser.password.data = request.form['password']
        createuser.firstname.data = request.form['firstname']
        createuser.lastname.data = request.form['lastname']
        createuser.emailaddress.data = request.form['emailaddress']
        createuser.location.data = request.form['location']
        createuser.bio.data = request.form['bio']
        createuser.photo.data = request.files['photo']
        
        if createuser.validate_on_submit():
            username = createuser.username.data
            password = createuser.password.data
            firstname = createuser.firstname.data
            lastname = createuser.lastname.data
            emailaddress = createuser.emailaddress.data
            location = createuser.location.data
            bio = createuser.bio.data
            photo = createuser.profile_photo.data

            filename = secure_filename(photo.filename)
            dbuser = UserProfile(username, password, firstname, lastname, emailaddress, location, bio, filename)
            db.session.add(dbuser)
            db.session.commit()
            profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            Formdata = {
            "message": "File upload was successful!",
            "filename": filename,
            }
            return jsonify(formdata=formdata)
        else:
            errordata = {
            "errors": [{"filename":form_errors(createuser)}]
        }
        return jsonify(errordata=errordata)


            
    
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

            mycar = Car(make, description, model, colour, year, transmission, cartype,price, filename)
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
    app.run(debug=True,host="0.0.0.0",port="8080")