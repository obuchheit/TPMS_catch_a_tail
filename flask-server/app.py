from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
from threading import Thread
from flask_cors import CORS
import threading
import main
import config
import tpms_catch_a_tail

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

@app.route('/start', methods=['POST'])
def start():
    threading.Thread(target=main.start_main).start()
    return jsonify({"status": "success", "message": "Main function started."})

@app.route('/stop', methods=['POST'])
def stop():
    main.stop_main()
    return jsonify({"status": "success", "message": "Main function stopped."})

# SocketIO Events
@socketio.on('get_data')
def send_data():
    data = main.data()
    emit('data_response', data, broadcast=True)



if __name__=="__main__": 
    socketio.run(app, debug=True)