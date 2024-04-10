#!/usr/bin/env python3
'''Basic Babel setup'''
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''A config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    '''calls render template on the html file'''
    return render_template('4-index.html', home_title=_('home_title'),
                           home_header=_('home_header'))


@babel.localeselector
def get_locale():
    '''
    Determine the best match between supported languages
    '''
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
