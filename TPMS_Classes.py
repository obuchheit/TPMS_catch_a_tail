
class ID:
  '''Makes a new unique id with a list of permanent items and dict of changable items linked to a Tire Pressure Sensor Monitor.'''

  def __init__(self):
    with open('cat.json', 'r') as infile:
      self._rtl_data = infile.load(infile)
  
  def get_data(self):
    print(self._rtl_data)


class UID:
  def __init__(self, time, id, model,):
    pass

  




  
