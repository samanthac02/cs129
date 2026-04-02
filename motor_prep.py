import time

class Motor:
	def __init__(self, pinA, pinB):
		self.pinA = pinA
		self.pinB = pinB
		
	def off(self):
		io.set_PWM_dutycycle(self.pinA, 0)
		io.set_PWM_dutycycle(self.pinB, 0)
	
	# level is within -1.0 and 1.0
	def setlevel(self, level):
		# set level
	
class Robot:
	def __init__(self, motorR, motorL):
		self.motorR = motorR
		self.motorL = motorL
		
	def forward(self, dt, speed):
		start_time = time.time()

		while (time.time() - start_time) < dt:
			# move robot forward 1 m by setting the dutycycle of both motor's pinA to be greater than pinB
		
		motorR.off()
		motorL.off()
		
	def right_turn(self, deg):
		# turn robot right by setting diff in left motor's pin to be greater than right motor's pin
	
	def square(self):
		for i in range(4):
			forward(ONE_METER_TIME, 1.0)
			right()
	
ONE_METER_TIME = # constant

motorR = Motor()
motorL = Motor()
crab = Robot(motorR, motorL)

crab.forward(ONE_METER_TIME, 1.0)
crab.right_turn()
crab.square()


	