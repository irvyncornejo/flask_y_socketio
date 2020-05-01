from flask import Flask, render_template
from flask_socketio import SocketIO, send
import time

app = Flask(__name__)

#sesion
app.config['SECRET_KEY'] = 'pALABRASECRETA'

#socket
socketio = SocketIO(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

#manejador del evento para los eventos de envio
"""@socketio.on('message')
def handle_message(msg):
    print(f'Message {msg}')
    #reenvio de mensajes mediante la conexión web socket
    send(msg, broadcast = True)
"""
@socketio.on('data')
def read_sensor():
    data_set = [34, 46, 45, 45, 45, 67, 78, 89, 5667, 789, 89]
    #reenvio de mensajes mediante la conexión web socket
    for data in data_set:
        print(data)
        send(data, broadcast = True)
        time.sleep(1.5)
        

if __name__ == '__main__':
    socketio.run(app)

