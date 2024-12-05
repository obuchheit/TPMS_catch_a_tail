import csv
import os
import time
from id_classes import IDs
import signal
import threading
from track import GPSDataCollector, GPSKMLGenerator, save_kml
import gpsd
import sys

stop_threads = False
threads = []
gps_collector = None
kml_generator = None
test = None

def signal_handler(sig, frame):
    """Handle termination signals."""
    global stop_threads
    stop_threads = True
    google_earth_csv_maker()
    save_kml(kml_generator.kml, kml_generator.kml_file_name, kml_generator.coordinates)
    sys.exit(0)

class Csv:
    def __init__(self, file):
        self.file = file
        self.start_index = 0
        self.uids_dict = {}
        self.uids_lst = []

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
    """Create a CSV file for Google Earth."""
    csv_file = 'google_earth.csv'

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

def continuously_run():
    """Continuously collect GPS data."""
    retries = 12
    global gps_collector, kml_generator
    while not stop_threads:
        try:
            gpsd.connect()
            packet = gpsd.get_current()
            if packet.mode >= 2:  # Check for 2D or better fix
                retries = 12  # Reset retries after a successful connection
                location = gps_collector.get_location()
                if location:
                    latitude, longitude = location
                    kml_generator.add_point(latitude, longitude)  # Only store coordinates
                    print(f"Added point: {latitude}, {longitude}")

                time.sleep(1)  # Add a sleep to avoid overwhelming the GPS daemon
            else:
                print("GPS is running but has no fix.")
                time.sleep(3)
        except gpsd.GPSDException as e:
            print(f"GPS daemon is not running or cannot be accessed: {e}")
            if retries > 0:
                print(f"Retrying in 5 seconds... ({retries} retries left)")
                retries -= 1
                time.sleep(5)  # Wait before retrying
            else:
                print("Max retries reached. Continuing without GPS.")
                retries = 12
                time.sleep(5)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(5)

def data():
    """Process CSV data."""
    global test
    while not stop_threads:
        test.process_csv()
        for obj in test.uids_dict.values():
            if obj.difference_time > 5:
                print(obj)
        time.sleep(60)

def start_main_function(config):
    """Start the main application."""
    global gps_collector, kml_generator, test, threads, stop_threads

    # Reset stop flag
    stop_threads = False

    # Initialize components based on configuration
    test = Csv(config.get('csv_file', 'test.csv'))
    gps_collector = GPSDataCollector()
    kml_generator = GPSKMLGenerator(config.get('kml_file', 'my_gps_data.kml'))

    # Add signal handler for graceful termination
    signal.signal(signal.SIGINT, signal_handler)

    # Create and start threads
    thread1 = threading.Thread(target=continuously_run, daemon=True)
    thread2 = threading.Thread(target=data, daemon=True)
    threads = [thread1, thread2]
    for thread in threads:
        thread.start()
    print("Application started.")

def stop_main_function():
    """Stop the main application."""
    global stop_threads, threads
    stop_threads = True

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    threads = []
    print("Application stopped.")
