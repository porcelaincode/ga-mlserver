from flask import Flask, render_template
from flask_socketio import send, SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('connect')
def test_connect():
    emit('status', {'date': datetime.now(), 'status': True})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    send(message, namespace='/desktop-app')