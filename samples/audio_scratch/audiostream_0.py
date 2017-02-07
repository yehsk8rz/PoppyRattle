from time import sleep
from audiostream import get_output
from audiostream.sources.wave import SineSource

# get a output stream where we can play samples
stream = get_output(channels=2, rate=22050, buffersize=1024)

# create one wave sin() at 440Hz, attach it to our speaker, and play
sinsource = SineSource(stream, 440)
sinsource.start()

# you can change the frequency of the source during the playtime
for x in xrange(10):
    sinsource.frequency = 440 + x
    sleep(.5)

# ok we are done, stop everything.
sinsource.stop()