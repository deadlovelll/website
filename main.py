from flask import Flask, render_template
from markupsafe import escape
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('main.html')

@socketio.on('location')
def handle_location(data):
    emit('location', {'latitude': data['latitude'], 'longitude': data['longitude']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
