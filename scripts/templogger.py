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


#Read temperature sensor config file to get sensor info.
try:
	with open(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/config/temperaturesensors.json") as json_temperaturesensors:
		temperaturesensors = json.load(json_temperaturesensors)
except:
	print "Temperature Sensor config file not found."


#Log temperatures to CSV.
while True:
	try:
		data = []
		currentDT = datetime.datetime.now()
		data.append(currentDT.strftime("%m-%d-%Y %I:%M:%S %p"))
		for temperaturesensor in temperaturesensors:
				data.append(str("%.1f" % (DS18B20(str(temperaturesensor['address'])).get_temperature(DS18B20.DEGREES_F) + temperaturesensor['temperaturecorrection'])))
		file = open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)+"/static/temp.txt"),"a")
		write = str((data[0],data[1],data[2]))+"\n"
		write = write.translate(None,"(')")
		file.write(write)
		file.close()
		print data
		time.sleep(30)
	except KeyboardInterrupt:
		quit()
	except:
		print "Error logging temperatures."
		time.sleep(1)
		pass