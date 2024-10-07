import csv
import TPMS_Catch_A_Tail as cat

class ID:
  '''Creates a dictionary of all collected instances of a TPMS Tx.'''
  
  def __init__(self, time, grid_count, model, rssi, code):
    self.time = time
    self.grid_count = grid_count
    self.model = model
    self.rssi = rssi 
    self.code = code

  def get_time(self):
    return self.time
  
class UID(ID):
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self):
    pass

  def set_var_objs(self): 
    pass


class TargetDeck:
  pass

class IgnoreList:
  pass

class CSVOutput:
  pass

class KMLOutput:
  pass
    




  
