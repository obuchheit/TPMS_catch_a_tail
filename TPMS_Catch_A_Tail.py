import TPMS_Classes as tclass
import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

sln = 0
ln = 0

with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  for line in csv_reader:
    ln += 1
    
    id = int(line['id'])
    ti = line['time']
    coordinates = float(line['lat']), float(line['lon'])
    model = line['model']
    rssi = float(line['rssi'])
    code = int(line['code'])
    
    
    
    #Adds a new ID to the UID class
    if isinstance(id, tclass.UID) == False:
      count = 1
      first_ins = {count: [ti, coordinates, rssi]}
                  
      id = tclass.UID(model, code, count)
      id.var_objs = first_ins 
    #Adds the other instances of an ID in the UID class
    else:
      count = id.count + 1
      ins = {count: [ti, coordinates, rssi]}
      print(ins)
      
      tclass.UID.add_var_objs(ins)


