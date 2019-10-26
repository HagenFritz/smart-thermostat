# servo_scan.py - Test functionality of SG90 Micro Servo
#
# Written By: David Such
# Modified By: Hagen Fritz

import RPi.GPIO as GPIO
import time

MIN_DUTY = 2.2
MAX_DUTY = 12.4
CENTRE = MIN_DUTY + (MAX_DUTY - MIN_DUTY) / 2

servo_pin = 18
duty_cycle = CENTRE     # Should be the centre for a SG90

# Configure the Pi to use pin names (i.e. BCM) and allocate I/O
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM channel on the servo pin with a frequency of 50Hz
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)

try:
    while True:
        pwm_servo.ChangeDutyCycle(MIN_DUTY)
        time.sleep(0.5)
        pwm_servo.ChangeDutyCycle(CENTRE)
        time.sleep(0.5)
        pwm_servo.ChangeDutyCycle(MAX_DUTY)
        time.sleep(0.5)
        pwm_servo.ChangeDutyCycle(CENTRE)
        time.sleep(0.5)
            
except KeyboardInterrupt:
    print("Terminating program.")
finally:
    print("Cleaning up GPIO...")
    pwm_servo.ChangeDutyCycle(CENTRE)
    time.sleep(0.5)
    GPIO.cleanup()
