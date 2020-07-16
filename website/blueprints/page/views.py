'''

This is the page blueprints.

'''

# Import libraries
from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


# Render Template
@page.route('/')
def home():
    return render_template('page/home.html')
