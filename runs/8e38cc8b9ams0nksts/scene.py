from manim import *

class Hello(Scene):
    def construct(self):
        sq = Square(color=BLUE)
        self.play(Create(sq))
        self.play(Transform(sq, Circle(color=YELLOW)))
        self.play(sq.animate.shift(RIGHT * 2))
        self.wait()
