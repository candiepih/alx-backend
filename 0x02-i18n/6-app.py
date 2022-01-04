#!/usr/bin/env python3
"""
This is the main file of the flask application.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    This class is used to configure the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    This function is used to select the language.

    Returns:
        str: The language.
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
        return app.config['BABEL_DEFAULT_LOCALE']
    elif request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    This is the main page of the flask application.

    Returns:
        str: The rendered template.
    """
    return render_template('6-index.html')


def get_user() -> Union[dict, None]:
    """
    This function is used to get the user.

    Returns:
        dict: The user.
    """
    login_as = request.args.get('login_as')
    if login_as and login_as.isdigit():
        return users.get(int(login_as), None)
    return None


@app.before_request
def before_request() -> None:
    """
    This function is used to set the user.

    Returns:
        None
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
