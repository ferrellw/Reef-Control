from ds18b20 import DS18B20
import time
import datetime
import os.path
import json
import RPi.GPIO as GPIO


#Read config file to get outlet info.
try:
	with open(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/sensors.json") as json_sensors:
		sensors = json.load(json_sensors)
except:
	print "Failed to load sensor json config file."


#GPIO setup.
try:
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
except:
	print "Failed to setup GPIO."


#Control cooling fans.
def temperatureController(sensors):
	try:
		temps = []
		for sensor in sensors:
			temps.append(DS18B20(str(sensor['address'])).get_temperature(DS18B20.DEGREES_F) - sensor['correction'])
			threshold = sensor['threshold']
		if (temps[0] >= threshold) or (temps[1] >= threshold):
			for coolingpin in sensors:
				GPIO.setup(int(sensor['coolingpin']), GPIO.OUT)
				return "Temperature above threshold.",temps
				time.sleep(180)
		else:
			for coolingpin in sensors:
				GPIO.setup(int(sensor['coolingpin']), GPIO.IN)
				return "Temperature below threshold of",threshold,temps
	except KeyboardInterrupt:
		quit()
	except:
		return "Some sort of error. Continuing..."
		pass


#Main loop.
def main():
	while True:
		print temperatureController(sensors)
		time.sleep(5)


#Run it!
if __name__ == "__main__":
	main()