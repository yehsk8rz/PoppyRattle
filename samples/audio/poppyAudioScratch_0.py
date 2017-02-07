import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import pypot.dynamixel
import pypot.robot
from explauto.environment import environments


my_config ={}
my_config['controllers'] = {}
my_config['controllers']['upper_body_controler'] = {
    'port': '/dev/ttyUSB0',     # For Linux
    #'port': '/dev/tty.usbserial-AI03QEN0', # For OSX
    'sync_read': False,
    'attached_motors': ['arms'],
    'protocol': 1,
}
my_config['motorgroups']={}
my_config['motorgroups'] = {
    'arms': ['right_arm'],
    'right_arm': ['r_shoulder_x', 'r_shoulder_y', 'r_arm_z','r_elbow_y']
}
my_config['motors'] = {}
my_config['motors']['r_shoulder_y'] = {
    'id': 51,
    'type': 'MX-28',
    'orientation': 'indirect',
    'offset': 0.0,
    'angle_limit': (-80, 180),
}
my_config['motors']['r_shoulder_x'] = {
    'id': 52,
    'type': 'MX-28',
    'orientation': 'indirect',
    'offset': 0.0,
    'angle_limit': (-10, 175),
}
my_config['motors']['r_arm_z'] = {
    'id': 53,
    'type': 'MX-28',
    'orientation': 'indirect',
    'offset': 0.0,
    'angle_limit': (-95, 95),
}
my_config['motors']['r_elbow_y'] = {
    'id': 54,
    'type': 'MX-28',
    'orientation': 'indirect',
    'offset': 0.0,
    'angle_limit': (0, 125),
}

poppy = pypot.robot.from_config(my_config)

poppy.start_sync()
time.sleep(2)

for m in poppy.motors:
    m.compliant = False
    m.goto_behavior = 'minjerk'
pos = []
TIME = []
sys_load = []
speed = []
temp = []
volt = []


# Primitive actions

def rest_position():
    poppy.r_shoulder_x.goal_position = 0
    poppy.r_shoulder_y.goal_position = 0
    poppy.r_arm_z.goal_position = 0
    poppy.r_elbow_y.goal_position = 0

def app():
    pos.append(poppy.r_shoulder_x.present_position)
    pos.append(poppy.r_shoulder_y.present_position)
    pos.append(poppy.r_arm_z.present_position)
    pos.append(poppy.r_elbow_y.present_position)

    sys_load.append(poppy.r_shoulder_x.present_load)
    sys_load.append(poppy.r_shoulder_y.present_load)
    sys_load.append(poppy.r_arm_z.present_load)
    sys_load.append(poppy.r_elbow_y.present_load)
    
    speed.append(poppy.r_shoulder_x.present_speed)
    speed.append(poppy.r_shoulder_y.present_speed)
    speed.append(poppy.r_arm_z.present_speed)
    speed.append(poppy.r_elbow_y.present_speed)
    
    temp.append(poppy.r_shoulder_x.present_temperature)
    temp.append(poppy.r_shoulder_y.present_temperature)
    temp.append(poppy.r_arm_z.present_temperature)
    temp.append(poppy.r_elbow_y.present_temperature)
     
    volt.append(poppy.r_shoulder_x.present_voltage)
    volt.append(poppy.r_shoulder_y.present_voltage)
    volt.append(poppy.r_arm_z.present_voltage)
    volt.append(poppy.r_elbow_y.present_voltage)
    
def hand_wave(sec=10, rest=0.5):
    t0 = time.time()
    while True:
        
        t1 = time.time()
        if t1-t0 >= sec:
            break

        # run for sec
        app()
        TIME.append(t1-t0)
        poppy.r_shoulder_y.goal_position = -70
        app()
        TIME.append(t1-t0)
        poppy.r_shoulder_x.goal_position = -170  
        app()
        TIME.append(t1-t0)
        poppy.r_arm_z.goal_position = 60;
        app()
        TIME.append(t1-t0)
        poppy.r_elbow_y.goal_position = 125
        
        app()
        TIME.append(t1-t0)
        time.sleep(rest)
        
    
        app()
        TIME.append(t1-t0)
        poppy.r_shoulder_y.goal_position = -50
        app()
        TIME.append(t1-t0)
        poppy.r_shoulder_x.goal_position = -135
        app()
        TIME.append(t1-t0)
        poppy.r_arm_z.goal_position = 75
        app()
        TIME.append(t1-t0)
        poppy.r_elbow_y.goal_position = 90
        
        app()
        TIME.append(t1-t0)

        time.sleep(rest)
        app()
