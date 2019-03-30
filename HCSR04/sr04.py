from hcsr04sensor import sensor
import time
 
TRIGGER_PIN = 23
ECHO_PIN = 24
 
try:
    while True:
        sr04 = sensor.Measurement(TRIGGER_PIN, ECHO_PIN)
        raw_measurement = sr04.raw_distance()
        distance = sr04.distance_metric(raw_measurement)
        print('distance {:.1f} cm'.format(distance))
        time.sleep(10)
except KeyboardInterrupt:
    print('exit')