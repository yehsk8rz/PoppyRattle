from __future__ import division
import pypot.primitive
from pypot.primitive.utils import Sinus



class Relax(pypot.primitive.LoopPrimitive):
	"""docstring for Relax"""


	def __init__(self, robot,freq=20):
		pypot.primitive.LoopPrimitive.__init__(self, robot, freq)

		sinus_args = [{'motor_list': [self.robot.r_shoulder_x, ], 'amp': 2, 'freq': 0.2, 'offset': 0, 'phase': 66},
                      {'motor_list': [self.robot.r_shoulder_x, ], 'amp': 0.8, 'freq': 0.5, 'offset': 0, 'phase': 66},
                      {'motor_list': [self.robot.r_elbow_y, ], 'amp': 2, 'freq': 0.5, 'offset': 0, 'phase': 75},
                      {'motor_list': [self.robot.r_elbow_y, ], 'amp': 0.3, 'freq': 0.2, 'phase': 75},
                      {'motor_list': [self.robot.r_arm_z, ], 'amp': 3, 'freq': 0.2, 'phase':78}]
		
		self.all_sinus = [Sinus(self.robot, 50, **s) for s in sinus_args]




	def setup(self):
		for m in self.robot.motors:	
			m.compliant = False

		[all_sinus.start() for all_sinus in self.all_sinus]



	def teardown(self):
		for m in self.robot.motors:
			m.compliant = True
		[all_sinus.stop() for all_sinus in self.all_sinus]

	def update(self):
		pass

		
