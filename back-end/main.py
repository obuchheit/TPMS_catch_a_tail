from flask import Flask, render_template
import time
from datetime import datetime
from flask_socketio import SocketIO, emit
from tpms_catch_a_tail import Csv, stop_threads
import config

app = Flask(__name__)
socketio = SocketIO(app)




if __name__ == '__main__':
    socketio.run(app, debug=True)