from manim import *
from src.flow_object import FlowObject


class Test_Polygon(Scene):
    def construct(self):
        test = FlowObject(LEFT, RIGHT, RIGHT, 4)
        self.add(test)
