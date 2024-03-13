from manim import *
from src.flow_object import FlowPolygon


class Polygon(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        test = FlowPolygon(6)
        self.add(test)
