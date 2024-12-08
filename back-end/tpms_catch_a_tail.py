import csv
import threading
import time
import signal
import sys
from datetime import datetime
from track import GPSDataCollector, GPSKMLGenerator, save_kml
import gpsd
import config
from id_classes import IDs

# Global configurations
gps = config.gps
make_csv = config.make_csv
make_kml = config.make_kml
csv_name = config.csv_name or datetime.now().strftime("%Y-%m-%d_%H:%M")
kml_name = config.kml_name or datetime.now().strftime("%Y-%m-%d_%H:%M")
stop_threads = False

# Shared resources
gps_collector = GPSDataCollector()
kml_generator = GPSKMLGenerator(f"{kml_name}.kml")
test = None  # Will be initialized later

# Thread references
thread1 = thread2 = None

# Utility Classes and Functions
class Csv:
    def __init__(self, file):
        self.file = file
        self.start_index = 0
        self.uids_dict = {}

    def process_csv(self):
        with open(self.file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for index, row in enumerate(csv_reader):
                if index >= self.start_index:
                    coords = (float(row['lat']), float(row['lon']))
                    id = row['id']

                    if id not in self.uids_dict:
                        self.uids_dict[id] = IDs(id, row['time'], coords, float(row['rssi']), row['model'])
                    else:
                        self.uids_dict[id].add_instance(row['time'], coords, float(row['rssi']))

                self.start_index = index + 1
            self.start_index += 1


def google_earth_csv_maker():
    """Generates a Google Earth-compatible CSV file."""
    csv_file = f"{csv_name}.csv"
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['id', 'model', 'instance', 'lat', 'lon', 'times', 'rssi']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for instance in test.uids_dict.values():
            for index, i in enumerate(range(instance.count)):
                writer.writerow({
                    'id': instance.id,
                    'model': instance.model,
                    'instance': index + 1,
                    'lat': instance.coords[i][0],
                    'lon': instance.coords[i][1],
                    'times': instance.times[i],
                    'rssi': instance.rssi[i]
                })


def gps_route_run():
    """Continuously collect GPS data."""
    global stop_threads
    retries = 12
    while not stop_threads:
        try:
            gpsd.connect()
            packet = gpsd.get_current()

            if packet.mode >= 2:  # Check for 2D or better fix
                retries = 12
                location = gps_collector.get_location()
                if location:
                    latitude, longitude = location
                    kml_generator.add_point(latitude, longitude)
                    print(f"Added point: {latitude}, {longitude}")
                time.sleep(1)
            else:
                print("GPS is running but has no fix.")
                time.sleep(3)
        except gpsd.GPSDException as e:
            print(f"GPS daemon error: {e}")
            if retries > 0:
                retries -= 1
                time.sleep(5)
            else:
                print("Max retries reached. Continuing without GPS.")
                retries = 12
                time.sleep(5)
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)


def data(socketio=None):
    """Processes CSV data and optionally streams via WebSocket."""
    global stop_threads
    while not stop_threads:
        test.process_csv()
        for obj in test.uids_dict.values():
            if obj.difference_time > 5:
                print(obj)
                if socketio:
                    socketio.emit('data', {'id': obj.id, 'rssi': obj.rssi})
        time.sleep(60)


def start_main():
    """Starts main threads."""
    global thread1, thread2, stop_threads, test
    stop_threads = False
    test = Csv('test.csv')

    if gps:
        signal.signal(signal.SIGINT, signal_handler)
        thread1 = threading.Thread(target=gps_route_run)
        thread2 = threading.Thread(target=data)
        thread1.start()
        thread2.start()
    else:
        thread2 = threading.Thread(target=data)
        thread2.start()


def stop_main():
    """Stops all running threads."""
    global stop_threads
    stop_threads = True
    if thread1 and thread1.is_alive():
        thread1.join()
    if thread2 and thread2.is_alive():
        thread2.join()


def signal_handler(sig, frame):
    """Handles termination signals."""
    global stop_threads
    stop_threads = True
    google_earth_csv_maker()
    save_kml(kml_generator.kml, kml_generator.kml_file_name, kml_generator.coordinates)
    sys.exit(0)
