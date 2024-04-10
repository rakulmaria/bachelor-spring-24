from manim import *
from src.network import Network
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class Test_Graph_Linear(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_small()

        layers = [1, 2, 1]

        graph = Network(
            vertices,
            edges,
            capacities,
            source=source,
            sink=sink,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
        )

        self.camera.background_color = WHITE

        self.add(graph)
