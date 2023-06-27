import RPi.GPIO as GPIO
import time

irL = 2
irR = 3
in1 = 17
in2 = 18
in3 = 27
in4 = 22
enA = 12
enB = 13

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(irL,GPIO.IN)        #GPIO 2 -> Left IR out
GPIO.setup(irR,GPIO.IN)        #GPIO 3 -> Right IR out
GPIO.setup(17,GPIO.OUT)       #GPIO 4 -> Motor 1 terminal A
GPIO.setup(18,GPIO.OUT)      #GPIO 14 -> Motor 1 terminal B
GPIO.setup(27,GPIO.OUT)       #GPIO 17 -> Motor Left terminal A
GPIO.setup(22,GPIO.OUT)        #GPIO 18 -> Motor Left terminal B
GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
p1 = GPIO.PWM(enA,1000)
p2 = GPIO.PWM(enB,1000)
p1.start(50)
p2.start(50)

while 1:
    if(GPIO.input(irL)==False and GPIO.input(irR)==False):        #both while move forward     

        GPIO.output(in1,True) 
        GPIO.output(in2,False) 
        GPIO.output(in3,True) 
        GPIO.output(in4,False)    
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)

    elif(GPIO.input(irL)==True and GPIO.input(irR)==False):       #turn right  

        GPIO.output(in1,True)  
        GPIO.output(in2,False)   
        GPIO.output(in3,True)  
        GPIO.output(in4,True)  
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)


    elif(GPIO.input(irL)==False and GPIO.input(irR)==True):       #turn left

        GPIO.output(in1,True)  
        GPIO.output(in2,True)  
        GPIO.output(in3,True)  
        GPIO.output(in4,False)   
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)

    else:                                             #stop

        GPIO.output(in1,False)  
        GPIO.output(in2,False)  
        GPIO.output(in3,False)  
        GPIO.output(in4,False)  
GPIO.cleanup()


