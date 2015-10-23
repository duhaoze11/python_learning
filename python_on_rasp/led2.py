import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

pin = GPIO.PWM(8, 0.5)
pin.start(0)
try :
	while True :
		for dc in range(0, 101, 2) :
			pin.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100, -1, -2) :
			pin.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt :
	pass

pin.stop()
GPIO.cleanup()
