from manim import *
from src.graph import FlowGraph
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.SedgewickWayne()
        lt = {
            0: [-2, 0, 0],
            1: [-1, 1, 0],
            2: [-1, -1, 0],
            3: [1, 1, 0],
            4: [1, -1, 0],
            5: [2, 0, 0],
        }

        graph = FlowGraph(vertices, edges, capacities, layout=lt)
        self.camera.background_color = WHITE

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices, edges, capacities = V.SimpleGraph()

        lt = {
            0: [0, -1, 0],
            1: [2, 1, 0],
        }

        graph = FlowGraph(
            vertices, edges, capacities, layout=lt, growth_scale=GrowthScale.LOG2
        )
        self.camera.background_color = WHITE

        self.add(graph)


class Test3(Scene):
    def construct(self):
        vertices, edges, capacities = V.KleinbergTardos()

        layers = [1, 2, 1]

        graph = FlowGraph(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
        )

        self.camera.background_color = WHITE

        self.add(graph)

        graph.addToCurrentFlowTemp(10, [(0, 1), (1, 3)], scene=self)
        # self.wait(2)
        graph.addToCurrentFlowTemp(10, [(0, 1), (1, 2), (2, 3)], scene=self)
        # # # self.wait(2)
        graph.addToCurrentFlowTemp(10, [(0, 2), (2, 3)], scene=self)
