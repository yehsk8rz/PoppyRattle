from __future__ import division, print_function
from tqdm import tqdm
from explauto.environment import environments
import os, time, datetime, threading
import alsaaudio,audioop, sys, librosa
import numpy as np, torch as th
from poppy.creatures import PoppyRattle
from poppy_rattle.primitives import *
# import poppy_rattle.primitives.

# poppy = PoppyRattle(simulator='vrep')
poppy = PoppyRattle()

if poppy.simulated == True:
	# for simulator
	pos = []
else:
	pos_Head = []    # Stores the position of the hand (wrist) relative to the head
	pos_Stand = []    # Stores the position of the hand (wrist) relative to the center point between the feet

TIME = []    # Stores timestamps of when the arm is in a certain position
sys_load = []    # Stores the torque the motors are going through at a point in time.
                 # Good for being warry of the system load of a task and possibly calculating fatigue
speed = []    # Stores the angle speed the motors are travelling at
temp = []   # Stores the motors' temperature
volt = []   # Stores the motor's voltage. 
            # In conjunction with Temperaure, this can be used to measure energy of a task

# specific arrays for the rattle shaking movement
data_table = []  # stores the sound features of a recording
spike = [[],[]]  # stores instances of abnormal spikes in sound features and a given timestamp



# inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,device='sysdefault:CARD=Microphone')
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK,device='sysdefault:CARD=C920')
inp.setchannels(2)
inp.setrate(88200)
inp.setformat(alsaaudio.PCM_FORMAT_GSM)
inp.setperiodsize(160)

wavDir = "in_Data/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(wavDir):
    os.makedirs(wavDir)
csvDir = "out_Data/csv/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(csvDir):
    os.makedirs(csvDir)
pngDir = "out_Data/png/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(pngDir):
    os.makedirs(pngDir)



poppy.relax.start()
poppy.relax.stop()

for m in poppy.motors:
	m.compliant = True
poppy.close()