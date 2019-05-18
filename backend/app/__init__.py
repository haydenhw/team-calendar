from flask import Flask, render_template

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html'), 200
