"""
Runs the Flask application with SocketIO support.

This script creates the Flask application instance using the `create_app()` function from the `app` module, and then runs the application using the `socketio.run()` method. The application is run in debug mode, which enables features like automatic reloading when code changes.
"""
"""
Runs the main application loop.
"""
from flask_socketio import SocketIO
from app import create_app

app = create_app()
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)