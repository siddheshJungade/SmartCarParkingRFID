from flask import Flask
from flask_cors import CORS
from model.parking_model import Parking_model
from mfrc522 import SimpleMFRC522
from flask_socketio import *
import time 



start = {}
counter = 0
counterIN = 0
counterOut = 0

off = 1 

reader = SimpleMFRC522()
obj = Parking_model()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,cors_allowed_origins="*")
CORS(app)


@socketio.on('message')
def handleMessage(msg):
    print(msg)
    emit('message', msg, broadcast=True)
    return None




if __name__ == '__main__':
    socketio.run(app, debug=True)

from controller.parking_controller import *
