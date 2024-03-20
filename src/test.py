from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getGraphAsMobjects, getMaxCapacity
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.Jungnickel()
        scale = getMaxCapacity(capacities)
        vertices, edges = getGraphAsMobjects(
            vertices, edges, capacities, layout_scale=scale
        )
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE
        self.camera.frame_width = scale * 4
        self.camera.resize_frame_shape(0)

        self.add(graph)
