from functools import partial
import numpy as np
import os

from poppy.creatures import AbstractPoppyCreature

from .primitives.safe import LimitTorque, TemperatureMonitor
from .primitives.idle import Relax

class PoppyRattle(AbstractPoppyCreature):
    @classmethod
    def setup(cls,robot):
 		
        robot._primitive_manager._filter = partial(np.sum, axis=0)
    	
    	if robot.simulated:
    	    cls.vrep_hack(robot)
    	    cls.add_vrep_methods(robot)
	
        for m in robot.motors:
    	    m.goto_behavior = 'dummy'
            m.compliant = False
	
        # Attach default primitives:
        if not robot.simulated:
    	    sound_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    	                                     'media', 'sounds', 'error.wav')
            robot.attach_primitive(TemperatureMonitor(robot, sound=sound_file), 'temperature_monitoring')
            robot.temperature_monitoring.start()
	
    	# Safe primitives:
        robot.attach_primitive(LimitTorque(robot), 'limit_torque')
	
	
    	# Idle primitives
        robot.attach_primitive(Relax(robot), 'relax')

    @classmethod
    def add_vrep_methods(cls, robot):
        from pypot.vrep.controller import VrepController
        from pypot.vrep.io import remote_api

        def set_vrep_force(robot, vector_force, shape_name):
            """ Set a force to apply on Poppy Humanoid. """
            vrep_io = next(c for c in robot._controllers
                           if isinstance(c, VrepController)).io

            raw_bytes = (ctypes.c_ubyte * len(shape_name)).from_buffer_copy(shape_name)
            vrep_io.call_remote_api('simxSetStringSignal', 'shape',
                                    raw_bytes, sending=True)

            packedData = remote_api.simxPackFloats(vector_force)
            raw_bytes = (ctypes.c_ubyte * len(packedData)).from_buffer_copy(packedData)
            vrep_io.call_remote_api('simxSetStringSignal', 'force',
                                    raw_bytes, sending=True)

        robot.set_vrep_force = partial(set_vrep_force, robot)




