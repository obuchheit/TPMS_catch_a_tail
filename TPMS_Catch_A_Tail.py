import json
import os

#intializes rtl_433
os.system('rtl_433 -f 315M -F json:test.json -M level -M time -K gpsd,lat,lon')


class ID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self):
    with open('cat.json', 'r') as infile:
      self._rtl_data = json.load(infile)

  




  
