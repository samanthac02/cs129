class Motor:
	def __init__(self, pinA, pinB):
		self.pinA = 
		self.pinB = 
		
	def off(self):
		io.set_PWM_dutycycle(self.pinA, 0)
		io.set_PWM_dutycycle(self.pinB, 0)
	
	def setlevel(self, level):
	  
	
class Robot:
	def __init__(self, motorR, motorL):
		self.motorR = motorR
		self.motorL = motorL
		
	def forward(self, time, speed):
	# move robot forward 1 m by setting the dutycycle of both motor's pinA to be greater than pinB
		
	def right(self, deg):
	# turn robot right by setting diff in left motor's pin to be greater than right motor's pin
	
	def square(self):
	# call the forward function, right function 4 times
	
ONE_METER_TIME = 

DEGREE = 
motorR = Motor(
motorL = Motor(
crab = Robot(motorR, motorL)
crab.forward(ONE_METER_TIME, )
crab.right()
crab.square()


	