from manim import *
from src.flow_object import FlowPolygon


class Test_Polygon(Scene):
    def construct(self):
        test = FlowPolygon(LEFT, RIGHT, RIGHT, 4)
        self.add(test)
