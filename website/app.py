'''

This is the main source code for the website.

'''

# Import libraries
from flask import Flask, render_template

from website.blueprints.page.views import page


def create_app(settings_override=None):
    '''

    This is the main function for the site.

    return: Flask site

    '''

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    # Register blueprints
    app.register_blueprint(page)

    return app
