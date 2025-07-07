from flask import Blueprint, render_template

my_blueprint = Blueprint('my_blueprint', __name__, template_folder='templates')

@my_blueprint.route('/')
def home():
    return render_template('index.html')