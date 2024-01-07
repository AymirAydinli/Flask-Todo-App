from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize SqlAlchemy
db = SQLAlchemy()

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
