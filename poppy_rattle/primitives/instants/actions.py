import time
import numpy as np

class Instant_Actions(object):
	"""docstring for Instant_Actions"""
	def __init__(self, robot,data):
		self.robot = robot
		self.data = data
		
	def attention(self):
		for m in self.robot.motors:
			m.compliant = False
			m.goal_position = 0
	
	def release(self):
		for m in self.robot.motors:
			m.compliant = True

	def shutdown(self):
		self.attention()
		self.release()
		self.robot.close()

	
	def hand_wave(self,sec=10, rest=0.5):
	    """
	    This function is a primitive. When called, the robotic arm will move between two set point in space, defined by the angles the motors are travelling to.
	    
	        :param int sec: time in seconds for how long the arm will wave
	            ::default is set to 10 seconds
	        :param float rest: time in seconds for the time the arm has to finish its motion
	            ::default is set to 1/2 a second 
	    """
	    # define the first point in space
	    shoulder_y0 = -150
	    shoulder_x0 = 30
	    arm_0 = -50
	    elbow_0 = 0
	    
	    # define the second point in space
	    shoulder_y1 = -130
	    shoulder_x1 = -10
	    arm_1 = -70
	    elbow_1 = -65


	    self.robot.r_shoulder_y.goal_position = shoulder_y0
	    self.robot.r_shoulder_x.goal_position = shoulder_x0
	    self.robot.r_arm_z.goal_position = arm_0
	    self.robot.r_elbow_y.goal_position = elbow_0
	    time.sleep(1)
	    t0 = time.time()   # Gets the timestamp at the start of the waving motion
	    
	    
	    # This will loop through the two arm positions until the set time duration has elapsed. 
	    while True:
	        t1 = time.time() # Gets the timestamp at the end of each loop
	        
	        if t1-t0 >= sec: # This will end the loop and wave motion when the allotted time has expired
	            break
	            
	        
	        # run for sec
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_y.goal_position = shoulder_y0
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_x.goal_position = shoulder_x0
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_arm_z.goal_position = arm_0
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_elbow_y.goal_position = elbow_0
	        
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	       	time.sleep(rest)
	    
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_y.goal_position = shoulder_y1
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_x.goal_position = shoulder_x1
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_arm_z.goal_position = arm_1
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_elbow_y.goal_position = elbow_1
	        
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        
	        time.sleep(rest)
	        self.data.app()
	        self.data.TIME.append(t1-t0)


	    self.attention()
	        
	        
	  
	        
	
	    
	
	
	    
	def rattle_shake(self,sec=10.5, rest=0.4):
	    """
	    This function is a primitive. When called, the robotic arm will move between two set point
	    in space, defined by the angles the motors are travelling to. This will make the arm 
	    perform a vertical movement in order to imitate an infant shaking a rattle.
	
	        :param int sec: time in seconds for how long the arm will wave
	            ::default is set to 20 seconds
	        :param float rest: time in seconds for the time the arm has to finish its motion
	            ::default is set to 0.4 seconds
	    """
	    
	    # define the first point in space
	    shoulder_y0 = -45
	    shoulder_x0 = 0
	    arm_0 = 0
	    elbow_0 = -65
	    
	    # define the second point in space
	    shoulder_y1 = -30
	    shoulder_x1 = 0
	    arm_1 = 0
	    elbow_1 = -35
	    
	
	    
	    
	    t0 = time.time() # Gets the timestamp at the start of the waving motion
	    
	    # This will loop through the two arm positions until the set time duration has elapsed. 
	    while True:
	    	# signal = np.fromstring(signal, 'Int16')
	
	    	# #Split the self.data into channels 
	    	# channels = [[] for channel in range(wav_file.getnchannels())]
	    	# for index, datum in enumerate(signal):
	    	# channels[index%len(channels)].append(datum)
	
	    	# #Get time from indices
	    	# fs = wav_file.getframerate()
	    	# Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))
	
	    	# #Plot
	    	# plt.figure(1)
	    	# plt.title('Signal Wave...')
	    	# for channel in channels:
		    #     plt.plot(Time,channel)
		    # 	plt.show()
	
	        t1 = time.time() # Gets the timestamp at the start of each loop
	        
	        # This will end the loop and wave motion when the allotted time has expired
	        if t1-t0 >= sec: 
	            break
	            
	        # arm moves to first position
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_y.goal_position = shoulder_y0 #-45
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_x.goal_position = shoulder_x0 #5
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_arm_z.goal_position = arm_0 #20
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_elbow_y.goal_position = elbow_0 #-129
	        
	
	        
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        time.sleep(rest)
	        
	        
	        # arm moves to second position
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_y.goal_position = shoulder_y1 #-25
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_shoulder_x.goal_position = shoulder_x1  #0
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_arm_z.goal_position = arm_1; #0
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        self.robot.r_elbow_y.goal_position = elbow_1 #-10
	        
	
	
	       
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	        time.sleep(rest)
	        
	        
	        
	        self.data.app()
	        self.data.TIME.append(t1-t0)
	    
	         
	    self.attention()
	
