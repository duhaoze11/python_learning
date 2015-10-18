#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
#引脚采用BCM编码
GPIO.setmode(GPIO.BCM)

led = [21, 16, 19, 6, 5, 20, 26, 13]
pins = [17, 27, 22, 10]
num = [[0, 1, 2, 3, 4, 5], [1, 2], [0, 1, 3, 4 ,6], [0, 1, 2, 3, 6], [1, 2, 5, 6], [0, 2, 3, 5, 6], [0, 2, 3, 4, 5, 6], [0, 1, 2], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 5, 6]]

def init() :	
	for i in pins :
		GPIO.output(i, GPIO.HIGH)
		time.sleep(0.1)
		for j in led :
			GPIO.output(j, GPIO.HIGH)
			time.sleep(0.1)

def output(i) :
	GPIO.output(i, GPIO.LOW)
	print("%d\n" % i)

def layout(x) :
	for i in num[x] :
		output(led[i])
def clean() :
	for i in range(8) :
		GPIO.output(led[i], GPIO.HIGH)
		
for i in pins :
	GPIO.setup(i, GPIO.OUT)
for j in led :
	GPIO.setup(j, GPIO.OUT)

init()
GPIO.output(pins[3], GPIO.LOW)
GPIO.output(pins[2], GPIO.LOW)
GPIO.output(pins[1], GPIO.LOW)
GPIO.output(pins[0], GPIO.LOW)

while True :
	for x in range(10) :
		layout(x)
		time.sleep(0.5)
		clean()	
