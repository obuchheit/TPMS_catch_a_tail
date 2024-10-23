import csv 
from id_classes import IDs

csv_file = 'google_earth.csv' #change to a var name

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['id', 'coords', 'times', 'rssi'])

