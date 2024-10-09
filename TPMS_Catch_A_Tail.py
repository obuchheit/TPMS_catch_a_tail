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

  #Need to figure out how to loop starting our at 
  for line in csv_reader:
    ln += 1
            
    #Adds a new ID to the UID class
    if isinstance(line['id'], UID):
      count = id.count + 1
      ins = {line['id']: [line['time'], float(line['lat']), float(line['lon']), line['rssi']]}
      print(ins)
      
      UID.set_var_objs(ins)
      
    else:
      count = 1
      first_ins = {line['id']: [line['time'], float(line['lat']), float(line['lon']), line['rssi']]}
      
                  
      ids = UID(first_ins, line['model'], line['code'], count)
            
