from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user


main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    return render_template('second.html')


@main.route('/payment')
def payment():
    return render_template('payment.html')


@main.route('/account')
def index():
    return render_template('index.html')


@main.route('/account/<filename>')
def block_page(filename):
    return render_template(f'{filename}.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
