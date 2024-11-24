import RPi.GPIO as GPIO
import time

class motor_control:
    def __init__(self, in_one, in_two, en, pwm_freq=1000):
        self.in_one = in_one
        self.in_two = in_two
        self.en = en

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in_one, GPIO.OUT)
        GPIO.setup(self.in_two, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)

        GPIO.output(self.in_one, GPIO.LOW)
        GPIO.output(self.in_two, GPIO.LOW)

        self.motor = GPIO.PWM(self.en, pwm_freq)
        self.motor.start(0)
    
    def __del__(self):
        self.motor.stop()
        GPIO.cleanup(self.in_one)
        GPIO.cleanup(self.in_two)
        GPIO.cleanup(self.en)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        del self
    
    def forward(self, speed_percentage = 50):
        self.set_speed(speed_percentage)
        GPIO.output(self.in_one, GPIO.HIGH)
        GPIO.output(self.in_two, GPIO.LOW)

    def backwards(self, speed_percentage = 50):
        self.set_speed(speed_percentage)
        GPIO.output(self.in_one, GPIO.LOW)
        GPIO.output(self.in_two, GPIO.HIGH)
    
    def set_speed(self, speed_percentage):
        speed_percentage = max(0, min(100, speed_percentage))
        self.motor.ChangeDutyCycle(speed_percentage)
    
    def stop(self):
        self.motor.ChangeDutyCycle(0)
        GPIO.output(self.in_one, GPIO.LOW)
        GPIO.output(self.in_two, GPIO.LOW)

# For testing
if __name__ == "__main__":
    with motor_control(17, 27, 22) as LED:
        LED.forward(10)
        time.sleep(3)
        LED.stop()
