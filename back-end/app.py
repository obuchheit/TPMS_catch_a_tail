from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import threading
import config
import tpms_catch_a_tail

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

thread1 = thread2 = None

@app.route('/config', methods=['POST'])
def update_config():
    data = request.json
    for key, value in data.items():
        if hasattr(config, key):
            setattr(config, key, value)
    return jsonify({"message": "Config updated"}), 200

@app.route('/run/start', methods=['POST'])
def start_main():
    global thread1, thread2
    tpms_catch_a_tail.stop_threads = False
    thread1 = threading.Thread(target=tpms_catch_a_tail.gps_route_run, args=(tpms_catch_a_tail.gps_collector, tpms_catch_a_tail.kml_generator))
    thread2 = threading.Thread(target=tpms_catch_a_tail.data)
    thread1.start()
    thread2.start()
    return jsonify({"message": "Main started"}), 200

@app.route('/run/stop', methods=['POST'])
def stop_main():
    tpms_catch_a_tail.stop_main()
    return jsonify({"message": "Main stopped and files generated"}), 200

@socketio.on('connect')
def handle_connect():
    def stream_data():
        while not tpms_catch_a_tail.stop_threads:
            if tpms_catch_a_tail.test is None:
                print("Test instance is not initialized.")
                socketio.sleep(1)
                continue

            for obj in tpms_catch_a_tail.test.uids_dict.values():
                if obj.difference_time > 5:
                    socketio.emit('data', {'id': obj.id, 'model': obj.model})
            socketio.sleep(60)

        # Notify clients that streaming has stopped
        socketio.emit('data', {'message': 'Data stream has stopped.'})

    socketio.start_background_task(stream_data)


if __name__ == '__main__':
    socketio.run(app, debug=True)
