
  
class UID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''
  
  def __init__(self, first_ins, model, code, count):
    self.var_objs = first_ins
    self.model = model
    self.code = code
    self.count = count
    
    
  def set_var_objs(self, ins): 
    pass
  
  def get_var_objs(self):
    return self.var_objs       


class TargetDeck:
  pass

class IgnoreList:
  pass

class CSVOutput:
  pass

class KMLOutput:
  pass
    




  
