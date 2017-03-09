import pypot.primitive
import time
import numpy as np

class Motions(pypot.primitive.LoopPrimitive):
    """docstring for Motions"""
    def __init__(self, robot,data,freq=20):
    	pypot.primitive.LoopPrimitive.__init__(self, robot, freq)
    	self.robot = robot
    	self.data = data


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
    	t1 = time.time() # Gets the timestamp at the end of each loop

    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_y.goal_position = -150
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_x.goal_position = 30
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_arm_z.goal_position = -50
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_elbow_y.goal_position = 0

    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	time.sleep(rest)

    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_y.goal_position = -130
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_shoulder_x.goal_position = -10
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_arm_z.goal_position = -70
    	self.data.app()
    	self.data.TIME.append(t1-t0)
    	self.robot.r_elbow_y.goal_position = -65

    	self.data.app()
    	self.data.TIME.append(t1-t0)

    	time.sleep(rest)
    	self.data.app()
    	self.data.TIME.append(t1-t0)





    def stop(self):
        for m in self.robot.motors:
            m.goal_position = 0
    	    m.compliant = True
		

    def update(self):
    	pass

		

		
