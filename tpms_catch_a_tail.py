import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')
ids = {}
startIndex = 0



class IDs:
  def __init__(self, id):
    self.id = id
  
  def add_instance(self, id, time, coords, rssi):
    self.id['count'] += 1
    self.id['times'].append(time)
    self.id['coords'].append(coords)
    self.id['RSSI'].append(rssi)
    
    print(self.id)
    
    
    
  
def Main():
  with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for index, row in enumerate(csv_reader):
      if index >= startIndex:
        
        #TODO: Figure out a way to += startIndex
        coords = (float(row['lat']), float(row['lon']))
        
        if row['id'] in ids:
          #Adds data to ids dict
          ids[row['id']]['count'] += 1
          ids[row['id']]['times'].append(row['time'])
          ids[row['id']]['coords'].append(coords)
          ids[row['id']]['RSSI'].append(float(row['rssi']))
          
          #Adds data to UIDs class // DOESN'T WORK
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


    
Main()


