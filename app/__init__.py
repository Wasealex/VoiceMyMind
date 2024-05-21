"""
Initializes the Flask application.
"""
from flask import Flask
import secrets
import string

def create_app():
    """
    Creates a Flask application instance with a randomly generated secret key.
    
    Returns:
        Flask: The created Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32))
    from .routes import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/myjournal')
    app.register_blueprint(auth, url_prefix='/myjournal')
    

    return app
