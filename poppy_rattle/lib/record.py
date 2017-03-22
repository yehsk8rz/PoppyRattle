import datetime,time
import os
import threading
import wave

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt


class Recorder(object):
    """docstring for Recorder"""
    def __init__(self,
                sd_dev=sd.default.device,
                out_Dir='../out_Data',):
        self.out_Dir = out_Dir
        sd.default.device = sd_dev

        self.wavDir = "{}/wav/{}".format(self.out_Dir,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
        if not os.path.exists(self.wavDir):
            os.makedirs(self.wavDir)
        self.csvDir = "{}/csv/{}".format(self.out_Dir,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
        if not os.path.exists(self.csvDir):
            os.makedirs(self.csvDir)
        self.pngDir = "{}/png/{}".format(self.out_Dir,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))
        if not os.path.exists(self.pngDir):
            os.makedirs(self.pngDir)

        


    # audio recording setup
    # creates a new wavefile for each run
    def outFile():
        DATE = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        TIME = datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
        return "{}/{}/{}_rattle.wav".format(self.wavDir,DATE,TIME)

    def data_Output(self,outFile=outFile()):
    	outPng = outPng.replace('.wav','.png')
    	outCSV = outCSV.replace('.wav','.csv')
    	spf = wave.open(out,'r')

    	#Extract Raw Audio from Wav File
    	signal = spf.readframes(-1)
    	signal = np.fromstring(signal, 'Int16')
    	fs = spf.getframerate()
	
    	Time=np.linspace(0, len(signal)/fs, num=len(signal))
	
    	plt.figure(1)
    	plt.title('Mel spectrogram(Stereo)')
    	plt.xlabel('Time(s)')
    	plt.ylabel('Frequency(Hz)')
	
    	plt.plot(Time,signal)
    	plt.savefig(outPng)
    	plt.show()    
    	
    	np.savetxt(outCSV, signal,delimiter=',',fmt='%.3e')



    # function causes the rattle to shake and record audio
    def sd_rattle(self,function,outFile=outFile()):
    	l = 0
    	data = ''
    	
    	# set up the wave file
    	w = wave.open(outFile,'w')
    	# Open the device in nonblocking capture mode. The last argument could
    	# just as well have been zero for blocking mode. Then we could have
    	# left out the sleep call in the bottomvim of the loop
	
    	w.setnchannels(2)
    	w.setsampwidth(2)
    	w.setframerate(44100)
	
    	total = 0
    	count = 0
    	
    	# allows function to run in parallel
    	t = threading.Thread(target=function)
    	t.start()
    	timeStart = time.time()
    	while t.is_alive():
    	    
    	    timeStop = time.time()
    	    l,data = inp.read()
    	    if l:
    	        w.writeframes(data)
    	    time.sleep(.001)
    	rest_position()
	
    	print(w.getnframes())
    	print(w.getframerate())
    	print(len(data))
    	data_Output(outFile)


    def set_out_Dir(self,out_Dir):
        self.out_Dir = out_Dir

        
