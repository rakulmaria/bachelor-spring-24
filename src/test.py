from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getGraphAsMobjects
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges = getGraphAsMobjects(V.SedgewickWayne())
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE
        # self.camera.frame_width = 70
        self.camera.resize_frame_shape(0)

        self.add(graph)
        self.wait(1)
