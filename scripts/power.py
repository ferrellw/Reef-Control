import RPi.GPIO as GPIO
import sys
import time
import subprocess
import json


#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#Pin Keeping
outlets = '[{"name": "Outlet Group 1","pin": "13","status": "","feed": ""},{"name": "Outlet Group 2","pin": "19","status": "","feed": ""},{"name": "Outlet Group 3","pin": "26","status": "","feed": ""},{"name": "Outlet Group 4","pin": "21","status": "","feed": ""},{"name": "Outlet Group 5","pin": "20","status": "","feed": "yes"},{"name": "Outlet Group 6","pin": "16","status": "","feed": "yes"}]'
outlets = json.loads(outlets)


#Quick redirect after form submission. This should prolly be done in Flask (app.py) but I haven't looked into it yet.
back = "<script type=\"text/javascript\">window.setTimeout('history.back();', 100);</script>"


#All on. Read from outlets list and turn on all outlets via pin.
if sys.argv[1] == "on":
	try:
		for outlet in outlets:
			GPIO.setup(int(outlet['pin']), GPIO.OUT)
		print back
	except:
		print "Error turning on all outlet groups."


#All off. Read from outlets list and turn off all outlets via pin.
if sys.argv[1] == "off":
	try:
		for outlet in outlets:
			GPIO.setup(int(outlet['pin']), GPIO.IN)
		print back
	except:
		print "Error turning off all outlet groups."


#Feed. Turn off defined outlets for feeding time. Read from outlets, get all status of all outlets
if sys.argv[1] == "feed":
	#Loop over items in outlets.
	for outlet in outlets:
		#Get GPIO pin status.
		ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = str(ps.communicate())
		#Output is not boolean. Lets fix that.
		output = output.translate(None,"\n',N('on\e) ")
		#Update the list to reflect status of outlet.
		if output == "1":
			outlet['status'] = "Off"
		if output == "0":
			outlet['status'] = "On"
	#Once we have the status of all outlets we need to only action outlets defined as "feed".
	for outlet in outlets:
	  	if outlet['feed'] == "yes":
	  		#If the outlet is off, turn it on.
	  		if outlet['status'] == "Off":
	  			GPIO.setup(int(outlet['pin']), GPIO.OUT)
	  		#If the outlet is on, turn it off.	
	  		if outlet['status'] == "On":
	  			GPIO.setup(int(outlet['pin']), GPIO.IN)
	print back


#Outlet group control. I call them groups but they are a single outlet with 2 receptacles. Exception to this is 5 and 6. These are defined as "feed" outlets. 
#This should all be broken down to read from the outlets list vs manually defining each outlet group.
if sys.argv[1] == "outlet-control":	
	#Outlet 1
	if sys.argv[2] == 'og1':
		if sys.argv[3] == 'on':
			GPIO.setup(13, GPIO.OUT)
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(13, GPIO.IN)
			print back
	if sys.argv[2] == 'og2':
		if sys.argv[3] == 'on':
			GPIO.setup(19, GPIO.OUT)
			
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(19, GPIO.IN)
			print back	
	if sys.argv[2] == 'og3':
		if sys.argv[3] == 'on':
			GPIO.setup(26, GPIO.OUT)
			
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(26, GPIO.IN)
			print back		
	if sys.argv[2] == 'og4':
		if sys.argv[3] == 'on':
			GPIO.setup(21, GPIO.OUT)
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(21, GPIO.IN)
			print back				
	if sys.argv[2] == 'og5':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			GPIO.setup(16, GPIO.OUT)
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			GPIO.setup(16, GPIO.IN)
			print back			
	if sys.argv[2] == 'og6':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			GPIO.setup(16, GPIO.OUT)
			print back
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			GPIO.setup(16, GPIO.IN)
			print back