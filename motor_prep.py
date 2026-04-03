import pigpio
import sys
import time
import traceback

# Robot Constants
RIGHT_MOTOR_PIN_A = 1
RIGHT_MOTOR_PIN_B = 2
LEFT_MOTOR_PIN_A = 3
LEFT_MOTOR_PIN_B = 4

# Driving Goal Constants
ONE_METER_TIME = 10 # seconds

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
		self.motorR.off()
		self.motorL.off()
	
	# def forward(self, dt, speed):
	# 	start_time = time.time()

	# 	while (time.time() - start_time) < dt:
	# 		# move robot forward 1 m by setting the dutycycle of both motor's pinA to be greater than pinB
		
	# 	stop_motors()
		
	# def right_turn(self, deg):
	# 	# turn robot right by setting diff in left motor's pin to be greater than right motor's pin

	# 	stop_motors()

	
	# def square(self):
	# 	for i in range(4):
	# 		forward(ONE_METER_TIME, 1.0)
	# 		right(90)
	

if __name__ == "main":
	# Prepare the GPIO interface/connection (to command the motors).
	print("Setting up the GPIO...")
	io = pigpio.pi()
	if not io.connected:
		print("Unable to connection to pigpio daemon!")
		sys.exit(0)
	print("GPIO ready...")

	# Robot setup
	motorR = Motor(io, RIGHT_MOTOR_PIN_A, RIGHT_MOTOR_PIN_B)
	motorL = Motor(io, LEFT_MOTOR_PIN_A, LEFT_MOTOR_PIN_B)
	crab = Robot(motorR, motorL)

	try:
		crab.forward(ONE_METER_TIME, 1.0)
		crab.right_turn()
		crab.square()
	except BaseException as ex:
		# Report the error, but continue with the normal shutdown.
		print("Ending due to exception: %s" % repr(ex))
		traceback.print_exc()
	
	crab.stop_motors()
	