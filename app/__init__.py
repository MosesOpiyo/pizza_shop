from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy

from config import config_options

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(config_options['development'])
db.init_app(app)