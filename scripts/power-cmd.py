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
pinStatus = []

#Help
if sys.argv[1] == "help":
	print "\n"
	print "Useage: outlet-control og1 on"
	print "Useage: outlet-control og1 off"
	print "\n"
	print "status - Shows status of all outlet groups."
	print "on - Turns on all outlet groups."
	print "off - Turns off all outlet groups"
	print "og - Prints outlet group numbers"
	print "pins - Print used GPIO pins"
	print "pin-status - Print used GPIO pins and their status. 1 is off, 0 is on."
	print "outlet-control - Controls power functions of individual outlet groups."
	print "\n"

#Print Pins
if sys.argv[1] == "pins":
	for pin in pins:
		print pin

#Print Outlet Groups
if sys.argv[1] == "og":
	for outletGroup in outletGroups:
		print outletGroup

#Print pin Status
if sys.argv[1] == "pin-status":
	print "1 is off, 0 is on."
	for pin in pins:
		ps = subprocess.Popen(('gpio', '-g', 'read', pin), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = ps.communicate()
		outputTrans = str(output)
		outputTrans = outputTrans.translate(None,"\n',N('on\e) ")
		pinStatus.append(outputTrans)
	for outletGroup, pin in zip(outletGroups,pinStatus):
		print "Outlet Group: "+outletGroup+", Pin Status: "+pin

#Print Status
if sys.argv[1] == "status":
	print "#######################"
	for pin in pins:
		ps = subprocess.Popen(('gpio', '-g', 'read', pin), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
		output = ps.communicate()
		outputTrans = str(output)
		outputTrans = outputTrans.translate(None,"\n',N('on\e) ")
		pinStatus.append(outputTrans)
	for outletGroup, pin in zip(outletGroups,pinStatus):
		if pin == '1':	
			print "Outlet group "+outletGroup+": Off"
		if pin == '0':
			print "Outlet group "+outletGroup+": On"
	print "#######################"

#All on.
if sys.argv[1] == "on":
	try:
		print "#######################"
		GPIO.setup(20, GPIO.OUT)
		GPIO.setup(26, GPIO.OUT)
		GPIO.setup(19, GPIO.OUT)
		GPIO.setup(13, GPIO.OUT)
		GPIO.setup(6, GPIO.OUT)
		GPIO.setup(5, GPIO.OUT)
		print "All outlet groups on..."
		print "#######################"
	except:
		print "Error turning on all outlet groups."

#All off.
if sys.argv[1] == "off":
	try:
		print "#######################"
		GPIO.setup(20, GPIO.IN)
		GPIO.setup(26, GPIO.IN)
		GPIO.setup(19, GPIO.IN)
		GPIO.setup(13, GPIO.IN)
		GPIO.setup(6, GPIO.IN)
		GPIO.setup(5, GPIO.IN)
		print "All outlet groups off..."
		print "#######################"
	except:
		print "Error turning off all outlet groups."

#Outlet group control.
if sys.argv[1] == "outlet-control":	
	print "#######################"
	#Outlet 1
	if sys.argv[2] == 'og1':
		if sys.argv[3] == 'on':
			GPIO.setup(20, GPIO.OUT)
			print "Outlet group 1 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(20, GPIO.IN)
			print "Outlet group 1 is now: off"
			print "#######################"
	#Outlet 2
	if sys.argv[2] == 'og2':
		if sys.argv[3] == 'on':
			GPIO.setup(26, GPIO.OUT)
			print "Outlet group 2 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(26, GPIO.IN)
			print "Outlet group 2 is now: off"
			print "#######################"
	#Outlet 3		
	if sys.argv[2] == 'og3':
		if sys.argv[3] == 'on':
			GPIO.setup(19, GPIO.OUT)
			print "Outlet group 3 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(19, GPIO.IN)
			print "Outlet group 3 is now: off"
			print "#######################"
	#Outlet 4		
	if sys.argv[2] == 'og4':
		if sys.argv[3] == 'on':
			GPIO.setup(13, GPIO.OUT)
			print "Outlet group 4 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(13, GPIO.IN)
			print "Outlet group 4 is now: off"
			print "#######################"				
	#Outlet 5		
	if sys.argv[2] == 'og5':
		if sys.argv[3] == 'on':
			GPIO.setup(6, GPIO.OUT)
			print "Outlet group 5 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(6, GPIO.IN)
			print "Outlet group 5 is now: off"
			print "#######################"			
	#Outlet 6		
	if sys.argv[2] == 'og6':
		if sys.argv[3] == 'on':
			GPIO.setup(5, GPIO.OUT)
			print "Outlet group 6 is now: on"
			print "#######################"
		if sys.argv[3] == 'off':
			GPIO.setup(5, GPIO.IN)
			print "Outlet group 6 is now: off"
			print "#######################"