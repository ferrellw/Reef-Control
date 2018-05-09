from ds18b20 import DS18B20
import time
import RPi.GPIO as GPIO


#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#Sensor deffinition.
sensor1 = DS18B20('0317200b1bff')
sensor2 = DS18B20('0417207e4eff')


#Correct temprature difference between sensors.
calibration = float(0.3)


#Set thresholds
threshold = float(76.5)


#Loop so we are always running.
while True:
	try:
		#Define temp vars for later use.
		temp1 = sensor1.get_temperature(DS18B20.DEGREES_F) - calibration
		temp2 = sensor2.get_temperature(DS18B20.DEGREES_F)
		#Compare reading of both sensors to threshold. If either are over, turn on the outlet.
		if (temp1 >= threshold) or (temp2 >= threshold):
			print "Temp is above threshold of: "+str(threshold)+". Temp: "+str(temp1)+","+str(temp2)
			GPIO.setup(21, GPIO.OUT)
			#Lets sleep for 3 min to let the cooling action happening. This is so the realy isnt triggered every 15 seconds.
			time.sleep(180)
		#If we are under the threshold turn off the outlet. 		
		else:
			print "Temp is below threshold of: "+str(threshold)+". Temp: "+str(temp1)+","+str(temp2)
			GPIO.setup(21, GPIO.IN)
		time.sleep(15)
	except KeyboardInterrupt:
		break
	except:
		pass