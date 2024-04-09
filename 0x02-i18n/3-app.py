#!/usr/bin/env python3
"""
Basic Flask App
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

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
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('2-index.html', home_title=_('home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
