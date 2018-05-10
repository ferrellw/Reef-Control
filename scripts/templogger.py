from ds18b20 import DS18B20
import time
import datetime
import os.path
import json


#Setup CSV for temperature logging.
try:
	if os.path.isfile(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/static/temp.txt"):
		pass	
	else:
		file = open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)+"/static/temp.txt"),"w")
		file.write("Date,Temp1,Temp2\n")
		file.close()
except:
	print "Failed to setup CSV for temperature logging."



#Read sensor config file to get sensor info.
try:
	with open(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/sensors.json") as json_sensors:
		sensors = json.load(json_sensors)
except:
	print "Sensor config file not found."


#Log temperatures to CSV.
def temperatureLogging(sensors):
	try:
		data = []
		currentDT = datetime.datetime.now()
		data.append(currentDT.strftime("%m-%d-%Y %I:%M:%S %p"))
		for sensor in sensors:
				data.append(str(DS18B20(str(sensor['address'])).get_temperature(DS18B20.DEGREES_F) - sensor['correction']))
		file = open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)+"/static/temp.txt"),"a")
		write = str((data[0],data[1],data[2]))+"\n"
		write = write.translate(None,"(')")
		file.write(write)
		file.close()
		time.sleep(15)
	except KeyboardInterrupt:
		quit()
	except:
		pass


#Main loop.
def main():
	while True:
		temperatureLogging(sensors)


#Run it!
if __name__ == "__main__":
	main()