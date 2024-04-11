#!/usr/bin/env python3
'''Basic Babel setup'''
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

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


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match between supported languages
    """
    locale_from_url = request.args.get('locale')
    if locale_from_url and locale_from_url in app.config['LANGUAGES']:
        return locale_from_url

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    locale_from_header = request.headers.get('locale', '')
    if locale_from_header in app.config['LANGUAGES']:
        return locale_from_header

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    '''Support for timezones'''
    try:
        time_zone = request.args.get('timezone')
        if time_zone:
            pytz.timezone(time_zone)
            return time_zone

        if g.user:
            user_timezone = g.user.get('timezone')
            if user_timezone:
                pytz.timezone(user_timezone)
                return user_timezone

    except pytz.exceptions.UnknownTimeZoneError:
        pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


if __name__ == '__main__':
    app.run(debug=True)
