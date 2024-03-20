#This is a simple test that will turn on and off our relay
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

RELAIS_1_GPIO = 11
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

sleep(5.0)
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
GPIO.cleanup()
