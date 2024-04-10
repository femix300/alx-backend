#!/usr/bin/env python3
'''Basic Babel setup'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''A config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    '''calls render template on the html file'''
    return render_template('1-index.html')


def get_locale():
    '''
    Determine the best match between supported languages
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run(debug=True)
