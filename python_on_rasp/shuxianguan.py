#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
#引脚采用BCM编码
GPIO.setmode(GPIO.BCM)

led = [21, 16, 19, 6, 5, 20, 26, 13]
pins = [17, 27, 22, 10]

def init() :	
	for i in pins :
		GPIO.output(i, GPIO.HIGH)
		time.sleep(0.1)
		for j in led :
			GPIO.output(j, GPIO.HIGH)
			time.sleep(0.1)
def output(i) :
	GPIO.output(pins[i], GPIO.LOW)
	for j in led :
		GPIO.output(j, GPIO.LOW)
		print("%d\n" % j)
		raw_input()
		
		
for i in pins :
	GPIO.setup(i, GPIO.OUT)
for j in led :
	GPIO.setup(j, GPIO.OUT)

while True :
	init()
	i = 0
	output(i)
	i += 1
	i %= 8

	
				
