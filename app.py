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
with open('config.json') as json_config:
    outlets = json.load(json_config)

#Main page.
@app.route('/')
def index():
    outletStatus = reefcontrol.outletStatus(outlets)
    temp1 = reefcontrol.getTemp('0317200b1bff')
    temp2 = reefcontrol.getTemp('0417207e4eff')
    temp1avg = reefcontrol.getTempAvg(static+'temp.txt',1,0.23)
    temp2avg = reefcontrol.getTempAvg(static+'temp.txt',2,0.0)
    return render_template('index.html',outletStatus=outletStatus,temp1=temp1,temp2=temp2,temp1avg=temp1avg,temp2avg=temp2avg)

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


if __name__ == "__main__":
    	app.run(host='0.0.0.0',port=5000,debug=True)
