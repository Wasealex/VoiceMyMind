"""
Initializes the Flask application.
"""
from datetime import datetime
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO  # Import SocketIO
import speech_recognition as sr
import secrets
import string

db = SQLAlchemy()
socketio = SocketIO()  # Initialize SocketIO

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'voicemymind'
DB_PASSWORD = 'VoiceMyMind'
DB_NAME = 'voice_database'

SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    socketio.init_app(app)  # Initialize SocketIO with the app

    from .routes import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/myjournal')
    app.register_blueprint(auth, url_prefix='/')

    from app.models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    with app.app_context():
        db.create_all()

    @app.template_filter('datetime')
    def jinja2_datetime_filter(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M')

    return app