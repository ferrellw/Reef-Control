import RPi.GPIO as GPIO
import sys
import time
import subprocess
import json


#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#Pin Keeping
outlets = '[{"name": "Outlet Group 1","pin": "13","status": "","feed": "","form": "og1","desc":"Free"},{"name": "Outlet Group 2","pin": "19","status": "","feed": "","form": "og2","desc":"Refugium Light"},{"name": "Outlet Group 3","pin": "26","status": "","feed": "","form": "og3","desc":"Power Head Controller"},{"name": "Outlet Group 4","pin": "21","status": "","feed": "","form": "og4","desc":"Cooling Fan"},{"name": "Outlet Group 5","pin": "20","status": "","feed": "yes","form": "og5","desc":"Auto Top Off"},{"name": "Outlet Group 6","pin": "16","status": "","feed": "yes","form": "og6","desc":"Return Pump, Protein Skimmer"}]'
outlets = json.loads(outlets)





if sys.argv[1] == "outlet-control":	
	#Outlet 1
	if sys.argv[2] == 'og1':
		if sys.argv[3] == 'on':
			GPIO.setup(13, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(13, GPIO.IN)
	if sys.argv[2] == 'og2':
		if sys.argv[3] == 'on':
			GPIO.setup(19, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(19, GPIO.IN)
	if sys.argv[2] == 'og3':
		if sys.argv[3] == 'on':
			GPIO.setup(26, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(26, GPIO.IN)
	if sys.argv[2] == 'og4':
		if sys.argv[3] == 'on':
			GPIO.setup(21, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(21, GPIO.IN)
	if sys.argv[2] == 'og5':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			GPIO.setup(16, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			GPIO.setup(16, GPIO.IN)
	###These two operate together.		
	if sys.argv[2] == 'og6':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			GPIO.setup(16, GPIO.OUT)
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			GPIO.setup(16, GPIO.IN)