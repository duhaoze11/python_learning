# -*- coding: utf-8 -*-
#import RPi.GPIO as GPIO
#import time
#GPIO.setmode(GPIO.BCM)

led = [21, 16, 19, 6, 5, 20, 26, 13]
pins = [17, 27, 22, 10]
a = []
def layout(n = -1) :
	global a
	if  n == 0 :
		a = [led[0], led[1], led[2], led[3], led[4], led[5]]
		print(a)
	elif n == 1 :
		a = [led[1], led[2]]
		print(a)
	elif n == 2 :
		a = [led[0], led[1], led[3], led[4], led[6]]
		print(a)
	elif n == 3 :
		a = [led[0], led[1], led[2], led[3], led[6]]
		print(a)
	elif n == 4 :
		a = [led[1], led[2], led[5], led[6]]
		print(a)
	elif n == 5 :
		a = [led[0], led[2], led[3], led[5], led[6]]
		print(a)
	elif n == 6 :
		a = [led[0], led[2], led[3], led[4], led[5], led[6]]
		print(a)
	elif n == 7 :
		a = [led[0], led[1], led[2]]
		print(a)
	elif n == 8 :
		a = [led[0], led[1], led[2], led[3], led[4], led[5], led[6]]
		print(a)
	elif n == 9 :
		a = [led[0], led[1], led[2], led[3], led[5], led[6]]
		print(a)

for i in range(10) :
	layout(i)
