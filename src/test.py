from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getEdgesAndVerticesAsMobjects
from src.vertices_examples import VerticesExamples as V
from src.flow_object import FlowPolygon


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

        flow0 = FlowPolygon(edges[0], 0)

        self.play(Create(Dot()), run_time=2)

        flow = FlowPolygon(edges[0], 50)
        self.play(ReplacementTransform(flow0, flow), run_time=1)

        self.play(Create(Dot()), run_time=2)

        flow2 = FlowPolygon(edges[0], 70)
        self.play(ReplacementTransform(flow, flow2), run_time=1)

        self.play(Create(Dot()), run_time=2)
