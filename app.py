import sys
import json
import os
from flask import Flask, render_template, request, url_for, redirect
sys.path.insert(0, '/home/pi/reef-controller/reefcontrol')
import reefcontrol



#Location of main script, power.py
scripts = (os.getcwd()+"/scripts/")
static = (os.getcwd()+"/static/")


app = Flask(__name__)


#Read config file to get outlet info.
with open('outlets.json') as json_outlets:
    outlets = json.load(json_outlets)


#Read sensor config file to get sensor info.
with open('sensors.json') as json_sensors:
    sensors = json.load(json_sensors)


#Main page.
@app.route('/')
def index():
    coolingStatus = reefcontrol.coolingStatus(sensors)
    for sensor in sensors:
        sensor['temp'] = reefcontrol.getTemp(sensor['address'],sensor['correction'])
        sensor['tempavg'] = reefcontrol.getTempAvg(static+'temp.txt',int(sensor['csvid']),sensor['correction'])
    outletStatus = reefcontrol.outletStatus(outlets)
    return render_template('index.html',outletStatus=outletStatus,sensors=sensors, coolingStatus=coolingStatus)


#Turn all outlets on.
@app.route('/on/', methods=['POST'])
def on():
    reefcontrol.allOn(outlets)
    return redirect("/", code=302)


#Turn all outlets off.
@app.route('/off/', methods=['POST'])
def off():
    reefcontrol.allOff(outlets)
    return redirect("/", code=302)


#Turn off defined outlets for feeding time.
@app.route('/feed/', methods=['POST'])
def feed():
    reefcontrol.feed(outlets)
    return redirect("/", code=302)


#Control individual outlets.
@app.route('/outletControl/', methods=['POST'])
def outletControl():
    pin=request.form['pin']
    action=request.form['action']
    reefcontrol.outletControl(action,pin)
    return redirect("/", code=302)


#Run it!
if __name__ == "__main__":
    	app.run(host='0.0.0.0',port=5000,debug=True)