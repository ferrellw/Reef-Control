import csv
from ds18b20 import DS18B20
import subprocess
import json
import RPi.GPIO as GPIO


#Board setup.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#Read from CSV file to get temperature average. 
def getTempAvg(file,sensor,correction):
	avg = 0
	summation = 0
	rowCount = 0
	temp = 0
	try:
		with open(file, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			next(csvreader)
			for row in csvreader:
				summation = float(row[sensor]) + summation
				rowCount += 1
			csvfile.close()
			avg = summation / rowCount
			avg = avg - correction
			avg = str("%.2f" % avg)
			return avg
	except:
		return "Error retrieving temperature average for:",sensor


#Get temperature by sensor address.
def getTemp(address,correction):
	try:
		sensor = DS18B20(str(address))
		return str("%.2f" % (sensor.get_temperature(DS18B20.DEGREES_F) - correction))
	except:
		return "Error retrieving temperature." 


#Read from user supplied outlet list and get the status of each outlet.
def outletStatus(outletList):
	try:
		for outlet in outletList:
			ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
			output = str(ps.communicate())
			output = output.translate(None,"\n',N('on\e) ")
			if output == "1":
			    outlet['status'] = "Off"
			    outlet['selected'] = "selected"
			if output == "0":
			    outlet['status'] = "On"
		return outletList
	except:
		return "Error getting outlet status."


#Turn all outlets on.
def allOn(outletList):
	try:
		for outlet in outletList:
			GPIO.setup(int(outlet['pin']), GPIO.OUT)
		return "All outlets on."
	except:
		return "Error turning on all outlets."


#Turn all outlets off.
def allOff(outletList):
	try:
		for outlet in outletList:
			GPIO.setup(int(outlet['pin']), GPIO.IN)
		return "All outlets off."
	except:
		return "Error turning off all outlets."	


#Turn off defined outlets for feeding time.
def feed(outletList):
	try:
		for outlet in outletList:
			if outlet['feed'] == "yes":
				ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
				output = str(ps.communicate())
				output = output.translate(None,"\n',N('on\e) ")
				if output == "1":
					outlet['status'] = "Off"
				if output == "0":
					outlet['status'] = "On"
		for outlet in outletList:
			if (outlet['feed'] == "yes") and (outlet['status'] == "Off"):
					GPIO.setup(int(outlet['pin']), GPIO.OUT)
			if (outlet['feed'] == "yes") and (outlet['status'] == "On"):	
					GPIO.setup(int(outlet['pin']), GPIO.IN)
		return outletList
	except:
		return "Error turning off outlets for feeding."


#Control individual outlets.
def outletControl(action,pin):
	try:
		if action == "on":
			GPIO.setup(int(pin), GPIO.OUT)
		if action == "off":
			GPIO.setup(int(pin), GPIO.IN)
		return "Outlet is now ",action
	except:
		return "Error turning off outlet."


#Turn off defined outlets for feeding time.
def coolingStatus(sensors):
	try:
		for sensor in sensors:
			#print sensor['coolingpin']
			ps = subprocess.Popen(('gpio', '-g', 'read', str(sensor['coolingpin'])), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
			output = str(ps.communicate())
			output = output.translate(None,"\n',N('on\e) ")

			if output == "1":
				sensor['coolingStatus'] = "Off"
			if output == "0":
				sensor['coolingStatus'] = "On"
		return sensors
	except:
		return "Error retrieving cooling status."