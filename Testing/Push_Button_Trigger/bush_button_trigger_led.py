#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:00:58 2019

@author: hagenfritz
"""

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
# LED
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,False)
# Push Button
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(27,GPIO.RISING,bouncetime=200)

try:
    while True:
        if GPIO.event_detected(27): # if the button has been pushed
            activate = True
            while activate is True:
                # Light flashes
                GPIO.output(17,True)
                sleep(0.5)
                GPIO.output(17,False)
                sleep(0.5)
                if GPIO.event_detected(27):
                    activate = False
        else:
            GPIO.output(17,False)
            
except KeyboardInterrupt:
    # resets GPIOs
    GPIO.cleanup()