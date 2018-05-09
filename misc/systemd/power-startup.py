import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
print "Turning off outlets..."
time.sleep(1)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(16, GPIO.IN)
print "Turning on outlets..."
time.sleep(1)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
