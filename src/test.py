from manim import *
from src.graph import FlowGraph
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

        graph = FlowGraph(vertices, edges, capacities, layout=lt, growth_scale="log2")
        self.camera.background_color = WHITE

        self.add(graph)

        """ edges[0].add_to_current_flow(20, self)
        self.wait(3, frozen_frame=False)
        edges[0].add_to_current_flow(50, self)
        self.wait(10, frozen_frame=False)
        edges[0].add_to_current_flow(20, self)
        self.wait(3, frozen_frame=False)
 """


class Test4(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


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
            growth_scale="sqrt",
        )

        for vertex in graph.vertices:
            print(
                vertex.id,
                "outgoing:",
                vertex.outgoing_capacity,
                "ingoing:",
                vertex.ingoing_capacity,
                "max_opacity:",
                vertex.get_max_opacity(),
            )

        self.camera.background_color = WHITE
        self.add(graph)

        self.wait(1)

        graph.addToCurrentFlowTemp(10, [(0, 1), (1, 3)], scene=self)
        # self.wait(2)
        graph.addToCurrentFlowTemp(10, [(0, 1), (1, 2), (2, 3)], scene=self)
        # # # self.wait(2)
        graph.addToCurrentFlowTemp(10, [(0, 2), (2, 3)], scene=self)
