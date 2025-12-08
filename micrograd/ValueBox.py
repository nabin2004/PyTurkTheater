from manim import *

class ValueBox(VGroup):
    def __init__(self, name, data, grad, width=2.0, height=0.8, **kwargs):
        super().__init__(**kwargs)
        
        # Main rectangle
        self.rect = Rectangle(width=width, height=height, color=RED, stroke_width=2)
        
        # Labels
        self.name_label = Tex(f"{name}", font_size=20).to_edge(UP, buff=0.1)
        self.data_label = Tex(f"data {data:.4f}", font_size=18)
        self.grad_label = Tex(f"grad {grad:.4f}", font_size=18)
        
        # Stack labels inside rectangle
        self.labels = VGroup(self.name_label, self.data_label, self.grad_label)
        self.labels.arrange(DOWN, center=True, buff=0.05)
        self.labels.move_to(self.rect.get_center())
        
        self.add(self.rect, self.labels)
