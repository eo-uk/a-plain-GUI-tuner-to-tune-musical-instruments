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
