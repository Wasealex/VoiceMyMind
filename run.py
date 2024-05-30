"""
Runs the main application loop.
"""
from flask_socketio import SocketIO
from app import create_app

app = create_app()
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)