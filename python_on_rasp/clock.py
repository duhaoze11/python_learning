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
    while True:
        t = time.gmtime()
        flush(0, t.tm_min / 10)
        flush(1, t.tm_min % 10)
        flush(2, t.tm_sec / 10)
        flush(3, t.tm_sec % 10)
except:
    GPIO.cleanup()
