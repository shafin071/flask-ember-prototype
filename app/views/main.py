from flask import Blueprint
from flask import render_template


main_view = Blueprint('main', __name__)

@main_view.route("/")
def home():
    return render_template('home.html')

@main_view.route("/about")
def about():
    return render_template('about.html')