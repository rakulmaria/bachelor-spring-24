from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getEdgesAndVerticesAsMobjects
from src.vertices_examples import VerticesExamples as V


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

        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout=lt
        )
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices, edges, capacities = V.SimpleGraph()

        lt = {
            0: [0, -1, 0],
            1: [2, 1, 0],
        }
        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout=lt
        )

        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE

        self.add(graph)

        edges[0].add_to_current_flow(20, self)
        self.wait(3, frozen_frame=False)
        edges[0].add_to_current_flow(50, self)
        self.wait(10, frozen_frame=False)
        edges[0].add_to_current_flow(20, self)
        self.wait(3, frozen_frame=False)
