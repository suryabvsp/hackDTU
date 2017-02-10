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
M1 = 19
M2 = 26

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)

def calculateDistance(TRIG, ECHO):
	GPIO.output(TRIG,False) #waiting for sensor to settle
	time.sleep(2)

	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False) #trigger a 10us pulse

	while GPIO.input(ECHO)==0:   #note time when ECHO is last LOW
	#i.e. time at which last pulse leaves
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:   #note time when ECHO is last HIGH
	#i.e. time at which last pulse arrives
		pulse_end = time.time()

	#time taken for the last pulse to travel the distance
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150 #sound speed 343m/s
	distance = round(distance,2)
	#distance in cm

	GPIO.cleanup() #reset GPIO pins
	return distance;
	
distance1 = calculateDistance(TRIG1,ECHO1)
distance2 = calculateDistance(TRIG2,ECHO2)
diff = abs(distance1-distance2)

if distance1 > 300 and distance2 > 300:
	GPIO.output(M1,False)
	GPIO.output(M2,False)
else:
	if diff < 30:
		GPIO.output(M1,True)
		GPIO.output(M2,True)
	else:
		if distance1 < distance2:
			GPIO.output(M1,True)
			GPIO.output(M2,False)
		if distance2 < distance1:
			GPIO.output(M2,True)
			GPIO.output(M1,False)
	
	
