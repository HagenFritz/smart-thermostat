#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:00:58 2019
@author: hagenfritz
"""

import RPi.GPIO as GPIO
from time import sleep

def led_flash(pin):
	'''
	Turns the LED on for a fraction of a second.
	Input:
		- pin: integer specifying the pin to turn on and off
	'''
	sleep_time = 0.2
	GPIO.output(pin,GPIO.LOW)
	sleep(sleep_time)
	GPIO.output(pin,GPIO.HIGH)
	sleep(sleep_time)

GPIO.setmode(GPIO.BCM)
# LED
led_pins = [23,24,25]
for pin in led_pins:
	GPIO.setwarnings(False)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)
# Push Button
button_pins = [17,27,22]
for pin in button_pins:
	GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(pin,GPIO.RISING,bouncetime=200)
# Fan
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,False)

try:
	while True:
		# Red Button
		if GPIO.event_detected(button_pins[0]):
			led_flash(led_pins[0])
			GPIO.output(8,True)
			sleep(0.5)
			GPIO.output(8,False)

		# White Button
		if GPIO.event_detected(button_pins[1]):
			led_flash(led_pins[1])

		# Blue Button
		if GPIO.event_detected(button_pins[2]):
			led_flash(led_pins[2])
            
except KeyboardInterrupt:
	# resets GPIOs
	GPIO.cleanup()
