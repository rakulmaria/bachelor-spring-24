from manim import *
from ford_fulkerson import FordFulkerson
from network import Network
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class Test(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()
        lt = {
            0: [-2, 0, 0],
            1: [-1, 1, 0],
            2: [-1, -1, 0],
            3: [1, 1, 0],
            4: [1, -1, 0],
            5: [2, 0, 0],
        }

        graph = Network(
            vertices, edges, capacities, layout=lt, source=source, sink=sink
        )
        self.camera.background_color = WHITE

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices, edges, capacities = V.simple_graph()

        lt = {
            0: [0, -1, 0],
            1: [2, 1, 0],
        }

        graph = Network(
            vertices, edges, capacities, layout=lt, growth_scale=GrowthScale.LOG2
        )
        self.camera.background_color = WHITE

        self.add(graph)


class Test3(Scene):
    def construct(self):
        vertices, edges, capacities = V.kleinberg_tardos()

        layers = [1, 2, 1]

        graph = Network(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
        )

        self.camera.background_color = WHITE

        self.add(graph)

        graph.add_to_current_flow_temp(10, [(0, 1), (1, 3)], scene=self)
        # self.wait(2)
        graph.add_to_current_flow_temp(10, [(0, 1), (1, 2), (2, 3)], scene=self)
        # # # self.wait(2)
        graph.add_to_current_flow_temp(10, [(0, 2), (2, 3)], scene=self)


class Test4(Scene):
    def construct(self):
        vertices, edges, capacities = V.kleinberg_tardos_small()

        layers = [1, 2, 1]

        graph = Network(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
        )

        self.camera.background_color = WHITE

        self.add(graph)

        graph.add_to_current_flow_temp(1, [(0, 1), (1, 3)], scene=self)
        # self.wait(2)
        graph.add_to_current_flow_temp(1, [(0, 1), (1, 2), (2, 3)], scene=self)
        # # # self.wait(2)
        graph.add_to_current_flow_temp(1, [(0, 2), (2, 3)], scene=self)


class Test5(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()

        layers = [1, 2, 2, 1]

        graph = Network(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
        )

        self.camera.background_color = WHITE
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        max_flow = ford_fulkerson.find_max_flow(self)

        print(max_flow)

        self.wait(2)
