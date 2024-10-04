import TPMS_Classes as tclass
import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

data = {}
sln = 0
ln = 0

'''Adds any new ID in the data file'''
with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  for line in csv_reader[sln:]:
    ln += 1
    
    if line['id'] not in data:

      data[line['id']] = [line['time'], line['lat'], line['lon'], line['model'], line['rssi'], line['code']] 



