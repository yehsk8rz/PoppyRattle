import pypot.primitive

class Idle(pypot.primitive.LoopPrimitive):
	"""docstring for Idle"""
	def __init__(self, robot,freq=0):
		pypot.primitive.LoopPrimitive.__init__(self, robot, freq)


	def rest(robot):
		for m in self.motors:
			print(m)






# [p.name for p in poppy.primitives]