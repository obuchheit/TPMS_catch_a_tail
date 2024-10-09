# __add__ method
#uuid

    #print(line['time'], line['lat'], line['lon'], line['model'], line['id'],line['rssi'], line['code']) 


class UID:
  def __init__(self, id, time, lat, lon, model, rssi, code): 
    self.id = id
    self.time = time
    self.lat = lat
    self.lon = lon
    self.model = model
    self.rssi = rssi
    self.code = code
  
class IdLoader:
 
  def __init__(self, file):
    self.file = file
    self.ids = []
  
  #add try except
  def load_ids(self):
    with open('test.csv', 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      self.ids = [UID(int(row['id ']), 
                      float(row['lat']),
                      float(row['lon']),
                      row['time'],
                      row['model'],
                      float(row['rssi']),
                      int(row['code']),)
                          for row in csv_reader ] 
      
  def add_id()
      