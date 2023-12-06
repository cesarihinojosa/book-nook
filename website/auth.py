from flask import Blueprint, render_template, request, flash
from website import validate

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        if validate.valid_signup_flash(username, password, passwordConfirm):
            print('success')#add user to db

    return render_template("sign_up.html")


