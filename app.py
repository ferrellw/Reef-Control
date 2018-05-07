import sys
import subprocess
import os
from flask import Flask, render_template, request, url_for, redirect
scripts = (os.getcwd()+"/scripts/")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats/')
def stats():
    return render_template('stats.html')

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
    	app.run(host='0.0.0.0',port=5000,debug=False)
