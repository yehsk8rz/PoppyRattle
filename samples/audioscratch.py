from __future__ import division, print_function
from tqdm import tqdm
from explauto.environment import environments
import os, time, datetime, threading
import pyaudio, wave
import numpy as np, torch as th
from poppy.creatures import PoppyRattle
from poppy_rattle import Data, Instant_Actions

# poppy = PoppyRattle()
# data = Data(poppy)
# act = Instant_Actions(poppy, data)
# poppy.temperature_monitoring.start()


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                # input_
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()