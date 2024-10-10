# __add__ method
#uuid

import csv
    #print(line['time'], line['lat'], line['lon'], line['model'], line['id'],line['rssi'], line['code']) 


test_id = {'156870': {
  'count': 1,
  'times': ['0900'],
  'coords': [(90.001, 49.789)],
  'RSSI': [-22.6],
  'model': 'Ford',
  'code': 180
}}


test_id['156870']['count'] += 1
test_id['156870']['times'].append('1000')
test_id['156870']['coords'].append((91, 48))

print(test_id['156870']['count'])

print(test_id)

class UID:
  def __init__(self, id):
    pass