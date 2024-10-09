from TPMS_Classes import UID
import csv
import os
import time
import uuid # might not need it

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')

ln = 0
sln = 0   




  


class ID:
  def __init__(self, id, time, lat, lon, model, rssi, code): 
    self.id = id
    self.time = time
    self.lat = lat
    self.lon = lon
    self.model = model
    self.rssi = rssi
    self.code = code
    
    #self.sku = str(uuid.uuid4())
    
  def display_info(self):
    print(f"Id: {self.id}, time: {self.time}") #Add other items

  
class Id_Manager:
 
  def __init__(self):
    self.ids = []
    count = 0
    
  
  def load_ids(self):
      with open('test.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        self.ids = [ID(
          int(row['id']), 
          float(row['lat']),
          float(row['lon']),
          row['time'],
          row['model'],
          float(row['rssi']),
          int(row['code']),)
              for row in csv_reader ] 
        

    
test = Id_Manager() 

test.load_ids()

