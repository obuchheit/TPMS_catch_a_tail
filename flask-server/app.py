from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from threading import Thread
from flask_cors import CORS
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('api/config', methods=['POST'])
def update_config():
    new_config = request.json
    config.gps = new_config.get('gps', config.gps)
    config.make_csv = new_config.get('make_csv', config.make_csv)
    config.make_kml = new_config.get('make_kml', config.make_kml)
    config.csv_name = new_config.get('csv_name', config.csv_name)
    config.kml_name = new_config.get('kml_name', config.kml_name)
    return jsonify({"messsage": "Configuration updated", "config": new_config})


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