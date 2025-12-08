from manim import *

class OperationNode(VGroup):
    def __init__(self, symbol="*", radius=0.3, **kwargs):
        super().__init__(**kwargs)
        self.circle = Circle(radius=radius, color=RED, stroke_width=2)
        self.label = Tex(symbol, font_size=24).move_to(self.circle.get_center())
        self.add(self.circle, self.label)
