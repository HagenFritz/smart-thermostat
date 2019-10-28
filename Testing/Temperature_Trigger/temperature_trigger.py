#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:39:26 2019

@author: hagenfritz
"""

import RPi.GPIO as GPIO
from time import sleep
import board
import busio
import adafruit_sht31d

# ----- #
# Setup #
# --------------------------------------------------------------------------- #

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# red LED
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,False)
# blue LED
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,False)
# T/RH sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)
# SG90 Servo
## Specifics to the servo
cooling_duty = 2.2
heating_duty = 12.4
center = (heating_duty+cooling_duty)/2
## Pin setup
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
## Create PWM channel on the servo pin with a frequency of 50Hz
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(center)


try:
    while True:
        tc = sensor.temperature
        print('Temperature',tc)
        if tc > 22: # if the button has been pushed
            GPIO.output(17,True)
            pwm_servo.ChangeDutyCycle(heating_duty)
        elif tc < 20:
            GPIO.output(27,True)
            pwm_servo.ChangeDutyCycle(cooling_duty)
        else:
            GPIO.output(17,False)
            GPIO.output(27,False)
            pwm_servo.ChangeDutyCycle(center)
        
        sleep(5)
            
except KeyboardInterrupt:
    # resets GPIOs
    GPIO.cleanup()