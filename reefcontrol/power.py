import sys
import json
import os
import subprocess
import RPi.GPIO as GPIO


#Turn all outlets on.
def allOn(outlets):
    try:
        for outlet in outlets:
            GPIO.setup(int(outlet['pin']), GPIO.OUT)
        return "All outlets on."
    except:
        return "Error turning on all outlets."


#Turn all outlets off.
def allOff(outlets):
    try:
        for outlet in outlets:
            GPIO.setup(int(outlet['pin']), GPIO.IN)
        return "All outlets off."
    except:
        return "Error turning off all outlets." 


#Control individual outlets.
def controlOutlet(action,pin):
    try:
        if action == "on":
            GPIO.setup(int(pin), GPIO.OUT)
        if action == "off":
            GPIO.setup(int(pin), GPIO.IN)
        return "Outlet is now ",action
    except:
        return "Error turning off outlet."


#Read from user supplied outlet list and get the status of each outlet.
def getPowerStatus(outlets):
    try:
        for outlet in outlets:
            ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
            output = str(ps.communicate())
            output = output.translate(None,"\n',N('on\e) ")
            if output == "1":
                outlet['status'] = "Off"
                outlet['selected'] = "selected"
            if output == "0":
                outlet['status'] = "On"
        return outlets
    except:
        return "Error getting outlet status."


#Turn off defined outlets for feeding time.
def feed(outlets):
    try:
        for outlet in outlets:
            if outlet['feed'] == "yes":
                ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
                output = str(ps.communicate())
                output = output.translate(None,"\n',N('on\e) ")
                if output == "1":
                    outlet['status'] = "Off"
                if output == "0":
                    outlet['status'] = "On"
        for outlet in outlets:
            if (outlet['feed'] == "yes") and (outlet['status'] == "Off"):
                    GPIO.setup(int(outlet['pin']), GPIO.OUT)
            if (outlet['feed'] == "yes") and (outlet['status'] == "On"):    
                    GPIO.setup(int(outlet['pin']), GPIO.IN)
        return outlets
    except:
        return "Error turning off outlets for feeding."