from flask import flash

def valid_password_flash(password, passwordConfirm):
    if len(password) < 5:
        flash('password must be greater than 4 characters', category='error')
    elif password != passwordConfirm:
        flash('passwords don\'t match', category='error')
    else:
        return True
    return False

def valid_username_flash(username):
    if len(username) < 3:
        flash('username must be greater than 3 characters', category='error')
    elif len(username) > 25:
        flash('username must be less than 25 characters', category='error')
    else:
        return True
    return False

def valid_signup_flash(username, password, passwordConfirm):
    if valid_username_flash(username) and valid_password_flash(password, passwordConfirm):
        flash('account created successfuly', category='success')
        return True
    else:
        return False