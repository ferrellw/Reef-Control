import RPi.GPIO as GPIO
import time
import sys
import subprocess
import json

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Pin Keeping
feedGroups = ['Outlet Group 5','Outlet Group 6']
outlets = '[{"name": "Output Group 1","pin": "20","status": "","feed": ""},{"name": "Output Group 2","pin": "26","status": "","feed": ""},{"name": "Output Group 3","pin": "19","status": "","feed": ""},{"name": "Output Group 4","pin": "13","status": "","feed": ""},{"name": "Output Group 5","pin": "6","status": "","feed": "yes"},{"name": "Output Group 6","pin": "5","status": "","feed": "yes"}]'
outlets = json.loads(outlets)


#Help
if sys.argv[1] == "help":
	print "\n"
	print "Useage: outlet-control og1 on"
	print "Useage: outlet-control og1 off"
	print "\n"
	print "feed - Turn off select pumps."
	print "status - Shows status of all outlet groups."
	print "on - Turns on all outlet groups."
	print "off - Turns off all outlet groups"
	print "outlet-control - Controls power functions of individual outlet groups."
	print "\n"


#Print Status
if sys.argv[1] == "status":
    print "#######################<br>"
    for outlet in outlets:
        ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
        output = str(ps.communicate())
        output = output.translate(None,"\n',N('on\e) ")
        if output == "1":
            outlet['status'] = "Off"
        if output == "0":
            outlet['status'] = "On"
    for outlet in outlets:
        print outlet['name']+": "+outlet['status']+"<br>"
    print "#######################<br><br>"
    print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
    print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"

#All on.
if sys.argv[1] == "on":
	try:
		print "#######################<br>"
		for outlet in outlets:
			GPIO.setup(int(outlet['pin']), GPIO.OUT)
		print "All outlet groups are now on...<br>"
		print "#######################<br><br>"
		print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
		print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	except:
		print "Error turning on all outlet groups."

#All off.
if sys.argv[1] == "off":
	try:
		print "#######################<br>"
		for outlet in outlets:
			GPIO.setup(int(outlet['pin']), GPIO.IN)
		print "All outlet groups are now off...<br>"
		print "#######################<br><br>"
		print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
		print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	except:
		print "Error turning off all outlet groups."
#Feed
if sys.argv[1] == "feed":
	print "#######################<br>"
	for outlet in outlets:
		ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = str(ps.communicate())
		output = output.translate(None,"\n',N('on\e) ")
		if output == "1":
			outlet['status'] = "Off"
		if output == "0":
			outlet['status'] = "On"
	for outlet in outlets:
		if outlet['feed'] == "yes":
			if outlet['status'] == "Off":
				GPIO.setup(int(outlet['pin']), GPIO.OUT)
				print outlet['name']+" is now: "+outlet['status']+"<br>"
			if outlet['status'] == "On":
				print outlet['name']+" is now: "+outlet['status']+"<br>"
				GPIO.setup(int(outlet['pin']), GPIO.IN)

#Outlet group control.
if sys.argv[1] == "outlet-control":	
	print "#######################<br>"
	#Outlet 1
	if sys.argv[2] == 'og1':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			print "Outlet group 1 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
    
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			print "Outlet group 1 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	#Outlet 2
	if sys.argv[2] == 'og2':
		if sys.argv[3] == 'on':
			GPIO.setup(26, GPIO.OUT)
			print "Outlet group 2 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		if sys.argv[3] == 'off':
			GPIO.setup(26, GPIO.IN)
			print "Outlet group 2 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	#Outlet 3		
	if sys.argv[2] == 'og3':
		if sys.argv[3] == 'on':
			GPIO.setup(19, GPIO.OUT)
			print "Outlet group 3 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		if sys.argv[3] == 'off':
			GPIO.setup(19, GPIO.IN)
			print "Outlet group 3 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	#Outlet 4		
	if sys.argv[2] == 'og4':
		if sys.argv[3] == 'on':
			GPIO.setup(13, GPIO.OUT)
			print "Outlet group 4 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		if sys.argv[3] == 'off':
			GPIO.setup(13, GPIO.IN)
			print "Outlet group 4 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"			
	#Outlet 5		
	if sys.argv[2] == 'og5':
		if sys.argv[3] == 'on':
			GPIO.setup(6, GPIO.OUT)
			print "Outlet group 5 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		if sys.argv[3] == 'off':
			GPIO.setup(6, GPIO.IN)
			print "Outlet group 5 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"		
	#Outlet 6		
	if sys.argv[2] == 'og6':
		if sys.argv[3] == 'on':
			GPIO.setup(5, GPIO.OUT)
			print "Outlet group 6 is now: on<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		if sys.argv[3] == 'off':
			GPIO.setup(5, GPIO.IN)
			print "Outlet group 6 is now: off<br>"
			print "#######################<br><br>"
			print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
			print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"