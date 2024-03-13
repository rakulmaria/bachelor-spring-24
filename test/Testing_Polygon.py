from manim import *
from src.flow_object import FlowPolygon


class Testing_Polygon(Scene):
    def construct(self):
        test = FlowPolygon(6)
        self.add(test)
