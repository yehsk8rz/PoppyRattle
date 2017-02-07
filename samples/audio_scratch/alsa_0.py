from __future__ import print_function
from tqdm import tqdm
import alsaaudio, time, audioop, sys, librosa,json
import numpy as np
import time,wave


w = wave.open("in_Data/tmp.wav",'w')
# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottomvim of the loop
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,device='sysdefault:CARD=C920')

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(2)
inp.setrate(88200)
inp.setformat(alsaaudio.PCM_FORMAT_GSM)

# The period size controls the internal number of frames per period.
# The significance of this parameter is documented in the ALSA api.
# For our purposes, it is suficcient to know that reads from the device
# will return this many frames. Each frame being 2 bytes long.
# This means that the reads below will return either 320 bytes of data
# or 0 bytes of data. The latter is possible because we are in nonblocking
# mode.
inp.setperiodsize(160)


w.setnchannels(2)
w.setsampwidth(2)
w.setframerate(44100)

start = time.time()
data_table = []
for i in tqdm(range(10000),ncols=4):
    # Read data from device
    l,data = inp.read()
    if l:
        # Return the maximum of the absolute value of all samples in a fragment.
       data_table.append(audioop.max(data,2))
       w.writeframes(data)
       # print audioop.max(data, 2)
    time.sleep(.001)


data_num = np.asarray(data_table)

for x in data_table:
	print(x)

