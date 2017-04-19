import datetime,time
import os
import wave
from multiprocessing.pool import ThreadPool
import threading 

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import Queue
from scipy.io import wavfile


class Recorder(object):
    """docstring for Recorder"""

    def __init__(self,
                sd_dev=None,
                out_Dir='../out_Data',):
        self.out_Dir = out_Dir

        if sd_dev is not None:
            sd.default.device = sd_dev
            pass
        


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
    def create_outFile(self):
        DATE = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        TIME = datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
        return "{}/{}_rattle.wav".format(self.wavDir,TIME)

    def data_Output(self,outFile,fs,data):
    	outPng = outFile.replace('.wav','.png')
        outPng = outPng.replace('/wav/','/png/')
    	outCSV = outFile.replace('.wav','.csv')
        outCSV= outCSV.replace('/wav/','/csv/')
	
    	Time=np.linspace(0, len(data)/fs, num=len(data))
	
    	plt.figure(1)
    	plt.title('Mel spectrogram(Stereo)')
    	plt.xlabel('Time(s)')
    	plt.ylabel('Frequency(Hz)')

        np.savetxt(outCSV, data,delimiter=',',fmt='%.3e')

    	plt.plot(Time,data)
    	plt.savefig(outPng)
    	plt.show()    
    	
    	



    # function causes the rattle to shake and record audio
    def sd_rattle(self,function,args=None,outFile=None,
                    fs = 44100,
                    duration = None,
                    rec_len = 30):

        
        if outFile is None:
            outFile = self.create_outFile()

        sd.default.channels = 2,2
        sd.default.samplerate = fs

        if (duration == None):
            int num = 0
            if sec is None:
                print("Press Ctr-C to end the recording:")
            while(True):
                out = 
                try:
                    recording = sd.rec(rec_len * fs, dtype='float32')
                    if('primitives' in str(type(function))):
                        function.start()
                        sd.wait()
                        function.stop()
                    else:
                        function(sec=rec_len)
                        sd.wait()
                except KeyboardInterrupt:
                    break

                wavfile.write(outFile, fs, recording)
                self.data_Output(outFile, fs, recording)
            
            sd.wait()
            wavfile.write(outFile, fs, recording)
            self.data_Output(outFile, fs, recording)

        else:
            recording = sd.rec(duration * fs,dtype='float32')
            if('primitives' in str(type(function))):
                function.start()
                sd.wait()
                function.stop()

            else:
                function(sec=duration)
                sd.wait()


            wavfile.write(outFile, fs, recording)
            self.data_Output(outFile, fs, recording)



    def set_out_Dir(self,out_Dir):
        self.out_Dir = out_Dir

        
