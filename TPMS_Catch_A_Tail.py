import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')
ids = {}
startIndex = 0
    
  
def Main():
  with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for index, row in enumerate(csv_reader):
      if index >= startIndex:
        startIndex = startIndex + 1
        
        coords = (float(row['lat']), float(row['lat']))
        variable_data = {count: [row['time'], float(row['lat']), float(row['lon']), float(row['rssi'])]}
        
        if row['id'] in ids:
          
          pass
        else:
          ids[row['id']] = {
            'count': 1,
            'times': [row['time']],
            'coords': [coords],
            'RSSI': [float(row['rssi'])],
            'model': row['model'],
            'code': int(row['code'])
          }
            


    
Main()
print(ids)

  