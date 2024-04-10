#!/usr/bin/env python3
'''Basic Babel setup'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''A config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    '''
    a get_user function that returns a user dictionary or None if
    the ID cannot be found or if login_as was not passed.
    '''
    login_as = request.args.get('login_as')
    if login_as:
        user = users.get(int(login_as))
        return user
    return None


@app.before_request
def before_request():
    '''
    a before_request function and use the app.before_request decorator
    to make it be executed before all other functions.
    '''
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    '''calls render template on the html file'''
    return render_template('5-index.html')


# @babel.localeselector
def get_locale() -> str:
    '''
    Determine the best match between supported languages
    '''
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


if __name__ == '__main__':
    app.run(debug=True)