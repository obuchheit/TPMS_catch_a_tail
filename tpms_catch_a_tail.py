import csv
import os
import time
import configparser
from id_classes import IDs
from route_generator import RouteMaker
import sys
import signal

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



  def google_earth_csv_maker(self):

    csv_file = 'google_earth.csv' #change to a var name

    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['id', 'model', 'count', 'coordinates', 'times', 'rssi']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()

        for instance in self.uids_dict.values():
          for i in range(instance.count):
            writer.writerow({
              'ID': instance.id,
              'Model': instance.model,
              'Count': instance.count,
              'Coordinates': f"{instance.coordinates[i][0]},{instance.coordinates[i][1]}",
              'Times': instance.times[i],
              'RSSI': instance.rssi
            })
            
        


'''Intializes rtl_433'''
def start_rtl_433():
  os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')


def main():
  while True:
    '''Adds listeners to execute specific code when the program is terminated.'''
    signal.signal(signal.SIGINT, RouteMaker.create_kml)
    signal.signal(signal.SIGTERM, RouteMaker.create_kml)

    try:
      test.process_csv()
      for obj in test.uids_dict.values():
        print(obj)
      time.sleep(60)
    except KeyboardInterrupt:
      '''Creates kml file of the route upon program termination'''
      RouteMaker.create_kml()



if __name__=="__main__":
  #start_rtl_433()
  time.sleep(120)
  test = Csv('test.csv') #change argument of CSv after once finished
  main()
