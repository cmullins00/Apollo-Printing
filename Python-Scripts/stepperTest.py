#System imports
import RPi.GPIO as GPIO
from time import sleep

class StepperHandler():

	__CLOCKWISE = 1
	__ANTI_CLOCKWISE = 0

	def __init__(self,stepPin,directionPin,delay=0.5, stepsPerRevolution=400):

		#Configure instance
		self.CLOCKWISE = self.__CLOCKWISE
		self.ANTI_CLOCKWISE = self.__ANTI_CLOCKWISE
		self.StepPin = stepPin
		self.DirectionPin = directionPin
		self.Delay = delay
		self.RevolutionSteps = stepsPerRevolution
		self.CurrentDirection = self.CLOCKWISE
		self.CurrentStep = 0

		#setup gpio pins
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.StepPin,GPIO.OUT)
		GPIO.setup(self.DirectionPin,GPIO.OUT)

	def Step(self,stepsToTake, direction = __ANTI_CLOCKWISE):

		print("Step pin: " +str(self.StepPin) + " Direction Pin: " + str(self.DirectionPin) + " Delay: " + str(self.Delay))
		print("Taking " + str(stepsToTake) + " steps.")

		#set the direction
		GPIO.output(self.DirectionPin, direction)

		#take number of requested steps
		for x in range(stepsToTake):
			print("Step " + str(x))
			GPIO.output(self.StepPin, GPIO.HIGH)
			self.CurrentStep += 1
			sleep(self.Delay)
			GPIO.output(self.StepPin, GPIO.LOW)
			sleep(self.Delay)
		

x = StepperHandler(6,12)
x.Step(10000)