# Feature extraction example
from __future__ import print_function

import librosa
import math
import numpy as np
import wave



filename = "in_Data/rattle.wav"

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# Separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                             sr=sr)

# Compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# And the first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)

# Stack and synchronize between beat events
# This time, we'll use the mean value (default) instead of median
beat_mfcc_delta = librosa.feature.sync(np.vstack([mfcc, mfcc_delta]),
                                       beat_frames)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
                                        sr=sr)

# Aggregate chroma features between beat events
# We'll use the median value of each feature between beat frames
beat_chroma = librosa.feature.sync(chromagram,
                                   beat_frames,
                                   aggregate=np.median)


rmse = librosa.feature.rmse(y)
# Finally, stack all beat-synchronous features together
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

print()
print("y: ", y)
raw_input("Press Enter to continue...")
print()
print("sr: ", sr)
raw_input("Press Enter to continue...")
print()
print("y_harmonic: ", y_harmonic)
raw_input("Press Enter to continue...")
print()
print("y_percussive: ", y_percussive)
raw_input("Press Enter to continue...")
print()
print("tempo: ", tempo)
raw_input("Press Enter to continue...")
print()
print("beat_frames: ", beat_frames)
raw_input("Press Enter to continue...")
print()
print("mfcc: ", mfcc)
raw_input("Press Enter to continue...")
print()
print("mfcc_delta: ", mfcc_delta)
raw_input("Press Enter to continue...")
print()
print("beat_mfcc_delta: ", beat_mfcc_delta)
raw_input("Press Enter to continue...")
print()
print("chromagram: ", chromagram)
raw_input("Press Enter to continue...")
print()
print("beat_chroma: ", beat_chroma)
raw_input("Press Enter to continue...")
print()
print("beat_features: ", beat_features)
raw_input("Press Enter to continue...")
print()

print("rnmse: ", rmse)
