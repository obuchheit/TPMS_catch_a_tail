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

def signal_handler(sig, frame):
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


  '''Makes a csv file for google earth'''
def google_earth_csv_maker():

  csv_file = 'google_earth.csv' #change to a var name

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


'''Intializes rtl_433'''
def start_rtl_433():
  #os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')
  pass

  



def continuously_run(gps_collector, kml_generator):
    """Continuously collect GPS data."""
    retries = 12
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

            # Optionally, reset retries if you want to keep trying later
            retries = 12  
            time.sleep(5)  # Wait a bit before the next loop iteration

      except Exception as e:
          print(f"An unexpected error occurred: {e}")
          time.sleep(5)  # Wait before retrying in case of unexpected errors


def data():
  while not stop_threads:
    test.process_csv()
    '''Doesn't work'''
    for obj in test.uids_dict.values():
      if obj.difference_time > 5:
        print(obj)

    time.sleep(60)
  # google_earth_csv_maker()




if __name__=="__main__":
  
  #start_rtl_433()
  test = Csv('test.csv') #change argument of Csv after once finished

  # Initialize GPS data collector and KML generator
  gps_collector = GPSDataCollector()
  kml_generator = GPSKMLGenerator("my_gps_data.kml")

  '''Adds listeners to execute specific code when the program is terminated.'''
  signal.signal(signal.SIGINT, signal_handler)
 

  thread1 = threading.Thread(target=continuously_run, args=(gps_collector, kml_generator))
  thread2 = threading.Thread(target=data)
  # Start threads
  thread1.start()
  thread2.start()


  thread1.join()
  thread2.join()