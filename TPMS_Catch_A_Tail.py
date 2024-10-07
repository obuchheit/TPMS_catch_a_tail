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

  for line in csv_reader[sln:]:
    ln += 1
    
    count = 1
    id = line['id']
    ti = line['time']
    lat = line['lat']
    lon = line['lon']
    model = line['model']
    rssi = line['rssi']
    code = line['code']
    
    #Adds a new ID to the UID class
    if id not in tclass.UID and tclass.IgnoreList:
      count = 1
      
      id = tclass.UID()

    #Adds the other instances of an ID in the UID class
    if id in tclass.UID:
      
      tclass.UID.set_var_objs()


    #Set instance in class ID
    id = tclass.ID()

