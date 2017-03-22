import pypot.primitive
import time
import numpy as np
from .instants import Instant_Actions

"""
Figure out how to pass  data
"""


class Continuous_Wave(pypot.primitive.LoopPrimitive):
    """docstring for Motions"""
    # def __init__(self, robot,data,freq=20):
    def __init__(self, robot,freq=20):
    	pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
    	self.robot = robot
    	# self.data = data


    def setup(self):
    	for m in self.robot.motors:
    		m.compliant = False

    	self.robot.r_shoulder_y.goal_position = -150
    	self.robot.r_shoulder_x.goal_position = 30
    	self.robot.r_arm_z.goal_position = -50
    	self.robot.r_elbow_y.goal_position = 0

    	time.sleep(1)
    	t0 = time.time()   # Gets the timestamp at the start of the waving motion


    def start(self):
        self.setup()
    	t1 = time.time() # Gets the timestamp at the end of each loop

    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_y.goal_position = -150
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_x.goal_position = 30
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_arm_z.goal_position = -50
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_elbow_y.goal_position = 0

    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	time.sleep(rest)

    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_y.goal_position = -130
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_x.goal_position = -10
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_arm_z.goal_position = -70
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)
    	self.robot.r_elbow_y.goal_position = -65

    	# self.data.app()
    	# self.data.TIME.append(t1-t0)

    	time.sleep(rest)
    	# self.data.app()
    	# self.data.TIME.append(t1-t0)





    def stop(self):
        for m in self.robot.motors:
            m.goal_position = 0
    	    m.compliant = True
		

    def update(self):
    	pass




class Anatomical(pypot.primitive.LoopPrimitive):
    """docstring for Anatomical"""
    # def __init__(self, robot,data,freq=20):
    def __init__(self, robot,freq=20):
        pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
        self.robot = robot
        # self.data = data
        # self.instants = Instant_Actions(self.robot,self.data)


    def start(self,rest=3):
    #Lateral View Pictures   
    #Figure 1

        #Motor 51 Shoulder Flexion
        self.robot.r_shoulder_y.goal_position = 49 
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
        
        #Motor 51 Shoulder Extension
        self.robot.r_shoulder_y.goal_position = -169 
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()

    #Figure 2
    
        #Motor 54 Elbow Extension
        self.robot.r_elbow_y.goal_position = 0 
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
        
        #Motor 54 Elbow Flexion
        self.robot.r_elbow_y.goal_position = -129
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
            
    #Anterior View Pictures
    #Figure 3

        #Motor 53 Pronation
        self.robot.r_arm_z.goal_position = -20 
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
        
        #Motor 53 Supination
        self.robot.r_arm_z.goal_position = 94 
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
    
    #Figure 4       
        
        #Motor 52 Adduction
        self.robot.r_shoulder_x.goal_position = 0
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()
        
        #Motor 52 Abduction    
        self.robot.r_shoulder_x.goal_position = 89
        time.sleep(rest)
        #Rest Position
        # self.instants.attention()



    def stop(self):
        for m in self.robot.motors:
            m.goal_position = 0
    	    m.compliant = True
		

    def update(self):
    	pass
