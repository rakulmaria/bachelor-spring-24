from manim import *
from src.ford_fulkerson import FordFulkerson
from src.flow_network import FlowNetwork
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale


class SedgewickWayne(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()

        layers = [1, 2, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
        )

        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self)

        self.wait(2)


class WikiExample(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.wiki_example()

        layers = [1, 5, 5, 3, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=3,
        )

        self.camera.frame_width = 14
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self)

        self.wait(2)


class BigGraph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.silkes_big_graph()

        lt = {
            1: [-5, 0, 0],
            2: [-3, 3, 0],
            3: [-3, 0, 0],
            4: [-3, -3, 0],
            5: [-1, 4, 0],
            6: [-1, 2, 0],
            7: [-1, -2, 0],
            8: [-1, -4, 0],
            9: [1, 4, 0],
            10: [1, 2, 0],
            11: [1, -2, 0],
            12: [1, -4, 0],
            13: [3, 3, 0],
            14: [3, 0, 0],
            15: [3, -3, 0],
            16: [5, 0, 0],
        }

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout=lt,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=3,
        )

        self.camera.frame_width = 15
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self)

        self.wait(2)


class ThoresExampleDFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()

        layers = [1, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=4,
        )

        self.camera.frame_width = 10
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self, BSF=False)

        self.wait(2)


class ThoresExampleBFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()

        layers = [1, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=4,
        )

        self.camera.frame_width = 10
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph)
        ford_fulkerson.find_max_flow(self)

        self.wait(2)
