import pigpio
import sys
import time
import traceback

PIN_MOTORR_LEGA = 1 # Motor Right Leg A
PIN_MOTORR_LEGB = 2 # Motor Right Leg B
PIN_MOTORL_LEGA = 3 # Motor Left Leg A
PIN_MOTORL_LEGB = 4 # Motor Left Leg B

class Motor:
	def __init__(self, io, pinA, pinB):			
		self.pinA = pinA
		self.pinB = pinB

		io.set_mode(pinA, pigpio.OUTPUT)
		io.set_mode(pinB, pigpio.OUTPUT)
		io.set_PWM_frequency(pinA, 1000)
		io.set_PWM_frequency(pinB, 1000)
		io.set_PWM_range(self.pinA, 255)
		io.set_PWM_range(self.pinB, 255)
		
	def off(self):
		io.set_PWM_dutycycle(self.pinA, 0)
		io.set_PWM_dutycycle(self.pinB, 0)
		io.set_PWM_range(self.pinA, 0)
		io.set_PWM_range(self.pinB, 0)
	
	# level is in between -1.0 and 1.0
	def setlevel(self, level):
		io.set_PWM_range(self.pinA, level * 255)
		io.set_PWM_range(self.pinB, level * 255)
	
class Robot:
	def __init__(self, motorR, motorL):
		self.motorR = motorR
		self.motorL = motorL

		print("Motors ready...")
		
	def stop_motors(self):
		motorR.off()
		motorL.off()
	
	def forward(self, dt, speed):
		start_time = time.time()

		while (time.time() - start_time) < dt:
			# move robot forward 1 m by setting the dutycycle of both motor's pinA to be greater than pinB
		
		stop_motors()
		
	def right_turn(self, deg):
		# turn robot right by setting diff in left motor's pin to be greater than right motor's pin

		stop_motors()

	
	def square(self):
		for i in range(4):
			forward(ONE_METER_TIME, 1.0)
			right(90)
	
ONE_METER_TIME = # constant

motorR = Motor()
motorL = Motor()
crab = Robot(motorR, motorL)

crab.forward(ONE_METER_TIME, 1.0)
crab.right_turn()
crab.square()

if __name__ == "main":
	# Prepare the GPIO interface/connection (to command the motors).
	print("Setting up the GPIO...")
	io = pigpio.pi()
	if not io.connected:
	print("Unable to connection to pigpio daemon!")
	sys.exit(0)
	print("GPIO ready...")

	# Set up the four pins as output (commanding the motors).

	