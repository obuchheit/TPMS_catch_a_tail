ids = {}

'''open, loop through and add data from csv'''

# if row['id'] in ids:
          #Adds data to ids dict
          # ids[row['id']]['count'] += 1
          # ids[row['id']]['times'].append(row['time'])
          # ids[row['id']]['coords'].append(coords)
          # ids[row['id']]['RSSI'].append(float(row['rssi']))

    #else:
                  # #Adds first instance of an uid to ids dict
          # ids[row['id']] = {
          #   'id': row['id'],
          #   'count': 1,
          #   'times': [row['time']],
          #   'coords': [coords],
          #   'RSSI': [float(row['rssi'])],
          #   'model': row['model'],
          #   'code': int(row['code'])
          # }


    # for key in ids:
    # if ids[key]['count'] > 1:
    #   times = ids[key]['times']
    #   first_time = (times[0][-7] + times[0][-5] + times[0][-4])
    #   last_time = (times[-1][-7] + times[-1][-5] + times[-1][-4])
    #   difference = int(last_time) - int(first_time)
      
    #   if difference >= 15:
    #     print(f'ID {key} was seen 15 minutes apart.')
    #   elif 15 > difference >= 10:
    #     print(f'ID {key} was seen 10 minutes apart.')
    #   elif 10 > difference >= 5:
    #     print(f'ID {key} was seen 5 minutes apart.')
    #   else:
    #     pass