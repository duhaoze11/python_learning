#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [5, 6, 13, 19, 0, 1, 7, 8]

#GPIO.setup(17, GPIO.OUT, initial = GPIO.HIGH)
#GPIO.setup(27, GPIO.OUT, initial = GPIO.HIGH)
#GPIO.setup(22, GPIO.OUT, initial = GPIO.HIGH)
#GPIO.setup(10, GPIO.OUT, initial = GPIO.HIGH)

def setp(n, status = 'off') :
	if status == 'on' :
		GPIO.output(n, GPIO.LOW)
	else :
		GPIO.output(n, GPIO.HIGH)

for i in pins :
	GPIO.setup(i, GPIO.OUT)
	setp(i, 'off')

try :
	i = 0
	while True :
		setp(pins[i], 'on')
		time.sleep(0.1)
		setp(pins[i], 'off')
		i += 1
		i = i % 8

except :
	print 'except'
	GPIO.cleanup()

