#!/usr/bin/env python3
"""
A simple flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for the Flask app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """
    Get the locale from the request
    """
    if request.args.get('locale'):
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Return a user dictionary if 'login_as' 
    is a valid user ID, otherwise None.
    """
    login_as = request.args.get('login_as')
    if login_as is not None:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except (ValueError, TypeError):
            return None
    return None


def before_request():
    """
    Set the current user in flask.g before each request.
    """
    g.user = get_user()


app.before_request(before_request)

babel.init_app(app, locale_selector=get_locale, user_loader=get_user)


@app.route('/')
def hello_world():
    """
    Render the 5-index.html template
    """
    return render_template('5-index.html')
