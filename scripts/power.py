import RPi.GPIO as GPIO
import time
import sys
import subprocess

#GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Useful Lists
pins = ['20','26','19','13','6','5']
outletGroups = ['1','2','3','4','5','6']
feedPins = ['5','6']
feedPinStatus = []
pinStatus = []

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
	for pin in pins:
		ps = subprocess.Popen(('gpio', '-g', 'read', pin), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = ps.communicate()
		outputTrans = str(output)
		outputTrans = outputTrans.translate(None,"\n',N('on\e) ")
		pinStatus.append(outputTrans)
	for outletGroup, pin in zip(outletGroups,pinStatus):
		if pin == '1':	
			print "Outlet group "+outletGroup+": Off<br>"
		if pin == '0':
			print "Outlet group "+outletGroup+": On<br>"
	print "#######################<br><br>"
	print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
	print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"

#All on.
if sys.argv[1] == "on":
	try:
		print "#######################<br>"
		GPIO.setup(20, GPIO.OUT)
		GPIO.setup(26, GPIO.OUT)
		GPIO.setup(19, GPIO.OUT)
		GPIO.setup(13, GPIO.OUT)
		GPIO.setup(6, GPIO.OUT)
		GPIO.setup(5, GPIO.OUT)
		print "All outlet groups on...<br>"
		print "#######################<br><br>"
		print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
		print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	except:
		print "Error turning on all outlet groups."

#All off.
if sys.argv[1] == "off":
	try:
		print "#######################<br>"
		GPIO.setup(20, GPIO.IN)
		GPIO.setup(26, GPIO.IN)
		GPIO.setup(19, GPIO.IN)
		GPIO.setup(13, GPIO.IN)
		GPIO.setup(6, GPIO.IN)
		GPIO.setup(5, GPIO.IN)
		print "All outlet groups off...<br>"
		print "#######################<br><br>"
		print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
		print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
	except:
		print "Error turning off all outlet groups."

#Feed
if sys.argv[1] == "feed":
	print "#######################<br>"
	for pin in feedPins:
		ps = subprocess.Popen(('gpio', '-g', 'read', pin), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = ps.communicate()
		outputTrans = str(output)
		outputTrans = outputTrans.translate(None,"\n',N('on\e) ")
		feedPinStatus.append(outputTrans)
	for pin,status in zip(feedPins,feedPinStatus):
		#print pin, status
		if status == '1':
		 	GPIO.setup(int(pin), GPIO.OUT)
		 	print "Outlet group "+pin+" on.<br>"
		if status == '0':
		 	GPIO.setup(int(pin), GPIO.IN)
		 	print "Outlet group "+pin+" off.<br>"
	print "#######################<br><br>"
	print "<button onclick='goBack()''>Go Back</button><script>function goBack() {window.history.back();}</script>"
	print "<script type=\"text/javascript\">window.setTimeout('history.back();', 5000);</script>"
		
		

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