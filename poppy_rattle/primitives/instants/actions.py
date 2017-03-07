import time
import numpy as np

def attention(robot):
	for m in robot.motors:
		m.compliant = False
		m.goal_position = 0

def release(robot):
	for m in robot.motors:
		m.compliant = True

def app(robot,data):
    """
    This function merely appends system sensory information into the appropriate python list.
    """
    
    #
    if robot.simulated == True:
        # appends wrist position relative to head position
        data.pos_Head.append(robot.get_object_position('r_forearm_visual','head_visual'))
        # appends wrist position relative to the center point between the feet
        data.pos_Stand.append(robot.get_object_position('r_forearm_visual')) 
    else:
        # stores the angle position of all the motors
        data.pos.append(robot.r_shoulder_x.present_position)
        data.pos.append(robot.r_shoulder_y.present_position)
        data.pos.append(robot.r_arm_z.present_position)
        data.pos.append(robot.r_elbow_y.present_position)
    
    # appends the stress each motor is going through
    data.sys_load.append(robot.r_shoulder_x.present_load)
    data.sys_load.append(robot.r_shoulder_y.present_load)
    data.sys_load.append(robot.r_arm_z.present_load)
    data.sys_load.append(robot.r_elbow_y.present_load)
   
    # appends the angle speed each motor is currently traveling at 
    data.speed.append(robot.r_shoulder_x.present_speed)
    data.speed.append(robot.r_shoulder_y.present_speed)
    data.speed.append(robot.r_arm_z.present_speed)
    data.speed.append(robot.r_elbow_y.present_speed)
    
    # appends system temperature for each motor
    data.temp.append(robot.r_shoulder_x.present_temperature)
    data.temp.append(robot.r_shoulder_y.present_temperature)
    data.temp.append(robot.r_arm_z.present_temperature)
    data.temp.append(robot.r_elbow_y.present_temperature)
    
    # appends the voltage ruuning through each motor
    data.volt.append(robot.r_shoulder_x.present_voltage)
    data.volt.append(robot.r_shoulder_y.present_voltage)
    data.volt.append(robot.r_arm_z.present_voltage)
    data.volt.append(robot.r_elbow_y.present_voltage)


def hand_wave(robot,data,sec=10, rest=0.5):
    """
    This function is a primitive. When called, the robotic arm will move between two set point in space, defined by the angles the motors are travelling to.
    
        :param int sec: time in seconds for how long the arm will wave
            ::default is set to 10 seconds
        :param float rest: time in seconds for the time the arm has to finish its motion
            ::default is set to 1/2 a second 
    """
    robot.r_shoulder_y.goal_position = -150
    robot.r_shoulder_x.goal_position = 30
    robot.r_arm_z.goal_position = -50
    robot.r_elbow_y.goal_position = 0
    time.sleep(1)
    t0 = time.time()   # Gets the timestamp at the start of the waving motion
    
    
    # This will loop through the two arm positions until the set time duration has elapsed. 
    while True:
        t1 = time.time() # Gets the timestamp at the end of each loop
        
        if t1-t0 >= sec: # This will end the loop and wave motion when the allotted time has expired
            break
            
        
        # run for sec
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_y.goal_position = -150
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_x.goal_position = 30
        app()
        data.TIME.append(t1-t0)
        robot.r_arm_z.goal_position = -50
        app()
        data.TIME.append(t1-t0)
        robot.r_elbow_y.goal_position = 0
        
        app()
        data.TIME.append(t1-t0)
       	time.sleep(rest)
    
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_y.goal_position = -130
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_x.goal_position = -10
        app()
        data.TIME.append(t1-t0)
        robot.r_arm_z.goal_position = -70
        app()
        data.TIME.append(t1-t0)
        robot.r_elbow_y.goal_position = -65
        
        app()
        data.TIME.append(t1-t0)
        
        time.sleep(rest)
        app()
        data.TIME.append(t1-t0)
        
        
  
        

    


    
def rattle_shake(robot,sec=10.5, rest=0.4):
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
    	signal = np.fromstring(signal, 'Int16')

    	#Split the data into channels 
    	channels = [[] for channel in range(wav_file.getnchannels())]
    	for index, datum in enumerate(signal):
        	channels[index%len(channels)].append(datum)

    	#Get time from indices
    	fs = wav_file.getframerate()
    	Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

    	#Plot
    	plt.figure(1)
    	plt.title('Signal Wave...')
    	for channel in channels:
	        plt.plot(Time,channel)
	    	plt.show()

        t1 = time.time() # Gets the timestamp at the start of each loop
        
        # This will end the loop and wave motion when the allotted time has expired
        if t1-t0 >= sec: 
            break
            
        # arm moves to first position
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_y.goal_position = shoulder_y0 #-45
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_x.goal_position = shoulder_x0 #5
        app()
        data.TIME.append(t1-t0)
        robot.r_arm_z.goal_position = arm_0 #20
        app()
        data.TIME.append(t1-t0)
        robot.r_elbow_y.goal_position = elbow_0 #-129
        

        
        app()
        data.TIME.append(t1-t0)
        time.sleep(rest)
        
        
        # arm moves to second position
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_y.goal_position = shoulder_y1 #-25
        app()
        data.TIME.append(t1-t0)
        robot.r_shoulder_x.goal_position = shoulder_x1  #0
        app()
        data.TIME.append(t1-t0)
        robot.r_arm_z.goal_position = arm_1; #0
        app()
        data.TIME.append(t1-t0)
        robot.r_elbow_y.goal_position = elbow_1 #-10
        


       
        data.app()
        TIME.append(t1-t0)
        time.sleep(rest)
        
        
        
        app()
        data.TIME.append(t1-t0)
    
         


    
