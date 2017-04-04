import time
from threading import Thread

def sleeper(i):
    print "thread %d sleeps for 5 seconds" % i
    time.sleep(5)
    print "thread %d woke up" % i

for i in range(10000):
    t = Thread(target=sleeper, args=(i,))
    t.start()