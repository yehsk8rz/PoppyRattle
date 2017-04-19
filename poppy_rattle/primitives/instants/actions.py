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

	
	def hand_wave(self,sec=None, rest=0.5):
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
	    
	    if sec is None:
	    	print("Press Ctr-C to end the arm wave:")

	    # This will loop through the two arm positions until the set time duration has elapsed. 
	    while True:
	        t1 = time.time() # Gets the timestamp at the end of each loop

	        if sec is not None:
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
	    	else:
	    		try:
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

	    		except KeyboardInterrupt:
	    			break

	        
	        
	  
	        
	
	    
	
	
	    
	def rattle_shake(self,sec=None, rest=0.5):
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

	    self.robot.r_shoulder_y.goal_position = shoulder_y0
	    self.robot.r_shoulder_x.goal_position = shoulder_x0
	    self.robot.r_arm_z.goal_position = arm_0
	    self.robot.r_elbow_y.goal_position = elbow_0
	    
	    
	    time.sleep(1)
	    t0 = time.time() # Gets the timestamp at the start of the waving motion
	    
	    if sec is None:
	    	print("Press Ctr-C to end the hand shake:")


	    # This will loop through the two arm positions until the set time duration has elapsed. 
	    while True:	
	        t1 = time.time() # Gets the timestamp at the start of each loop
	        
	        # This will end the loop and wave motion when the allotted time has expired
	        if sec is not None:
	        	if t1-t0 >= sec: 
	        	    break
	            
	       		# arm moves to first position
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_shoulder_y.goal_position = shoulder_y0 # -45
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_shoulder_x.goal_position = shoulder_x0 # 0
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_arm_z.goal_position = arm_0 #0
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_elbow_y.goal_position = elbow_0 # -65
	       	        
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	time.sleep(rest)
	        
	        
	        	# arm moves to second position
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_shoulder_y.goal_position = shoulder_y1 # -30
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_shoulder_x.goal_position = shoulder_x1  # 0
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_arm_z.goal_position = arm_1; # 0
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	self.robot.r_elbow_y.goal_position = elbow_1 # -35
	       	       
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        	time.sleep(rest)
	        	        
	        	self.data.app()
	        	self.data.TIME.append(t1-t0)
	        else:
	        	try:
	       			# arm moves to first position
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_shoulder_y.goal_position = shoulder_y0 # -45
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_shoulder_x.goal_position = shoulder_x0 # 0
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_arm_z.goal_position = arm_0 #0
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_elbow_y.goal_position = elbow_0 # -65
	       	        
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		time.sleep(rest)
	        
	        		# arm moves to second position
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_shoulder_y.goal_position = shoulder_y1 # -30
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_shoulder_x.goal_position = shoulder_x1  # 0
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_arm_z.goal_position = arm_1; # 0
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		self.robot.r_elbow_y.goal_position = elbow_1 # -35
	       	       
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        		time.sleep(rest)
	        	        
	        		self.data.app()
	        		self.data.TIME.append(t1-t0)
	        	except KeyboardInterrupt:
	        		break


	
