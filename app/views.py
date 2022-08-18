from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
