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

    last_time = (int(time[-7]) * 60) + (int(time[-5]) * 10) + (int(time[-4]))
    self.difference_time = last_time - self.first_time

    if self.difference_time > 15:
      pass
  

  def __str__(self):
    return f'ID: {self.id}, Times: {self.times}'
    

  '''Reads a text file to give the csv_reader a start index'''
def read_start_index():
  if os.path.exists('start_index.txt'):
    with open('start_index.txt', 'r') as f:
      return int(f.read().strip())
  return 0

  '''Saves the last index of the csv_reader for loop.'''
def save_last_index(index):
  with open('start_index.txt', 'w') as f:
    f.write(str(index))


'''Deletes the start_index file upon exiting the program'''
def delete_txt_file():
  os.system("rm start_index.txt")



'''Loops through csv file from rtl_433 and pushes data into dictionaries'''  
def process_csv(uids_dict):
  startIndex = read_start_index()
  with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for index, row in enumerate(csv_reader):
      if index >= startIndex:
        coords = (float(row['lat']), float(row['lon']))
        id = row['id']

        '''Adds new identifiers to the IDs class'''
        if id not in uids_dict:
          uids_dict[id] = IDs(id, row['time'], coords, float(row['rssi']), row['model'], int(row['code']))

          '''Appends new data if the same identifier is seen'''
        else:
          uids_dict[id].add_instance(row['time'], coords, float(row['rssi']))

        save_last_index(index + 1)



def main():
  uids_dict = {}

  while True:
    process_csv(uids_dict)
    
    for obj in uids_dict.values():
      pass
      #print(obj)
    
    time.sleep(30)


if __name__=="__main__":
  main()

atexit.register(delete_txt_file)