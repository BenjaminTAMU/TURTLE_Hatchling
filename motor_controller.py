import RPi.GPIO as GPIO

class motor_control:
    def __init__(self, in_one, in_two, en):
        self.in_one = in_one
        self.in_two = in_two
        self.en = en

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in_one,GPIO.OUT)
        GPIO.setup(self.in_two,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in_one,GPIO.LOW)
        GPIO.output(self.in_two,GPIO.LOW)

        motor = GPIO.PWM(self.en,1000)