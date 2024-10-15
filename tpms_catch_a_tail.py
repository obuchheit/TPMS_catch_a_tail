import csv
import os
from datetime import datetime
import time
import atexit

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

ids = {}


class IDs:
  def __init__(self, id):
    self.id = id
  
  def add_instance(self, id, time, coords, rssi):
    self.id['count'] += 1
    self.id['times'].append(time)
    self.id['coords'].append(coords)
    self.id['RSSI'].append(rssi)
    print(self.id)

  def __str__(self):
    return f'{self. id}'



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
# def delete_txt_file():
#   os.system("rm start_index.txt")



'''Loops through csv file from rtl_433 and pushes data into dictionaries'''  
def Main():
  startIndex = read_start_index()

  with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for index, row in enumerate(csv_reader):
      if index >= startIndex:
        coords = (float(row['lat']), float(row['lon']))
        
        if row['id'] in ids:
          #Adds data to ids dict
          ids[row['id']]['count'] += 1
          ids[row['id']]['times'].append(row['time'])
          ids[row['id']]['coords'].append(coords)
          ids[row['id']]['RSSI'].append(float(row['rssi']))
          
          #Adds data to UIDs class 
          uids.add_instance(row['id'], row['time'], coords, row['rssi'])
          
        else:
          ids[row['id']] = {
            'count': 1,
            'times': [row['time']],
            'coords': [coords],
            'RSSI': [float(row['rssi'])],
            'model': row['model'],
            'code': int(row['code'])
          }
          
          id = row['id']
          #Adds first instance of an uid to ids dict
          id = {
            'count': 1,
            'times': [row['time']],
            'coords': [coords],
            'RSSI': [float(row['rssi'])],
            'model': row['model'],
            'code': int(row['code'])
          }
          
          #Instantiates uid class obj
          uids = IDs(id)

          save_last_index(index + 1)
          print(uids)

  '''Start other functions from here'''
  for key in ids:
    if ids[key]['count'] > 1:
      times = ids[key]['times']
      first_time = (times[0][-7] + times[0][-5] + times[0][-4])
      last_time = (times[-1][-7] + times[-1][-5] + times[-1][-4])
      difference = int(last_time) - int(first_time)
      
      if difference >= 15:
        print(f'ID {key} was seen 15 minutes apart.')
      elif 15 > difference >= 10:
        print(f'ID {key} was seen 10 minutes apart.')
      elif 10 > difference >= 5:
        print(f'ID {key} was seen 5 minutes apart.')
      else:
        pass
      
Main()







#For testing keep this in.
os.system('rm start_index.txt')

'''Initiates del_txt_file'''
#atexit.register(delete_txt_file)