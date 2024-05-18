import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
	GPIO.output(24, 1)
	sleep(5.0)
	GPIO.output(24, 0)
	sleep(0.5)
finally:
	GPIO.cleanup()
