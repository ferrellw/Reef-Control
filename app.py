import sys
import subprocess
import os
from flask import Flask, render_template, request, url_for, redirect
import json
scripts = (os.getcwd()+"/scripts/")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats/')
def stats():
    outlets = '[{"name": "Output Group 1","pin": "20","status": "","feed": ""},{"name": "Output Group 2","pin": "26","status": "","feed": ""},{"name": "Output Group 3","pin": "19","status": "","feed": ""},{"name": "Output Group 4","pin": "14","status": "","feed": ""},{"name": "Output Group 5","pin": "6","status": "","feed": "yes"},{"name": "Output Group 6","pin": "5","status": "","feed": "yes"}]'
    outlets = json.loads(outlets)
    for outlet in outlets:
        ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
        output = str(ps.communicate())
        output = output.translate(None,"\n',N('on\e) ")
        if output == "1":
            outlet['status'] = "Off"
        if output == "0":
            outlet['status'] = "On"
    return render_template('stats.html',outlets=outlets)

@app.route('/status/', methods=['POST'])
def status():
    cmd = ["python",scripts+"/power.py", "status"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/on/', methods=['POST'])
def on():
    cmd = ["python",scripts+"/power.py", "on"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/off/', methods=['POST'])
def off():
    cmd = ["python",scripts+"/power.py", "off"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/feed/', methods=['POST'])
def feed():
    cmd = ["python",scripts+"/power.py", "feed"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route('/ogcontrol/', methods=['POST'])
def ogcontrol():
    outletGroup=request.form['outletGroup']
    op=request.form['op']
    print outletGroup
    cmd = ["python",scripts+"/power.py", "outlet-control", outletGroup, op]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
    	app.run(host='0.0.0.0',port=5000,debug=True)
