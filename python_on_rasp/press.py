#!/usr/bin/env python
# coding=utf-8
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_btn = 23
pin_lgt = 7

GPIO.setup(pin_btn, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pin_lgt, GPIO.OUT, initial = GPIO.HIGH)

press_times = 0

def onPress(channel) :
	global press_times
	print('pressed')
	press_times += 1
	if press_times % 2 == 1 :
		GPIO.output(pin_lgt, GPIO.LOW)
	else :
		GPIO.output(pin_lgt, GPIO.HIGH)

GPIO.add_event_detect(pin_btn, GPIO.FALLING, callback = onPress, bouncetime = 500)

try :
	while True :
		time.sleep(1)

except KeyboardInterrupt :
	print('exit')

finally :
	GPIO.cleanup()
