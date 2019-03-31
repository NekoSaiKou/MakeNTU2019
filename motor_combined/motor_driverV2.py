import RPi.GPIO as GPIO     # Importing RPi library to use the GPIO pins
from time import sleep  # Importing sleep from time library

delay_circle = 10000 #unit circle run how many turns
power = 100


def forward(power):    
    global pwm1,pwm2,pwm3,pwm4
    pwm1.ChangeDutyCycle(power) # Change duty cycle
    pwm2.ChangeDutyCycle(0) # Change duty cycle
    pwm3.ChangeDutyCycle(power) # Change duty cycle
    pwm4.ChangeDutyCycle(0) # Change duty cycle
    pass

def backward(power):
    global pwm1,pwm2,pwm3,pwm4
    pwm1.ChangeDutyCycle(0) # Change duty cycle
    pwm2.ChangeDutyCycle(power) # Change duty cycle
    pwm3.ChangeDutyCycle(0) # Change duty cycle
    pwm4.ChangeDutyCycle(power) # Change duty cycle
    pass

def rotate(circle):
    global power
    if circle>0:
        #for c in range(int(delay_circle*circle)):
        forward(power)
        sleep(0.4)
    else:
        backward(power)
        sleep(0.4)    
    pass

def stop(back):
    global pwm1,pwm2,pwm3,pwm4
    rotate(back)
    pwm1.stop()      # Stop the PWM
    pwm2.stop() 
    pwm3.stop() 
    pwm4.stop() 

    GPIO.cleanup()  # Make all the output pins LOW
    pass
    
en1 = 22            # 1,2 front wheel 1+ 2-
en2 = 18            # Initializing the GPIO pin for motor
en3 = 5           # 3,4 back wheel 3+ 4-
en4 = 6

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(en1, GPIO.OUT)   # Declaring pin 21 as output pin
pwm1 = GPIO.PWM(en1, 100)    # Created a PWM object
pwm1.start(0)                    # Started PWM at 0% duty cycle

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(en2, GPIO.OUT)   # Declaring pin 21 as output pin
pwm2 = GPIO.PWM(en2, 100)    # Created a PWM object
pwm2.start(0)  

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(en3, GPIO.OUT)   # Declaring pin 21 as output pin
pwm3 = GPIO.PWM(en3, 100)    # Created a PWM object
pwm3.start(0)  

GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
GPIO.setup(en4, GPIO.OUT)   # Declaring pin 21 as output pin
pwm4 = GPIO.PWM(en4, 100)    # Created a PWM object
pwm4.start(0)  
'''
try:
    #while 1:                    # Loop will run forever
        rotate(1)
    
        #for x in range(1000):    # This Loop will run 100 times
            #forward(100) # Change duty cycle
        
        sleep(0.01)         # Delay of 10mS
            
        for x in range(1000): # Loop will run 100 times; 100 to 0
            backward(100)
        
    
# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
    pass        # Go to next line

#rotate(1)
pwm1.stop()      # Stop the PWM
pwm2.stop() 
pwm3.stop() 
pwm4.stop() 

GPIO.cleanup()  # Make all the output pins LOW
'''

