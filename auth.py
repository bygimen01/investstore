from flask import Blueprint, render_template
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/registration')
def signup():
    return render_template('registration.html')


@auth.route('/logout')
def logout():
    return 'Logout'
