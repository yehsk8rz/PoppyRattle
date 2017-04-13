from __future__ import print_function, division
from scipy.io import wavfile
import sounddevice as sd

fs = 44100						# standard recording frequency
duration = 10					# records for about 10 seconds
sd.default.samplerate = fs
sd.default.channels = 2,2			# 1 is mon, 2 stereo
recording = sd.rec(duration * fs,dtype='float32')
out = "out.wav"
sd.wait()


sd.stop()
print(recording)
print(type(recording))

# sd.default.device['input'] = 'Yeti Stereo Microphone'
# print(sd.default.device)
# print(sd.query_devices())
wavfile.write(out, fs, recording)