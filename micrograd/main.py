from manim import *
from ValueBox import ValueBox
from OperationNode import OperationNode   

class ComputationGraphScene(Scene):
    def construct(self):
        # Value boxes
        x1 = ValueBox("x1", 2.0, -1.5)
        x2 = ValueBox("x2", 0.0, 0.5)
        w1 = ValueBox("w1", -3.0, 1.0)
        w2 = ValueBox("w2", 1.0, 0.0)
        
        # Operation nodes
        mult1 = OperationNode("*")
        mult2 = OperationNode("*")
        add1 = OperationNode("+")
        
        # Layout manually (can be improved with automatic grid)
        x1.move_to(LEFT*4 + UP*1)
        w1.move_to(LEFT*4 + DOWN*1)
        x2.move_to(LEFT*6 + UP*1)
        w2.move_to(LEFT*6 + DOWN*1)
        
        mult1.move_to(LEFT*2 + UP*0.5)
        mult2.move_to(LEFT*2 + DOWN*0.5)
        add1.move_to(RIGHT*0 + UP*0)
        
        # Arrows
        arrows = VGroup(
            Arrow(x1.get_right(), mult1.get_left(), buff=0.1),
            Arrow(w1.get_right(), mult1.get_left(), buff=0.1),
            Arrow(x2.get_right(), mult2.get_left(), buff=0.1),
            Arrow(w2.get_right(), mult2.get_left(), buff=0.1),
            Arrow(mult1.get_right(), add1.get_left(), buff=0.1),
            Arrow(mult2.get_right(), add1.get_left(), buff=0.1)
        )
        
        # Add everything
        self.add(x1, x2, w1, w2, mult1, mult2, add1, arrows)
        self.wait(3)
