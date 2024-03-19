from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getGraphAsMobjects
from src.vertices_examples import VerticesExamples as V


class Test(Scene):
    def construct(self):
        vertices, edges, capacities, scale = V.SedgewickWayne()
        print(scale)
        vertices, edges, scale = getGraphAsMobjects(
            vertices, edges, capacities, layout_scale=scale / 2
        )
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE
        self.camera.frame_width = scale * scale * scale
        self.camera.resize_frame_shape(0)

        self.add(graph)
        self.wait(1)
