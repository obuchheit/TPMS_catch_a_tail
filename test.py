import csv
import os
from datetime import datetime
import time
import atexit

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')


class IDs:

  def __init__(self, id, time, coord, rssi, model, code):
    self.id = id
    self.count = 1
    self.times = [time]
    self.coords = [coord]
    self.rssi = [rssi]
    self.model = model
    self.code = code
    self.first_time = (int(time[-7]) * 60) + (int(time[-5]) * 10) + (int(time[-4]))

  
  def add_instance(self, time, coord, rssi):
    self.count += 1
    self.times.append(time)
    self.coords.append(coord)
    self.rssi.append(rssi)
    self.last_time = (int(time[-7]) * 60) + (int(time[-5]) * 10) + (int(time[-4]))
    
    self.difference_time = self.last_time - self.first_time
    print(f'{self.id} has been seen {self.count} times. Last time was {self.last_time}')

  

  def __str__(self):
    return f'ID: {self.id}, Times: {self.times}'
    



'''Loops through csv file from rtl_433 and pushes data into dictionaries'''  
class Csv:

  def __init__(self, file):
    self.file = file
    self.start_index = 0
    self.uids_dict = {}



  def process_csv(self):
    with open('test.csv') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for index, row in enumerate(csv_reader):
        if index >= self.start_index:

          coords = (float(row['lat']), float(row['lon']))
          id = row['id'] 

          if id not in self.uids_dict: 
            self.uids_dict[id] = IDs(id, row['time'], coords, float(row['rssi']), row['model'], int(row['code']))

          else:
            self.uids_dict[id].add_instance(row['time'], coords, float(row['rssi']))

        self.start_index = index + 1
    self.start_index += 1



def main():

  while True:
    test = Csv('test.csv')
    test.process_csv()
    # for obj in test.uids_dict.values():
    #   print(obj)
    
    time.sleep(30)


if __name__=="__main__":
  main()

atexit.register(delete_txt_file)