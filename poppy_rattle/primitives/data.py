class Data(object):
    """docstring for Data"""
    def __init__(self,robot):
        self.robot = robot
        if robot.simulated == True:
	       # for simulator
	       self.pos_Head = []    # Stores the position of the hand (wrist) relative to the head
	       self.pos_Stand = []    # Stores the position of the hand (wrist) relative to the center point between the feet
        else:
	       self.pos = []

        self.TIME = []    # Stores timestamps of when the arm is in a certain position
        self.sys_load = []    # Stores the torque the motors are going through at a point in time.
                         # Good for being warry of the system load of a task and possibly calculating fatigue
        self.speed = []    # Stores the angle speed the motors are travelling at
        self.temp = []   # Stores the motors' temperature
        self.volt = []   # Stores the motor's voltage. 
                    # In conjunction with Temperaure, this can be used to measure energy of a task

        # specific arrays for the rattle shaking movement
        self.data_table = []  # stores the sound features of a recording
        self.spike = [[],[]]  # stores instances of abnormal spikes in sound features and a given timestamp


    def app(self):
	"""
	This function merely appends system sensory information into the appropriate python list.
	"""
        
	if self.robot.simulated == True:
	    # appends wrist position relative to head position
	    self.pos_Head.append(self.robot.get_object_position('r_forearm_visual','head_visual'))
	    # appends wrist position relative to the center point between the feet
	    self.pos_Stand.append(self.robot.get_object_position('r_forearm_visual')) 
	else:
	    # stores the angle position of all the motors
	    self.pos.append(self.robot.r_shoulder_x.present_position)
	    self.pos.append(self.robot.r_shoulder_y.present_position)
	    self.pos.append(self.robot.r_arm_z.present_position)
	    self.pos.append(self.robot.r_elbow_y.present_position)
	    
	# appends the stress each motor is going through
	self.sys_load.append(self.robot.r_shoulder_x.present_load)
	self.sys_load.append(self.robot.r_shoulder_y.present_load)
	self.sys_load.append(self.robot.r_arm_z.present_load)
	self.sys_load.append(self.robot.r_elbow_y.present_load)
	   
	# appends the angle speed each motor is currently traveling at 
	self.speed.append(self.robot.r_shoulder_x.present_speed)
	self.speed.append(self.robot.r_shoulder_y.present_speed)
	self.speed.append(self.robot.r_arm_z.present_speed)
	self.speed.append(self.robot.r_elbow_y.present_speed)
	    
	# appends system temperature for each motor
	self.temp.append(self.robot.r_shoulder_x.present_temperature)
	self.temp.append(self.robot.r_shoulder_y.present_temperature)
	self.temp.append(self.robot.r_arm_z.present_temperature)
	self.temp.append(self.robot.r_elbow_y.present_temperature)
	    
	# appends the voltage ruuning through each motor
	self.volt.append(self.robot.r_shoulder_x.present_voltage)
	self.volt.append(self.robot.r_shoulder_y.present_voltage)
	self.volt.append(self.robot.r_arm_z.present_voltage)
	self.volt.append(self.robot.r_elbow_y.present_voltage)
	
	
    def clear(self):
	    self.__init__()
