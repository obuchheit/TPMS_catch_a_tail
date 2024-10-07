import TPMS_Classes as tclass
import csv
import os
import time

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

data = {}
sln = 0
ln = 0

with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  for line in csv_reader[sln:]:
    ln += 1
    count = 1

    id = line['id']
    ti = line['time']

    grid_count = grid_count[count] = line['lat'], line['lon']

    model = line['model']
    rssi = line['rssi']
    code = line['code']

    if id not in tclass.UID:

      id = tclass.UID(ti, grid_count, model, rssi, code, count)

    if id in tclass.UID:
      tclass.UID.set_UID()

    id = tclass.ID(ti, grid_count, model, rssi, code, count)


sln = ln
ln = 0

for key in tclass.ID:
  if key not in tclass.ID:
    pass




