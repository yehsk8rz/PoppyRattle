from __future__ import division, print_function
from tqdm import tqdm
from explauto.environment import environments
import os, time, datetime, threading
import sounddevice
import numpy as np, torch as th
from poppy.creatures import PoppyRattle
from poppy_rattle import Data, Instant_Actions

#from poppy_rattle import 

poppy = PoppyRattle(simulator='vrep')
# poppy = PoppyRattle()

data = Data(poppy)
act = Instant_Actions(poppy, data)
poppy.temperature_monitoring.start()


wavDir = "in_Data/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(wavDir):
    os.makedirs(wavDir)
csvDir = "out_Data/csv/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(csvDir):
    os.makedirs(csvDir)
pngDir = "out_Data/png/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
if not os.path.exists(pngDir):
    os.makedirs(pngDir)


act.hand_wave(sec=3)
act.rattle_shake(sec=3)

poppy.relax.start()
time.sleep(5)
poppy.relax.stop()

poppy.temperature_monitoring.stop()

for m in poppy.motors:
	m.compliant = True


poppy.close()