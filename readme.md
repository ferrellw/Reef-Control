# Reef Tank Power Control

This is a quick project I put together to control an 8 channel power relay connected to a Raspberry Pi. This relay controls various aquarium equipment. The Pi is also monitoring temperature using DS18B20 probes. I plan to add support for ph probes, light timers, and more. 

## Getting Started

The files in this project will get you up and running with a web based portal where you can toggle outlets, get the status of outlets, view temperatures, and cooling status.

### Prerequisites

You will then need a Raspberry Pi, an appropriate relay, and wiring. You can view pictures of my build [here](https://photos.app.goo.gl/66KXyf0TYG3iR5cI2).

Here are the parts used in my build.
* Raspberry Pi B+: [Link](https://www.amazon.com/gp/product/B07BDRD3LP/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
* 8 channel power relay: [Link](https://www.amazon.com/gp/product/B01HCFJC0Y/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)
* DS18B20 Sensor: [Link](https://www.amazon.com/gp/product/B01LY53CED/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)

Here are some links I used to help get my build completed.
* Wiring a DS18B20 sensor: [Link](http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/)
* Wiring for multiple DS18B20 sensors: [Link](https://www.raspberrypi.org/forums/viewtopic.php?t=167896)
* GPIO pin reference: [Link](https://i.stack.imgur.com/KL4PZ.png) 

### App Dependencies
This app relies on two other python scripts responsible for logging temperature values to a csv and controlling an outlet for cooling purposes. When using the `supervisord.conf` provided these scripts will run automatically. Otherwise you will need to ensure `scripts/templogger.py` and `/scripts/tempcontroller.py` are running for proper operation.

### Python Dependencies

This app is written in Python and uses Flask with a few other modules. You will need to install the below modules.
```
pip install flask
pip install DS18B20
```  

## Configuration 
Once your build is setup you will need to edit `outlets.json` and `sensors.json` to reflect your pin configuration and sensor I2C sensor addresses.

 `outlets.json` and `sensors.json` contain the information that will be passed to functions within the app. The schema is as follows.

`outlets.json`

      [{
    	"status": "", ##Will be used in the app to display status.
    	"feed": "", ##Determines if outlet is used for feeding.
    	"name": "Outlet 1", ##Friendly name of outlet.
    	"pin": "13", ##GPIO pin the outlet/relay is connected to.
    	"desc": "Free" ##Description of what is plugged into the outlet.
    }]

`sensors.json`

    [{
	"name": "Sensor 1", ##Friendly name of sensor.
	"address": "0317200b1bff", ##I2C address of Sensor.
	"temp": "", ##Will be used in the app to display temperature.
	"tempavg": "", ##Will be used in the app to display temperature averages.
	"csvid": "1", ##Column in which the sensor in /static/temp.txt.
	"correction": 0.22, ##Correction of sensor, if needed.
	"threshold": 77, ##Temperature threshold. Used for cooling functions.
	"coolingpin": 21, ##GPIO pin used to trigger fans.
	"coolingStatus": "" ##Used in the app to display status of cooling fans.
	}]
	
## Running

I am running this app via Supervisor. To get up and running quickly, you can run:
```
python app.py
```
Note that the app by default has debug enabled. When running via supervisor debug is disabled.

## Notes
* As stated before I am using Supervisor to run Flask. My `supervisord.conf` file is included under [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/supervisord).
* I am using [amazon-dash](https://github.com/Nekmo/amazon-dash) for an IoT Amazon dash button to control outlet groups. This config is also included in [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/amazon-dash).
* In the even of a power failure the outlets default to on. I am using `systemd` for this. The unit file and script to power on the outlets is once again, included in [misc](https://github.com/ferrellw/ReefTankPowerControl/tree/master/misc/systemd).