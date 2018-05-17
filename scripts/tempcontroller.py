from ds18b20 import DS18B20
import time
import datetime
import os.path
import json
import RPi.GPIO as GPIO
import csv
import subprocess
import sys


#Location of main script, power.py
temperatureSensorsPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
temperatureSensorsJSON = temperatureSensorsPath+"/config/temperaturesensors.json"


#Read temperature sensor config file to get sensor info.
try:
    with open(temperatureSensorsJSON) as json_temperaturesensors:
        temperaturesensors = json.load(json_temperaturesensors)
except:
    print "Temperature Sensor config file not found."


#GPIO setup.
try: 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    print "GPIO setup."
except:
    print "Failed to setup GPIO."
    sys.exit(1)


def getTemperatureStats(temperaturesensors):
    try:
        for temperaturesensor in temperaturesensors:
            if temperaturesensor['type'] == "temperature":
                avg = 0
                summation = 0
                rowCount = 0
                temperature = 0
                temperaturesensor['temperature'] = float("%.2f" % (DS18B20(str(temperaturesensor['address'])).get_temperature(DS18B20.DEGREES_F) + temperaturesensor['temperaturecorrection']))
            if temperaturesensor['pin']:
                ps = subprocess.Popen(('gpio', '-g', 'read', str(temperaturesensor['pin'])), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
                output = str(ps.communicate())
                output = output.translate(None,"\n',N('on\e) ")
            if output == "1":
                temperaturesensor['pinstatus'] = "Off"
            if output == "0":
                temperaturesensor['pinstatus'] = "On"
        return temperaturesensors

    except:
        print "Error getting sensor status."


while True:
    getTemperatureStats(temperaturesensors)
    try:
        for temperaturesensor in temperaturesensors:
            if (float(temperaturesensor['temperature']) >= float(temperaturesensor['temperaturethreshold'])):
                GPIO.setup(int(temperaturesensor['pin']), GPIO.OUT)
                print "Temperature above threshold. \nName: "+temperaturesensor['name']+" Temperature: "+str(temperaturesensor['temperature'])+" Threshold: "+str(temperaturesensor['temperaturethreshold'])
                break
            if (float(temperaturesensor['temperature']) <= float(temperaturesensor['temperaturethreshold'])):
                GPIO.setup(int(temperaturesensor['pin']), GPIO.IN)
                print "Temperature below threshold. \nName: "+temperaturesensor['name']+" Temperature: "+str(temperaturesensor['temperature'])+" Threshold: "+str(temperaturesensor['temperaturethreshold'])
        time.sleep(30)
    except KeyboardInterrupt:
      quit()
    except:
      print "Some sort of error. Continuing..."
      pass