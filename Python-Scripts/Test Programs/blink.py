import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
try:
	while True:
		GPIO.output(8, GPIO.HIGH)
		sleep(1)
		GPIO.output(8, GPIO.LOW)
		GPIO.output(10, GPIO.HIGH)
		sleep(1)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(12, GPIO.HIGH)
		sleep(1)
		GPIO.output(12, GPIO.LOW)

except KeyboardInterrupt:
	GPIO.output(8, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
