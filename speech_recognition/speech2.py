
import speech_recognition
import time
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
    harvard = speech_recognition.AudioFile('open.wav')
    with harvard as source: 
        audio = r.record(source)
    try:
        Text = r.recognize_google(audio, language="zh-TW")       
    except:
        Text = "Cannot translate or recognize!"

    return Text
### 

Text = Voice_To_Text()
print(Text)
if Text == '打開':
    open_sound()
