import sys
import json
import os
import subprocess
import RPi.GPIO as GPIO
import csv
from ds18b20 import DS18B20


def getTemperatureStats(temperaturesensors,tempCSVpath,tempCSV):
    try:
        for temperaturesensor in temperaturesensors:
            if temperaturesensor['type'] == "temperature":
                avg = 0
                summation = 0
                rowCount = 0
                temperature = 0
                temperaturesensor['temperature'] = float("%.2f" % (DS18B20(str(temperaturesensor['address'])).get_temperature(DS18B20.DEGREES_F) + temperaturesensor['temperaturecorrection']))
                with open(tempCSVpath+tempCSV, 'r') as csvfile:
                    csvreader = csv.reader(csvfile)
                    next(csvreader)
                    for row in csvreader:
                        summation = float(row[int(temperaturesensor['csvid'])]) + summation
                        rowCount += 1
                    csvfile.close()
                    avg = summation / rowCount
                    temperaturesensor['temperatureaverage'] = str("%.2f" % avg)
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