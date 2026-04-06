import pigpio
import sys
import time
import traceback

# Robot Constants
RIGHT_MOTOR_PIN_A = 7
RIGHT_MOTOR_PIN_B = 8
LEFT_MOTOR_PIN_A = 6
LEFT_MOTOR_PIN_B = 5

class Motor:
    def __init__(self, io, pinA, pinB):         
        self.io = io
        self.pinA = pinA
        self.pinB = pinB
    
        self.io.set_mode(self.pinA, pigpio.OUTPUT)
        self.io.set_mode(self.pinB, pigpio.OUTPUT)
        self.io.set_PWM_frequency(self.pinA, 1000)
        self.io.set_PWM_frequency(self.pinB, 1000)
        self.io.set_PWM_range(self.pinA, 255)
        self.io.set_PWM_range(self.pinB, 255)
        self.io.set_PWM_dutycycle(self.pinA, 255)
        self.io.set_PWM_dutycycle(self.pinB, 255)

    def set_level(self, level):
        if level < 0:
            self.io.set_PWM_dutycycle(self.pinA, 255 + (level * 255))
            self.io.set_PWM_dutycycle(self.pinB, 255)
        else:
            self.io.set_PWM_dutycycle(self.pinA, 255)
            self.io.set_PWM_dutycycle(self.pinB, 255 - (level * 255))

    def off(self):
        print("Turning off")
        self.io.set_PWM_dutycycle(self.pinA, 0)
        self.io.set_PWM_dutycycle(self.pinB, 0)
    
class Robot:
    def __init__(self, leftMotor, rightMotor):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
    
    def forward(self, rightSpeed, leftSpeed, seconds):
        self.leftMotor.set_level(leftSpeed)
        self.rightMotor.set_level(-1 * rightSpeed)
        time.sleep(seconds)

        self.stop_motors(1)

    def turn(self, seconds):
        self.leftMotor.io.set_PWM_dutycycle(self.leftMotor.pinA, 255)
        self.leftMotor.io.set_PWM_dutycycle(self.leftMotor.pinB, 100)
        time.sleep(seconds)

        self.stop_motors(1)

    def stop_motors(self, seconds):
        self.leftMotor.off()
        self.rightMotor.off()
        time.sleep(seconds)

if __name__ == "__main__":
	# Prepare the GPIO interface/connection (to command the motors).
    print("Setting up the GPIO...")
    io = pigpio.pi()
    if not io.connected:
        print("Unable to connect to pigpio daemon!")
        sys.exit(0)
    print("GPIO ready...")

	# Robot setup
    leftMotor = Motor(io, LEFT_MOTOR_PIN_A, LEFT_MOTOR_PIN_B)
    rightMotor = Motor(io, RIGHT_MOTOR_PIN_A, RIGHT_MOTOR_PIN_B)
    crabBot = Robot(leftMotor, rightMotor)

    try:
        crabBot.forward(155 / 255, 155 / 255, 2.2)
        crabBot.turn(0.5)
        crabBot.forward(152 / 255, 155 / 255, 1.8)
        crabBot.turn(0.55)
        crabBot.forward(155 / 255, 153 / 255, 2.1)
        crabBot.turn(0.52)
        crabBot.forward(155 / 255, 155 / 255, 1.8)

    except BaseException as ex:
        # Report the error, but continue with the normal shutdown.
        print("Ending due to exception: %s" % repr(ex))
        traceback.print_exc()

    finally:
        crabBot.stop_motors(1)
        io.stop()
    

