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
		GPIO.setup(i, GPIO.OUT)
	for j in led :
		GPIO.setup(j, GPIO.OUT)
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
		

init()
while True :
	x = raw_input()
	xx = list(x)
	i = 3
	while True :
		while i >= 0 :
			GPIO.output(led[i], GPIO.LOW)
			layout(int(xx[i]))
			GPIO.output(led[i], GPIO.HIGH)
			i -= 1
		y = raw_input()
		if y != '' :
			clean()
			break
