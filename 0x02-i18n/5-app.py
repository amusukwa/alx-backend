#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, g
from flask_babel import Babel, _, gettext

app = Flask(__name__)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Config class
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

# Get locale function
@babel.localeselector
def get_locale():
    # Check if locale parameter is present in the request URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    
    # If not present or not supported, resort to default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Get user function
def get_user(user_id):
    return users.get(user_id)

# Before request function
@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None

@app.route('/')
def index():
    if g.user:
        welcome_message = gettext('You are logged in as %(username)s.') % {'username': g.user['name']}
    else:
        welcome_message = gettext('You are not logged in.')
    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
