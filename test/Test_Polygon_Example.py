from manim import *
from src.flow_object import FlowPolygon

# test comment to get file with


class Test_Polygon_Example(Scene):
    def construct(self):
        test = FlowPolygon(6)
        self.add(test)
