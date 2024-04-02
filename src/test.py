from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getEdgesAndVerticesAsMobjects, getMaxCapacity
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
        vertices, edges, capacities = V.SedgewickWayne()
        edgeScale = getMaxCapacity(capacities)
        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout_scale=edgeScale
        )

        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE

        self.add(graph)
