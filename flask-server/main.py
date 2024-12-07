import threading
import time
import signal
import sys
import gpsd
from datetime import datetime
from config import gps, make_csv, make_kml, csv_name, kml_name
from track import GPSDataCollector, GPSKMLGenerator, save_kml
from id_classes import IDs
import csv

# Global variables
stop_threads = False
threads = []
gps_collector = None
kml_generator = None

# Initialize filenames with fallback
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
csv_file = csv_name if csv_name else f"{current_time}.csv"
kml_file = kml_name if kml_name else f"{current_time}.kml"


class CsvProcessor:
    """Handles CSV data processing."""
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
                    uid = row['id']

                    if uid not in self.uids_dict:
                        self.uids_dict[uid] = IDs(uid, row['time'], coords, float(row['rssi']), row['model'])
                    else:
                        self.uids_dict[uid].add_instance(row['time'], coords, float(row['rssi']))

                self.start_index = index + 1
        self.start_index += 1


def continuously_run():
    """Collects GPS data and updates the KML generator."""
    retries = 12
    while not stop_threads:
        try:
            gpsd.connect()
            packet = gpsd.get_current()

            if packet.mode >= 2:  # Check for 2D or better fix
                location = gps_collector.get_location()
                if location:
                    latitude, longitude = location
                    kml_generator.add_point(latitude, longitude)
                    print(f"Added GPS point: {latitude}, {longitude}")
                time.sleep(1)
            else:
                print("No GPS fix. Retrying...")
                time.sleep(3)
        except gpsd.GPSDException as e:
            if retries > 0:
                retries -= 1
                print(f"GPS error: {e}. Retrying ({retries} attempts left)...")
                time.sleep(5)
            else:
                print("GPS failed. Continuing without GPS.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)


def data_processor_loop(csv_processor):
    """Processes CSV data periodically."""
    while not stop_threads:
        csv_processor.process_csv()
        # Implement logic for handling processed CSV data
        time.sleep(60)


def google_earth_csv_maker(csv_processor):
    """Creates a Google Earth CSV from the processed data."""
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['id', 'model', 'instance', 'lat', 'lon', 'times', 'rssi']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for instance in csv_processor.uids_dict.values():
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


def start_threads():
    """Start all necessary threads."""
    global threads, gps_collector, kml_generator

    if gps:
        gps_collector = GPSDataCollector()
        kml_generator = GPSKMLGenerator(kml_file)
        threads.append(threading.Thread(target=continuously_run))

    csv_processor = CsvProcessor('test.csv')  # Replace with your actual file
    threads.append(threading.Thread(target=data_processor_loop, args=(csv_processor,)))

    for thread in threads:
        thread.start()


def stop_threads_signal_handler(sig, frame):
    """Stop threads gracefully on signal."""
    global stop_threads
    stop_threads = True
    for thread in threads:
        thread.join()
    if gps:
        save_kml(kml_generator.kml, kml_generator.kml_file_name, kml_generator.coordinates)
    google_earth_csv_maker(CsvProcessor('test.csv'))  # Replace with your actual file
    sys.exit(0)


def start_main():
    """Main entry point for starting processes."""
    signal.signal(signal.SIGINT, stop_threads_signal_handler)
    start_threads()


def stop_main():
    """Stop processes programmatically."""
    global stop_threads
    stop_threads = True
    for thread in threads:
        thread.join()



