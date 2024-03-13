from manim import *
from src.flow_object import FlowPolygon


class Test_polygon(Scene):
    def construct(self):
        test = FlowPolygon(6)
        self.add(test)
