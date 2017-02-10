## program to run the sonars

# make sure there is a voltage divider down to 
import RPi.GPIO as GPIO  #import Python GPIO library,
#referred henceforth as GPIO
 
import time #import the time library

GPIO.setmode(GPIO.BCM) # or GPIO.BOARD, refer pin numbering
TRIG1 = 23
ECHO1 = 24
TRIG2 = 27
ECHO2 = 22

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

def calculateDistance(arg 1
GPIO.output(TRIG,False) #waiting for sensor to settle
time.sleep(2)

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False) #trigger a 10us pulse

while GPIO.input(ECHO)==0:   #note the time when ECHO is last LOW
#i.e. time at which last pulse leaves
	pulse_start = time.time()

while GPIO.input(ECHO)==1:   #note the time when ECHO is last HIGH
#i.e. time at which last pulse arrives
	pulse_end = time.time()

#time taken for the last pulse to travel the distance
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150
distance = round(distance,2)
#distance in cm

GPIO.cleanup() #reset GPIO pins
