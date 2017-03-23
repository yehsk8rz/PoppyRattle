import datetime,time
import os
import wave
from multiprocessing.pool import ThreadPool

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import Queue
from scipy.io import wavfile


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
    def outFile(self):
        DATE = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        TIME = datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
        return "{}/{}/{}_rattle.wav".format(self.wavDir,DATE,TIME)

    def data_Output(self,outFile):
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
    def sd_rattle(self,function,outFile,
                    fs = 44100,
                    duration = 10):

        sd.default.samplerate = fs
        sd.default.channels = 2,2
    	
        recording = sd.rec
    	
    	# allows function to run in parallel
    	t = threading.Thread(target=sd.rec,args=())
    	t.start()
    	timeStart = time.time()
    	while t.is_alive():
    	    
    	
        wavfile.write(outFile, fs, data)
    	data_Output(outFile)


    def set_out_Dir(self,out_Dir):
        self.out_Dir = out_Dir

        
