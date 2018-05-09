import sys
import subprocess
import json
import os
from flask import Flask, render_template, request, url_for, redirect

#Location of main script, power.py
scripts = (os.getcwd()+"/scripts/")

app = Flask(__name__)
    

#Main page.
@app.route('/')
def index():
    ##Lets get the status for the outlets.
    #Define outlets. This list should match what is in power.py.
    outlets = '[{"name": "Outlet Group 1","pin": "13","status": "","feed": "","form": "og1","desc":"Free"},{"name": "Outlet Group 2","pin": "19","status": "","feed": "","form": "og2","desc":"Refugium Light"},{"name": "Outlet Group 3","pin": "26","status": "","feed": "","form": "og3","desc":"Power Head Controller"},{"name": "Outlet Group 4","pin": "21","status": "","feed": "","form": "og4","desc":"Cooling Fan"},{"name": "Outlet Group 5","pin": "20","status": "","feed": "yes","form": "og5","desc":"Auto Top Off"},{"name": "Outlet Group 6","pin": "16","status": "","feed": "yes","form": "og6","desc":"Return Pump, Protein Skimmer"}]'
    outlets = json.loads(outlets)
    #Loop over each item in the list.
    for outlet in outlets:
        #Get the status of the GPIO pin for each outlet.
        ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
        output = str(ps.communicate())
        #Output is not boolean. Lets fix that.
        output = output.translate(None,"\n',N('on\e) ")
        #Update the list to reflect status of outlet.
        if output == "1":
            outlet['status'] = "Off"
            outlet['selected'] = "selected"
        if output == "0":
            outlet['status'] = "On"
        #Now that we have the status of the outlets, present to the template for rendering.
    return render_template('index.html',outlets=outlets)


#Main page.
@app.route('/pi/')
def pi():
    ##Lets get the status for the outlets.
    #Define outlets. This list should match what is in power.py.
    outlets = '[{"name": "Outlet Group 1","pin": "13","status": "","feed": "","form": "og1","desc":"Free"},{"name": "Outlet Group 2","pin": "19","status": "","feed": "","form": "og2","desc":"Refugium Light"},{"name": "Outlet Group 3","pin": "26","status": "","feed": "","form": "og3","desc":"Power Head Controller"},{"name": "Outlet Group 4","pin": "21","status": "","feed": "","form": "og4","desc":"Cooling Fan"},{"name": "Outlet Group 5","pin": "20","status": "","feed": "yes","form": "og5","desc":"Auto Top Off"},{"name": "Outlet Group 6","pin": "16","status": "","feed": "yes","form": "og6","desc":"Return Pump, Protein Skimmer"}]'
    outlets = json.loads(outlets)
    #Loop over each item in the list.
    for outlet in outlets:
        #Get the status of the GPIO pin for each outlet.
        ps = subprocess.Popen(('gpio', '-g', 'read', outlet['pin']), stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
        output = str(ps.communicate())
        #Output is not boolean. Lets fix that.
        output = output.translate(None,"\n',N('on\e) ")
        #Update the list to reflect status of outlet.
        if output == "1":
            outlet['status'] = "Off"
            outlet['selected'] = "selected"
        if output == "0":
            outlet['status'] = "On"
        #Now that we have the status of the outlets, present to the template for rendering.
    return render_template('pi.html',outlets=outlets)


# @app.route('/status/', methods=['POST'])
# def status():
#     cmd = ["python",scripts+"/power.py", "status"]
#     p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
#     out,err = p.communicate()
#     return out

@app.route('/on/', methods=['POST'])
def on():
    cmd = ["python",scripts+"/power.py", "on"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return redirect("/", code=302)

@app.route('/off/', methods=['POST'])
def off():
    cmd = ["python",scripts+"/power.py", "off"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return redirect("/", code=302)

@app.route('/feed/', methods=['POST'])
def feed():
    cmd = ["python",scripts+"/power.py", "feed"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return redirect("/", code=302)

@app.route('/ogcontrol/', methods=['POST'])
def ogcontrol():
    outletGroup=request.form['outletGroup']
    op=request.form['op']
    print outletGroup
    cmd = ["python",scripts+"/power.py", "outlet-control", outletGroup, op]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    out,err = p.communicate()
    return redirect("/", code=302)

if __name__ == "__main__":
    	app.run(host='0.0.0.0',port=80,debug=True)
