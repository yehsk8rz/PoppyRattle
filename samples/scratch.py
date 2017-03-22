from __future__ import division, print_function
from explauto.environment import environments
import os, time, datetime, threading
import sounddevice as sd
import numpy as np, torch as th
from poppy.creatures import PoppyRattle
from poppy_rattle import Data, Instant_Actions, Recorder

### Look up available sound devices ###
# sd.query_devices()
## Then you can set the device as its name in a string ##
recording_device = 'HD Pro Webcam C920'
## Or as the index number associated with it
# recording_device = 4




# poppy = PoppyRattle(simulator='vrep')
poppy = PoppyRattle()

data = Data(poppy)
act = Instant_Actions(poppy, data)
rec = Recorder(recording_device)


if not poppy.simulated:
	poppy.temperature_monitoring.start()


# wavDir = "in_Data/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
# if not os.path.exists(wavDir):
#     os.makedirs(wavDir)
# csvDir = "out_Data/csv/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
# if not os.path.exists(csvDir):
#     os.makedirs(csvDir)
# pngDir = "out_Data/png/{}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
# if not os.path.exists(pngDir):
#     os.makedirs(pngDir)


act.hand_wave(sec=3)
act.rattle_shake(sec=3)

poppy.relax.start()
time.sleep(5)
poppy.relax.stop()

if not poppy.simulated:
	poppy.temperature_monitoring.stop()

act.shutdown()

del wavDir, csvDir, pngDir
del wave_cont ,act, data, poppy