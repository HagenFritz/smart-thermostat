#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:00:58 2019
@author: hagenfritz
"""

import RPi.GPIO as GPIO
import time
from datetime import datetime

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

color_pins = [26,16,6,5,25]

try:
	while True:
		if datetime.now().hour < 4:
			GPIO.output(color_pins[0],GPIO.LOW)
		elif datetime.now().hour < 8:
			GPIO.output(color_pins[1],GPIO.LOW)
		elif datetime.now().hour < 12:
			GPIO.output(color_pins[2],GPIO.LOW)
		elif datetime.now().hour < 16:
			led_flash(color_pins[3])
			GPIO.output(color_pins[3],GPIO.LOW)
		else:
			print("here")
			GPIO.output(color_pins[4],GPIO.LOW)
		# Red Button
		if GPIO.event_detected(button_pins[0]):
			led_flash(led_pins[0])

		# Green Button
		if GPIO.event_detected(button_pins[1]):
			led_flash(led_pins[1])

		time.sleep(5)
            
except KeyboardInterrupt:
	# resets GPIOs
	GPIO.cleanup()
