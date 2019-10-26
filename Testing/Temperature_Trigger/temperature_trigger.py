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

try:
    while True:
        if sensor.temperature > 22: # if the button has been pushed
            GPIO.output(17,True)
        elif sensor.temperature < 20:
            GPIO.output(27,True)
        else:
            GPIO.output(17,False)
            GPIO.output(27,False)
        
        sleep(5)
            
except KeyboardInterrupt:
    # resets GPIOs
    GPIO.cleanup()