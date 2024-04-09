#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext
import pytz
from datetime import datetime

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

# Get timezone function
@babel.timezoneselector
def get_timezone():
    # Check if timezone is specified in URL parameters
    tzname = request.args.get('timezone')
    if tzname:
        try:
            pytz.timezone(tzname)
            return tzname
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    # Check if user is logged in and has a preferred timezone
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    # Default to UTC
    return 'UTC'

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
    
    timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(timezone)).strftime('%b %d, %Y, %I:%M:%S %p')

    return render_template('7-index.html', welcome_message=welcome_message, timezone=timezone, current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
