from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import *


auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/welcome')
def welcome():
    return render_template('welcome.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            flash('Logged in successfully.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.myjournal'))
        else:
            flash('Invalid email or password.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.welcome'))


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        else:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password_hash=generate_password_hash(password1, method='scrypt', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            flash('account created', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.myjournal'))
        
    return render_template("sign_up.html", user=current_user)
