from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# ==== App setup ==== #

app = Flask(__name__, static_url_path='')

app.config.from_object('app.config.Config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# ==== Blueprint setup ==== #

from app import main, auth  # noqa E402
app.register_blueprint(main.main)
app.register_blueprint(auth.auth)

login_manager.login_view = 'auth.login'
