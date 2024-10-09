from TPMS_Classes import UID
import csv
import os
import time
import uuid # might not need it

#intializes rtl_433
#os.system('rtl_433 -f 315M -F csv:cat.csv -M level -M time -K gpsd,lat,lon')
  


<<<<<<< HEAD
with open('test.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)


  #need to make for loop start at the point we left off
  for line in csv_reader:
    ln += 1
=======
class ID:
  def __init__(self, id, time, lat, lon, model, rssi, code): 
    self.id = id
    self.time = time
    self.lat = lat
    self.lon = lon
    self.model = model
    self.rssi = rssi
    self.code = code
>>>>>>> 3d22140476aeff8e55ebb07c1fd84714d9df3220
    
    #self.sku = str(uuid.uuid4())
    
  def display_info(self):
    print(f"Id: {self.id}, time: {self.time}") #Add other items

  
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
        
<<<<<<< HEAD
    
    #Adds a new ID to the UID class
    if isinstance(line['id'], UID):
      count = line['id'].count + 1
      ins = {count: [ti, coordinates, rssi]}
      print(ins)
      
      UID.set_var_objs(ins)
      
    else:
      count = 1
      first_ins = {count: [ti, coordinates, rssi]}
      
      line['id'] = UID(first_ins, model, code, count)
=======

    
test = Id_Manager() 
test.load_ids()
>>>>>>> 3d22140476aeff8e55ebb07c1fd84714d9df3220

  