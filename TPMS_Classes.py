
  
class UID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self, model, code, count):

    self.var_objs = {}
    self.model = model
    self.code = code
    self.count = count

  def add_var_objs(self, ins): 
    self.count += 1
    
    #might need to do this in other file
    self.var_objs = ins
  
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
    




  
