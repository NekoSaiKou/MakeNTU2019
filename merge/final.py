import RPi.GPIO as GPIO
import playwav
import distance
#import ws2812
import speech_recognition as sr
import time
import servo
import tracker_motor


state = 0
r = sr.Recognizer()
source = sr.Microphone()

length_threshold = 16

s1 = servo.Servo(17,50)
s2 = servo.Servo(27,50)
s1.turn(0)
s2.turn(150)
# Tracking thread
#tracker = tracker_motor.Tracking()

# Microphone input callback
def callback(recognizer, audio):  # this is called from the background thread
    global state
    try:
        print('check')
        speech_as_text = recognizer.recognize_google(audio, language="zh-TW")    
        print(speech_as_text)

        # Look for your "Ok Google" keyword in speech_as_text
        if "打開" in speech_as_text :
            state = 1
            ini_start()
            pass
        if "關掉" in speech_as_text :
            state = 0
            ini_stop()
            pass
    except Exception:
        print('I can\'t understand')
    #except sr.UnknownValueError:
        '''question mark'''

def ini_start():
    #tracker.resume()
    #tracker.run()
    s1.turn(140)
    s2.turn(10)

def ini_stop():
    #tracker.pause()
    s1.turn(0)
    s2.turn(150)

def start_recognizer():
    print("record")
    r.listen_in_background(source, callback)

def start_play():
    garbage_dis = 0
    try:
        garbage_dis = distance.get_distance()
        print ("Distance 1 : %.1f " % garbage_dis)
        if garbage_dis < 3:
            pass
        elif garbage_dis < length_threshold:
            playwav.play(0)
            pass
            #ws2812.light(0)
        else:
            pass
            #ws2812.light(1)
    except Exception:
        pass

if __name__ == "__main__":
    start_recognizer()
    while(True):
        if state == 1:
            start_play()
        elif state == 0:
            pass
        else:
            pass
