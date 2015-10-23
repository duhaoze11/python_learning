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

def layout(p, x) :
	GPIO.output(pins[p], GPIO.LOW)
	for i in num[x] :
		output(led[i])
	GPIO.output(pins[p], GPIO.HIGH)

def show(x) :
	xx = list(x)
	i = 0
	while (i <= len(xx) - 1) :
		layout(i, int(xx[i]))
		i += 1
	
def clean() :
	for i in range(4) :
		GPIO.output(pins[i], GPIO.HIGH)
	for i in range(8) :
		GPIO.output(led[i], GPIO.HIGH)
		
for i in pins :
	GPIO.setup(i, GPIO.OUT)
for j in led :
	GPIO.setup(j, GPIO.OUT)

init()
while True :
	n = raw_input()
	show(n)
	raw_input()
	print(n)
	clean()
