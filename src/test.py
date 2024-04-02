from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getGraphAsMobjects
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.Jungnickel()
        vertices, edges = getGraphAsMobjects(vertices, edges, capacities)
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE
        self.add(graph)
