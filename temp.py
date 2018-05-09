from ds18b20 import DS18B20
import time
import datetime
import json
import os.path

if os.path.isfile('static/temp.txt'):
	pass	
else:
	file = open("static/temp.txt","w")
	file.write("Date,Temp1,Temp2\n")
	file.close()

while True:
	try:
		currentDT = datetime.datetime.now()

		sensor1 = DS18B20('0317200b1bff')
		temp1 = sensor1.get_temperature(DS18B20.DEGREES_F)

		sensor2 = DS18B20('0417207e4eff')
		temp2 = sensor2.get_temperature(DS18B20.DEGREES_F)

		data = currentDT.strftime("%m-%d-%Y %I:%M:%S %p")+','+str(temp1)+','+str(temp2)+'\n'
		
		file = open("static/temp.txt","a")
		file.write(data)
		file.close()

		time.sleep(15)
	except KeyboardInterrupt:
		break
	except:
		pass