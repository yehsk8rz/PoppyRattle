from __future__ import print_function
import numpy as np
import librosa

filename = "in_Data/Pokemon-Lugia's Song www.mp3c.cc .mp3"
y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to Lugia.csv')
librosa.output.times_csv('out_Data/Lugia.csv', beat_times)

