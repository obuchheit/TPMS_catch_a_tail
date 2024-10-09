import csv
import os
import time
import uuid # might not need it

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')
ids = []
objects = []

class ID:
  def __init__(self, id): 
    self.id = id
   
    
  
def Main():
  with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      id_dict = {row['id']: [
        row['time'],
        float(row['lat']),
        float(row['lon']),
        row['model'],
        float(row['rssi']),
        int(row['code']),
        1]}
      ids.append(id_dict)
      
  
  for key in ids:
    uid = ID(key)
    objects.append(uid)
    
Main()
print(objects)




  
class Id_Manager:
 
  def __init__(self):
    self.ids = []
    
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
        
    
    #Adds a new ID to the UID class
  