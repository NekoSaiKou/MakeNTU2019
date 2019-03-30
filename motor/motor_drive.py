import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
my_pwm=GPIO.PWM(17,100)
my_pwm.start(0)
'''
while True:
    ch = input("車子如何移動 f往前  b往後 l往左  r往右 q結束？")
    if ch == 'q':
       GPIO.output(17, False)
       GPIO.output(18, False)
       GPIO.output(22, False)
       GPIO.output(23, False)
       break
    if ch == 'f':
       GPIO.output(17, False)
       GPIO.output(18, True)
       GPIO.output(22, False)
       GPIO.output(23, True)
    if ch == 'b':
       GPIO.output(17, True)
       GPIO.output(18, False)
       GPIO.output(22, True)
       GPIO.output(23, False)
    if ch == 'r':
       GPIO.output(17, False)
       GPIO.output(18, True)
       GPIO.output(22, False)
       GPIO.output(23, False)
    if ch == 'l':
       GPIO.output(17, False)
       GPIO.output(18, False)
       GPIO.output(22, False)
       GPIO.output(23, True)
'''
while(1):
        my_pwm.ChangeDutyCycle(40)

        
my_pwm.stop()
GPIO.cleanup()