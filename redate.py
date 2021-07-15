# Recursively walks the provided path, changing each file's created and
# accessed time to match the datetime, if one is specified in the file
# name e.g... IMG_20190527_152734857.jpg
#
# USAGE: python3 redate.py <optional path to a folder>
#
# Current working directory is used as the start point if no source
# path is provided as an argument.

import os
import re
import sys
import json
import platform
import datetime
from datetime import timezone
from datetime import datetime

if(platform.system() == "Windows"):
	from win32_setctime import setctime

rex = re.compile(
	'^[A-Z]{1,10}_(?P<year>20[0-2][0-9])'
	'(?P<month>[0-1][0-9])'
	'(?P<day>[0-3][0-9])_'
	'(?P<hour>[0-2][0-9])'
	'(?P<minute>[0-5][0-9])'
	'(?P<second>[0-5][0-9])')

num_files = 0
num_redated = 0

def process(file_name, file_path):
	global num_redated
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
		os.utime(file_path, (timestamp, timestamp))
		if(platform.system() == "Windows"):
			setctime(file_path, timestamp)
		num_redated += 1

source = os.getcwd() if len(sys.argv) < 2 else sys.argv[1]

assert os.path.isdir(source)
for root, dirs, files in os.walk(source):
	for file in files:
		num_files += 1
		process(file, os.path.join(root,file))
print(f"Done. Updated timestamps for {num_redated} of {num_files} files.")