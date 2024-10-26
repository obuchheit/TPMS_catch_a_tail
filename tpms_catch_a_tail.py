import csv
import os
import time
from id_classes import IDs
import signal
import threading

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
  def google_earth_csv_maker(signum, frame):

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

  

def data():
  while True:
    test.process_csv()
    '''Doesn't work'''
    # for obj in test.uids_dict.values():
    #   print(obj)
    time.sleep(60)



if __name__=="__main__":
  
  #start_rtl_433()
  #time.sleep(120)
  test = Csv('test.csv') #change argument of Csv after once finished

  '''Adds listeners to execute specific code when the program is terminated.'''
  signal.signal(signal.SIGINT, Csv.google_earth_csv_maker)
  signal.signal(signal.SIGTERM, Csv.google_earth_csv_maker)
  data()


 
  


