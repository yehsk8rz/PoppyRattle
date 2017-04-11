from __future__ import division, print_function
from explauto.environment import environments
import os, time, datetime, threading
import sounddevice as sd
import numpy as np
from pypot.creatures import PoppyRattle
from poppy_rattle import Data, Instant_Actions, Recorder

### Look up available sound devices ###
# sd.query_devices()
## Then you can set the device as its name in a string ##
recording_device = 'HD Pro Webcam C920'
sd.default.samplerate = 44100
## Or as the index number associated with it
# recording_device = 4
print(sd.default.samplerate)
out_Dir = "out_Data"

poppy = PoppyRattle(simulator='vrep')
# poppy = PoppyRattle()

data = Data(poppy)
act = Instant_Actions(poppy, data)
rec = Recorder(sd_dev=recording_device,out_Dir=out_Dir)
print(sd.default.samplerate)

if not poppy.simulated:
	poppy.temperature_monitoring.start()





act.hand_wave(sec=3)
act.rattle_shake(sec=3)
rec.sd_rattle(act.hand_wave)

poppy.relax.start()
time.sleep(5)
poppy.relax.stop()

if not poppy.simulated:
	poppy.temperature_monitoring.stop()

act.shutdown()

del wavDir, csvDir, pngDir
del wave_cont ,act, data, poppy