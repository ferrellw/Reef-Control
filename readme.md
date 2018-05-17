
# Reef Tank Power Control

This is a quick project I put together to control an 8 channel power relay connected to a Raspberry Pi. This relay controls various aquarium equipment. The Pi is also monitoring temperature using DS18B20 probes. I plan to add support for ph probes, light timers, and more. 

## Getting Started

The files in this project will get you up and running with a web based portal where you can toggle and get the status of outlets, view temperatures and trends, view cooling status, and monitor your ATO (Auto Top Off) reservoir level.

## Prerequisites
### Build
You will need a Raspberry Pi, an appropriate relay, wiring, and sensors. You can view pictures of my build [here](https://photos.app.goo.gl/66KXyf0TYG3iR5cI2).

Here are the parts used in my build.
* Raspberry Pi B+: [Link](https://www.amazon.com/gp/product/B07BDRD3LP/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
* 8 channel power relay: [Link](https://www.amazon.com/gp/product/B01HCFJC0Y/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
* DS18B20 Sensor: [Link](https://www.amazon.com/gp/product/B01LY53CED/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
* HC-SR04 Ultrasonic Sensor: [Link](https://www.amazon.com/gp/product/B01MA4O5G5/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)

Here are some links I used to help get my build completed.
* Wiring a DS18B20 sensor: [Link](http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)
* Wiring for multiple DS18B20 sensors: [Link](https://www.raspberrypi.org/forums/viewtopic.php?t=167896)
* GPIO pin reference: [Link](https://i.stack.imgur.com/KL4PZ.png) 
* HC-SR04 wiring: [Link](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)


##  Dependencies
#### Python
This app is written in Python and uses Flask with a few other modules that should be pre-installed. You will need to install the below modules.
```
pip install flask
pip install DS18B20
```  
#### Application
This application relies on [Supervisor](http://supervisord.org/) to ensure processes are running and autostart with the OS. Install supervisor by running:
```
sudo apt-get install supervisor
systemctl enable supervisor.service
```
Once installed ensure Supervisor is configured to run the application and its scripts. You can find my `supervisord.conf` [here.](https://github.com/ferrellw/Reef-Control/blob/master/misc/supervisord/supervisord.conf) 

## Configuration 
Once your build is complete we need to tell the application what pins are connected to each sensor or relay. The configuration files can be found under [config.](https://github.com/ferrellw/Reef-Control/tree/master/config)
### Outlets
 `outlets.json` contains information that the application needs to control the relay. This relay switches power on and off to the outlets. 

      [{
    	"name": "Outlet 1", ##Friendly name of outlet.
    	"desc": "Protein Skimmer", ##Description of what is plugged into the outlet.
    	"status": "", ##Will be used in the app to display the outlets status.
    	"pin": "13", ##GPIO pin the outlet/relay is connected to.
    	"feed": "" ##Determines if outlet is used for feeding.
    }]
### Temperature Sensors
`temperaturesensors.json` contains information that the application needs to sense temperature and trigger cooling if configured. Currently the application only supports 2 temperature sensors. Once your sensors are setup you can find their addresses by running: 

```ls /sys/bus/w1/devices/```

    [{
	"type": "temperature", ##The type of sensor.
	"name": "Overflow", ##Friendly name of the sensor.
	"address": "0417207e4eff", ##I²C sensor address. See above for command to locate this.
	"temperature": "", ##This will be populated in the application.
	"temperatureaverage": "", ##This will be populated in the application.
	"csvid": "2", ##The index used when reading from the CSV to get the average temperature.
	"temperaturecorrection": 1.04, ##Temperature correction amount.
	"temperaturethreshold": 77, ##Threshold at which we turn on cooling.
	"pin": 21, ##Pin we toggle with we reach the threshold above.
	"pinstatus": "" ####This will be populated in the application. Tells us if coolling is on or off.
	}]
	
	
### Processes
`processes.json` contains information that the application needs to track the status of processes. The app does not start or stop services it only tells you their status.

    [{
	"type": "Python", ##The type of process.
	"name": "tempcontroller.py", ##The name of the process.
	"command": "python tempcontroller.py", ##The command used to invoke the process.
	"pid": "", ##The PID of the process. Populated by the application.
	"status": "" ##The status of the process. Populated by the app.
	}]

### ATO
`ato.json` contains information that the application needs to sense the level of the ATO reservoir.

    [{
	"type": "ultrasonic", ##The type of sensor.
	"name": "ATO Reservoir", ##Friendly name of the sensor.
	"triggerpin": 18, ##The pin used to send pulses.
	"echopin": 24, ##The pin used to listen for pulses.
	"capacity": 39.5, ##Measured empty "capacity" of the reservoir. Measurements are in CM.
	"uppercorrection": 6.5, ##Correction to account for the distace between the sensor and the level of the water at 100% capacity.
	"percentfull": "" ####This will be populated in the application.
	}]


## Running

I am running the application via Supervisor. To get up and running quickly, you can run:
```
python app.py
```
This will start the application in debug mode on 0.0.0.0:5001.


## Notes
* As stated before I am using Supervisor to run Flask. My `supervisord.conf` file is included under [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/supervisord).
* I am using [amazon-dash](https://github.com/Nekmo/amazon-dash) for an IoT Amazon dash button to control outlet groups. This config is also included in [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/amazon-dash).
* In the even of a power failure all outlets default to an on status. I am using `systemd` for this. The unit file and script to power on the outlets is once again, included in [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/systemd).
## Built With
* [Flask](http://flask.pocoo.org/) - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
* [ds18b20](https://github.com/rgbkrk/ds18b20) - This little pure python module provides a single class to get the temperature of a DS18B20 sensor.
* [SB Admin 2](https://startbootstrap.com/template-overviews/sb-admin-2/) - A Bootstrap admin theme, dashboard, or web app UI featuring powerful jQuery plugins for extended functionality.
* [dygraphs](http://dygraphs.com/) - dygraphs is a fast, flexible open source JavaScript charting library.