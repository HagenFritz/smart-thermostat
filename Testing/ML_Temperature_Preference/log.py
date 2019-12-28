#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:00:58 2019
@author: hagenfritz
"""

import RPi.GPIO as GPIO
import time
from datetime import datetime
from random import randint

def led_flash(pin):
	'''
	Turns the LED on for a fraction of a second.
	Input:
		- pin: integer specifying the pin to turn on and off
	'''
	sleep_time = 0.2
	GPIO.output(pin,GPIO.LOW)
	time.sleep(sleep_time)
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(sleep_time)

def light(colors):
	'''
	Chooses a light to turn on
	'''
	num = randint(0,3)

GPIO.setmode(GPIO.BCM)

# LED
led_pins = [23,24,26,16,6,5,25]
for pin in led_pins:
	GPIO.setwarnings(False)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)

# Push Button
button_pins = [17,27]
for pin in button_pins:
	GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(pin,GPIO.RISING,bouncetime=200)

color_pins = {'white':26,'blue':16,'green':6,'yellow':5,'red':25}

try:
	while True:
		if datetime.now().hour % 2 == 0:
			GPIO.output(color_pins['blue'],GPIO.LOW)
		elif datetime.now().hour % 3 == 0:
			GPIO.output(color_pins['green'],GPIO.LOW)
		elif datetime.now().hour % 5 == 0:
			GPIO.output(color_pins['yellow'],GPIO.LOW)
		elif datetime.now().hour % 7 == 0:
			GPIO.output(color_pins['green'],GPIO.LOW)
		else:
			GPIO.output(color_pins['white'],GPIO.LOW)

		# Red Button
		if GPIO.event_detected(button_pins[0]):
			led_flash(led_pins[0])

		# Green Button
		if GPIO.event_detected(button_pins[1]):
			led_flash(led_pins[1])
            
except KeyboardInterrupt:
	# resets GPIOs
	GPIO.cleanup()
