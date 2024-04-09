#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext

app = Flask(__name__)

# Config class
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Get user function
def get_user(user_id):
    return users.get(user_id)

# Get locale function
@babel.localeselector
def get_locale():
    # Check if locale is specified in URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Check if user is logged in and has a preferred locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Check if locale is specified in request headers
    locale = request.headers.get('Accept-Language')
    if locale:
        best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
        if best_match:
            return best_match
    
    # If none of the above conditions are met, resort to default locale
    return app.config['BABEL_DEFAULT_LOCALE']

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
    return render_template('6-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

