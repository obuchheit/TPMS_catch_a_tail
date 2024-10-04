import csv

data = {}

with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)

  for line in csv_reader:
    data[line['id']] = [line['lat'], line['lon'], line['model'], line['rssi'], line['code']] 


class UID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self, time, id, model,):
    pass

  




  
