from ds18b20 import DS18B20
import time
import datetime
import os.path


#File setup.
if os.path.isfile(os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/static/temp.txt"):
	pass	
else:
	file = open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)+"/static/temp.txt"),"w")
	file.write("Date,Temp1,Temp2\n")
	file.close()


#Sesnor deffinition.
sensor1 = DS18B20('0317200b1bff')
sensor2 = DS18B20('0417207e4eff')


#Correct temprature difference between sensors.
calibration = float(0.25)


#Loop so we are always running.
while True:
	try:
		currentDT = datetime.datetime.now()
		temp1 = sensor1.get_temperature(DS18B20.DEGREES_F) - calibration
		temp2 = sensor2.get_temperature(DS18B20.DEGREES_F)
		data = currentDT.strftime("%m-%d-%Y %I:%M:%S %p")+','+str(temp1)+','+str(temp2)+'\n'
		file = open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)+"/static/temp.txt"),"a")
		file.write(data)
		file.close()
		time.sleep(15)
	except KeyboardInterrupt:
		break
	except:
		pass