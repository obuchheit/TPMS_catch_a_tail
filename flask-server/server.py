from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import threading
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/api/launch', methods=['POST'])
def launch_app():
    config = request.json
    start_main_function(config)


@app.route('/api/stop', methods=['POST'])
def stop_app():
    stop_main_function()
    return jsonify({'message': 'Application stopped'})


if __name__=="__main__": 
    socketio.run(app)