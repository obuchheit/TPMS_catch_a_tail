# __add__ method
#uuid

import csv
    #print(line['time'], line['lat'], line['lon'], line['model'], line['id'],line['rssi'], line['code']) 


ids = {}

with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    
    ids[row['id']] = [
    row['time'],
    float(row['lat']),
    float(row['lon']),
    row['model'],
    float(row['rssi']),
    int(row['code'])]
    
print(ids)