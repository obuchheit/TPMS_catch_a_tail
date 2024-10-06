import csv
import TPMS_Catch_A_Tail as cat

class ID:
  '''Creates a dictionary of all collected instances of a TPMS Tx.'''
  
  def __init__(self, time, loc, model, rssi, code):
    self.time = time
    self.loc = loc
    self.model = model
    self.rssi = rssi 
    self.code = code

  def get_time(self):
    return self.time
  
class UID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self, time, loc, model, rssi, code):
    pass
    




  
