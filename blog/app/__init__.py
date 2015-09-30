from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from .main import main as main_blueprint


# bootstrap = Bootstrap()
# db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

app.register_blueprint(main_blueprint)