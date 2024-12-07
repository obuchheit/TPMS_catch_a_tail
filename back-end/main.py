from flask import Flask, render_template
import time
from flask_socketio import SocketIO, emit
from tpms_catch_a_tail import Csv, stop_threads
import config

app = Flask(__name__)
socketio = SocketIO(app)

test = Csv('test.csv')

def data():
  while not stop_threads:
    test.process_csv()
    '''Doesn't work'''
    for obj in test.uids_dict.values():
      if obj.difference_time > 5:
        print(obj)

    time.sleep(60)

if __name__ == '__main__':
    socketio.run(app, debug=True)