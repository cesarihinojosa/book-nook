from flask import flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

def valid_password_flash(password, passwordConfirm):
    if len(password) < 5:
        flash('password must be greater than 4 characters', category='error')
    elif password != passwordConfirm:
        flash('passwords don\'t match', category='error')
    else:
        return True
    return False

def valid_username_flash(username):
    user = User.query.filter_by(username=username).first()
    if user:
        flash('username already exists', category='error')
    elif len(username) < 3:
        flash('username must be greater than 3 characters', category='error')
    elif len(username) > 25:
        flash('username must be less than 25 characters', category='error')
    else:
        return True
    return False

def valid_signup_flash(username, password, passwordConfirm):
    if valid_username_flash(username) and valid_password_flash(password, passwordConfirm):
        return True
    else:
        return False
    
def valid_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in successfully', category='success')
            return True
        else:
            flash('Username or password is incorrect', category='error')
    else:
        flash('Username or password is incorrect', category='error')
    return False