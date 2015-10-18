import RPi.GPIO as GPIO
import time, random
 
"""
Display date to LED lights
There are four lights, it displays 4 number
"""
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins = [21, 16, 19, 6, 5, 20, 26, 13] #GPIO ports
sels = [17, 27, 22, 10] #GPIO ports to select led, there are four led lights
nums = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]
leds = [0, 1, 7, 8]
sounds = 11

for i in leds :
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
 
 
def setp(n, status='on'):
    if status == 'on':
        GPIO.output(n, GPIO.LOW)
    else:
        GPIO.output(n, GPIO.HIGH)
 
for i in pins + sels:
    GPIO.setup(i, GPIO.OUT)
    setp(i, 'off')
 
for i in sels:
    setp(i, 'on')

GPIO.setup(sounds, GPIO.OUT)
setp(sounds, 'off')
 

#
#     __0_
#    |     |    |  0 ->  543210     -> 011 1111 -> 0x3f   6 -> 654320   -> 111 1101 -> 0x7d
#  5 |     | 1  |  1 ->  21         -> 000 0110 -> 0x06   7 -> 210      -> 000 0111 -> 0x07
#    |__6__|    |  2 ->  64310      -> 101 1011 -> 0x5b   8 -> 6543210  -> 111 1111 -> 0x7f
#    |     |    |  3 ->  63210      -> 100 1111 -> 0x4f   9 -> 653210   -> 110 1111 -> 0x6f
#  4 |     | 2  |  4 ->  6521       -> 110 0110 -> 0x66
#    |__3__|    |  5 ->  65320      -> 110 1101 -> 0x6d
#
 
 
def flush(sel, n):
    setp(sels[sel], 'on')
    n = nums[n]
    for i in sels:
        if i != sels[sel]:
            setp(i, 'off')
 
    for i in range(7):
        if (n & (1 << i)):
            setp(pins[i], 'on')
 
    for i in range(7):
        if (n & (1 << i)):
            setp(pins[i], 'off')
 

try:
    set_time = input("please input set time:")
    timen = int(set_time)
    i = 0
    pt = time.clock()
    while timen >= 0 :
	t = timen
	a = t / 1000
	t = t % 1000
	b = t / 100
	t = t % 100
	c = t / 10
	t = t % 10
	d = t
        flush(0, a)
        flush(1, b)
        flush(2, c)
        flush(3, d)
        t = time.clock() - pt
        if t >= i :
	    timen -= 1
            i += 1
    for i in leds :
	setp(i, 'on')
    setp(sounds, 'on')
    raw_input()
    setp(sounds, 'off')
    for i in leds :
	setp(i, 'off')

except:
    GPIO.cleanup()
