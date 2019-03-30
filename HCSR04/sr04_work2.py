import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER_1 = 23
GPIO_ECHO_1 = 24

GPIO_TRIGGER_2 = 17
GPIO_ECHO_2 = 27

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_1,GPIO.IN)      # Echo

GPIO.setup(GPIO_TRIGGER_2,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_2,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER_1, False)
GPIO.output(GPIO_TRIGGER_2, False)

while(True):
  # Allow module to settle
  time.sleep(0.005)

  # Send 10us pulse to trigger
  GPIO.output(GPIO_TRIGGER_1, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER_1, False)

  start_1 = time.time()
  while GPIO.input(GPIO_ECHO_1)==0:
    start_1 = time.time()
  while GPIO.input(GPIO_ECHO_1)==1:
    stop_1 = time.time()

  # Send 10us pulse to trigger
  GPIO.output(GPIO_TRIGGER_2, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER_2, False)

  start_2 = time.time()
  while GPIO.input(GPIO_ECHO_2)==0:
    start_2 = time.time()
  while GPIO.input(GPIO_ECHO_2)==1:
    stop_2 = time.time()

  # Calculate pulse length
  elapsed_1 = stop_1-start_1
  elapsed_2 = stop_2-start_2

  # Distance pulse travelled in that time is time
  # multiplied by the speed of sound (cm/s)
  distance_1 = elapsed_1 * 34000
  distance_2 = elapsed_2 * 34000
  # That was the distance there and back so halve the value
  distance_1 = distance_1 / 2
  distance_2 = distance_2 / 2

  print ("Distance 1 : %.1f  Distance 2 : %.1f" %( distance_1 ,distance_2))

# Reset GPIO settings
GPIO.cleanup()