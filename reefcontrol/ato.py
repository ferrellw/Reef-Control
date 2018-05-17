import RPi.GPIO as GPIO
import time

 
def getReservoirStatus(GPIO_TRIGGER, GPIO_ECHO,capacity,upperlimit):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) 
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    try:
        avgsum = 0
        distanceList = []
        for i in range(0,5):
            GPIO.output(GPIO_TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_TRIGGER, False)
            StartTime = time.time()
            StopTime = time.time()
            while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()
            while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()
            TimeElapsed = StopTime - StartTime
            distance = (TimeElapsed * 34300) / 2
            distanceList.append(distance)
            time.sleep(.05)
        for i in distanceList:
            avgsum = (i + avgsum) 
            average = (avgsum / len(distanceList) - float(upperlimit))
        percentfull = (capacity-(average))/capacity*100
        return round(float(percentfull),0)
    except:
        return "Error getting reservoir status."


def getReservoirStatusCalibration(GPIO_TRIGGER, GPIO_ECHO):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False) 
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        StartTime = time.time()
        StopTime = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
        return distance
    except:
        return "Error getting reservoir calibration."
