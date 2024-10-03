import TPMS_Classes as tclass
import os
import time
import json

#intializes rtl_433
os.system('rtl_433 -f 315M -F json:cat.json -M level -M time -K gpsd,lat,lon')

ln = 0

tclass.ID()

def parse_uids(ln):
  pass