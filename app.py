from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = ['secret!']
socketio = SocketIO(app)

@app.route('/')
def index() -> None:
    return render_template('index.html')

@socketio.on('message')
def handle_message(message: str) -> None:
    emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
