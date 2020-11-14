import os
import sounddevice as sd
import pitch
from scipy.io.wavfile import write


def get_current_pitch():
    fs = 44100  
    seconds = 0.1
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  
    write('audio', fs, myrecording)   
    
    return pitch.find_pitch('audio')

def check(pitch_target):
    #Get current pitch from the microphone input
    pitch_current = get_current_pitch()
    #Get delta between current pitch and target pitch
    delta = int(pitch_current - pitch_target)

    #Text to display above the offset
    text = 'Too Low' if delta < -10 else 'Too High' if delta > 10 else 'Perfect!'
    #Decorate the offset with a plus sign if above 0
    offset = '+' + str(delta) if delta > 0 else str(delta)

    return (text, offset)
