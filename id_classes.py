import math

'''Loops through csv file from rtl_433 and pushes data into dictionaries''' 

'''TODO: Create an ignore list that won't add any of the Ids to the output.
          - Add a function where the user can manually add Ids to ignore list.
          -Might be better off in another file that is then read by class.'''


class IDs:
  targets = {}
  def __init__(self, id, time, coord, rssi, model):
    self.id = id
    self.count = 1
    self.times = [time]
    self.coords = [coord]
    self.rssi = [rssi]
    self.model = model
    self.first_time = (int(time[-7]) * 60) + (int(time[-5]) * 10) + (int(time[-4]))

  def add_instance(self, time, coord, rssi):
    self.count += 1
    self.times.append(time)
    self.coords.append(coord)
    self.rssi.append(rssi)
    self.last_time = (int(time[-7]) * 60) + (int(time[-5]) * 10) + (int(time[-4]))
    self.difference_time = self.last_time - self.first_time
    self.difference_distance = self.calulate_distance(self.coords[0][0], self.coords[0][1], self.coords[-1][0], self.coords[-1][1])


  @staticmethod
  def calulate_distance(lat1, lon1, lat2, lon2):
    #Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    #Hversine Formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    #Radius of Earth in Km 
    r = 6371.0
    return c * r
  

  def __str__(self):
    if self.difference_distance > 1 and self.difference_time > 5:
      return f'''
{self.model} with ID {self.id} was seen:\n 
{self.difference_time} minutes apart and {self.difference_distance} Kms apart.'''

      