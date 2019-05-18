from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/rest/*": {"origins": "*"}})


db = SQLAlchemy(app)
db.app = app
db.init_app(app)

from app import routes
