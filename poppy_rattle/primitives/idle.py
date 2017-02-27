import pypot.primitive

class Rest(pypot.primitive.LoopPrimitive):
    """
    docstring for Rest

    This command function returns the arm to a "resting" position, although it is more on the 
    lines of the attention position.
    
    For the physical arm, it is important to calibrate the motors so that the resting position 
    is set for all the motors is at angle 0. The simulator defaults to this, so this will 
    eliminate the need to constantly translate angles when switching between the two.
    """
    def __init__(self, robot):
        robot.r_shoulder_x.goal_position = 0   
        robot.r_shoulder_y.goal_position = 0
        robot.r_arm_z.goal_position = 0
        robot.r_elbow_y.goal_position = 0
        
       

class Attention(object):
    """docstring for Attention"""
    def __init__(self, robot):
        super(Attention, self).__init__()
        self.arg = arg
        


