import sys
import json
import os
import subprocess
from flask import Flask, render_template, request, url_for, redirect
import RPi.GPIO as GPIO
sys.path.insert(0, '/home/pi/project/reefcontrol')
import reefcontrol
from reefcontrol import ato, temperature, power, processes


#Board setup.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#Location of temperature sensor JSON config.
temperatureSensorsPath = os.getcwd()
temperatureSensorsJSON = temperatureSensorsPath+"/config/temperaturesensors.json"
#Read temperature sensor config file to get sensor info.
with open(temperatureSensorsJSON) as json_temperaturesensors:
    temperaturesensors = json.load(json_temperaturesensors)


#Location of outlet JSON config.
outletsPath = os.getcwd()
outletsJSON = outletsPath+"/config/outlets.json"
#Read outlet config file to get outlet info.
with open(outletsJSON) as json_outlets:
    outlets = json.load(json_outlets)


#Location of processes JSON config.
processesPath = os.getcwd()
processesJSON = processesPath+"/config/processes.json"
#Read processes config file to get process info.
with open(processesJSON) as json_processes:
    processesList = json.load(json_processes)


#Location of ato JSON config.
atoPath = os.getcwd()
atoJSON = atoPath+"/config/ato.json"
#Read ato config file to get ato info.
with open(atoJSON) as json_ato:
    atosensors = json.load(json_ato)


#Location of temperature CSV file provided by scripts/templogger.py (Run by SUpervisor.)
tempCSVpath = (os.getcwd()+"/static/")
tempCSV = "temp.txt"


app = Flask(__name__)


#Main page.
@app.route('/')
def index():
    temperatureStats = temperature.getTemperatureStats(temperaturesensors,tempCSVpath,tempCSV)
    powerStatus = power.getPowerStatus(outlets)
    processStatus = processes.getProcessStatus(processesList)
    atoStatus = ato.getReservoirStatus(int(atosensors[0]['triggerpin']),int(atosensors[0]['echopin']),int(atosensors[0]['capacity']),int(atosensors[0]['uppercorrection']))
    if atoStatus <= 15:
        atoStatusColor = "progress-bar-danger"
    elif atoStatus <= 33:
        atoStatusColor = "progress-bar-warning"
    elif atoStatus >= 34:
        atoStatusColor = "progress-bar-success"
    return render_template('index.html',temperatureStats=temperatureStats,powerStatus=powerStatus,atoStatus=atoStatus,atoStatusColor=atoStatusColor,processStatus=processStatus)


#Turn all outlets on.
@app.route('/on/', methods=['POST'])
def on():
    power.allOn(outlets)
    return redirect("/", code=302)


#Turn all outlets off.
@app.route('/off/', methods=['POST'])
def off():
    power.allOff(outlets)
    return redirect("/", code=302)


#Turn off defined outlets for feeding time.
@app.route('/feed/', methods=['POST'])
def feed():
    power.feed(outlets)
    return redirect("/", code=302)


#Control individual outlets.
@app.route('/outletControl/', methods=['POST'])
def outletControl():
    pin=request.form['pin']
    action=request.form['action']
    power.controlOutlet(action,pin)
    return redirect("/", code=302)


#Run it!
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5001,debug=True)