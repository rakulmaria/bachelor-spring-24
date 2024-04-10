from manim import *
from src.graph import FlowGraph
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class Test_Graph_Log2(Scene):
    def construct(self):
        vertices, edges, capacities = V.KleinbergTardosSmall()

        layers = [1, 2, 1]

        graph = FlowGraph(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LOG2,
        )

        self.camera.background_color = WHITE

        self.add(graph)
