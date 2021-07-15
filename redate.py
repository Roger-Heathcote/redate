import os
import re
import sys
import json
import pytz
import platform
import datetime
from datetime import timezone
from datetime import datetime

if(platform.system() == "Windows"):
	print("Windows detected")
	from win32_setctime import setctime

rex = re.compile( r'^[A-Z]{1,10}_(?P<year>20[0-2][0-9])(?P<month>[0-1][0-9])(?P<day>[0-3][0-9])_(?P<hour>[0-2][0-9])(?P<minute>[0-5][0-9])(?P<second>[0-5][0-9])')

def process(file_name, file_path):
	res = re.match(rex, file_name)
	if res:
		Y = int(res.group("year"))
		M = int(res.group("month"))
		D = int(res.group("day"))
		h = int(res.group("hour"))
		m = int(res.group("minute"))
		s = int(res.group("second"))
		dt = datetime(Y, M, D, h, m, s)
		timestamp = dt.timestamp()
		print(file_name, timestamp)

		os.utime(file_path, (timestamp, timestamp))
		if(platform.system() == "Windows"):
			setctime(file_path, timestamp)

source = os.getcwd() if len(sys.argv) < 2 else sys.argv[1]

assert os.path.isdir(source)
for root, dirs, files in os.walk(source):
	for file in files:
		process(file, os.path.join(root,file))