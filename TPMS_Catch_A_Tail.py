import csv
import os
import time
import uuid # might not need it

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
        
        
        if row['id'] in ids:
          pass
        else:
          ids[row['id']] = [
            row['time'],
            float(row['lat']),
            float(row['lon']),
            row['model'],
            float(row['rssi']),
            int(row['code']),
            1]
        
      
  

    
Main()
print(ids)

  