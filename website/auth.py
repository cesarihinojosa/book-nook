from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import validate
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if validate.valid_login(username, password):
            user = User.query.filter_by(username=username).first()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        if validate.valid_signup_flash(username, password, passwordConfirm):
            new_user = User(username=username, first_name=first_name, password=generate_password_hash(password, method='pbkdf2:sha1'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created successfuly', category='success')
            user = User.query.filter_by(username=username).first()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


