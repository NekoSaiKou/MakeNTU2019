
import speech_recognition
import time
import os
import pyaudio
#import wave
import pygame
import time

def open_sound():
    pygame.mixer.init()

    sound = pygame.mixer.Sound('open.wav')
    sound.play()
    #pygame.mixer.music.play(1)
    start = time.time()
    while True:
        sound.play()
        end = time.time()
        if end-start >2:
            break
    
        
def Voice_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source: 
        print("Please speak something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")
    except r.UnknowValueError:
        Text = "無法翻譯"
    except r.RequestError as e:
        Text = "無法翻譯{0}".format(e)          
    except:
        Text = "Cannot translate or recognize!"

    return Text
### 

Text = Voice_To_Text()
print(Text)
if Text == '打開':
    open_sound()
