from TPMS_Classes import UID
import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

sln = 0
ln = 0

with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)


  #need to make for loop start at the point we left off
  for line in csv_reader:
    ln += 1
    
    id_int = int(line['id'])
    id = f"id_{id_int}"
    ti = line['time']
    coordinates = float(line['lat']), float(line['lon'])
    model = line['model']
    rssi = float(line['rssi'])
    code = int(line['code'])
        
    
    #Adds a new ID to the UID class
    if isinstance(line['id'], UID):
      count = line['id'].count + 1
      ins = {count: [ti, coordinates, rssi]}
      print(ins)
      
      UID.set_var_objs(ins)
      
    else:
      count = 1
      first_ins = {count: [ti, coordinates, rssi]}
      
      line['id'] = UID(first_ins, model, code, count)

  