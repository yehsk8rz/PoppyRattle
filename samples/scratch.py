from __future__ import division, print_function
#from explauto.environment import environments
#import os, time, datetime, threading
import time
import sounddevice as sd
#import numpy as np
from pypot.creatures import PoppyRattle
from poppy_rattle import Data, Instant_Actions, Recorder

### Look up available sound devices ###
# sd.query_devices()
## Then you can set the device as its name in a string ##
# recording_device = 'HD Pro Webcam C920'
# sd.default.device = recording_device
## Or as the index number associated with it
# recording_device = 4
out_Dir = "out_Data"

# poppy = PoppyRattle(simulator='vrep')
poppy = PoppyRattle()

data = Data(poppy)
act = Instant_Actions(poppy, data)
rec = Recorder(out_Dir=out_Dir)

if not poppy.simulated:
	poppy.temperature_monitoring.start()


# act.hand_wave(sec=3)
# act.rattle_shake(sec=3)
rec.sd_rattle(act.hand_wave,duration=3)
rec.sd_rattle(poppy.relax, duration=12)



if not poppy.simulated:
	poppy.temperature_monitoring.stop()


act.attention()
act.shutdown()

# del wavDir, csvDir, pngDir
del act, data, poppy