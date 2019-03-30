import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER_1 = 23
GPIO_ECHO_1 = 24

print ("Ultrasonic Measurement")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER_1,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO_1,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER_1, False)

def get_distance():
  distance_1 = 0
  tstart = time.time()
  while time.time() - tstart < 0.0025: # About 2 ms to reach 36cm
    # Allow module to settle
    time.sleep(0.005)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER_1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_1, False)

    start = time.time()
    start_1 = start
    stop_1 = 1
    while GPIO.input(GPIO_ECHO_1)==0 and time.time()- start < 0.001:
      start_1 = time.time()
    while GPIO.input(GPIO_ECHO_1)==1 and time.time()- start < 0.0022:
      stop_1 = time.time()

    # Calculate pulse length
    elapsed_1 = stop_1-start_1

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance_1 = elapsed_1 * 34000
    # That was the distance there and back so halve the value
    distance_1 = distance_1 / 2

    # print ("Distance 1 : %.1f " % distance_1 )
    break
  return distance_1
  # Reset GPIO settings
  # GPIO.cleanup()