from manim import *
from numpy import ndarray
from edge import Edge
from vertex import Vertex


class Flow(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 20
        self.camera.resize_frame_shape(0)
        self.camera.frame_center = np.array([2, 0, 0])
        self.edges = {}
        self.vertices = {}

        self.add_vertices(
            [
                ["vertex1", -4, 0],
                ["vertex2", 0, 0],
                ["vertex3", 6, 2],
                ["vertex4", 7, -1],
                ["vertex5", 8, 2],
            ]
        )

        self.add_edges(
            [
                ["edge1", self.vertices["vertex1"], self.vertices["vertex2"], 4],
                ["edge2", self.vertices["vertex2"], self.vertices["vertex3"], 3],
                ["edge3", self.vertices["vertex2"], self.vertices["vertex4"], 2],
                ["edge4", self.vertices["vertex4"], self.vertices["vertex5"], 3],
                ["edge5", self.vertices["vertex3"], self.vertices["vertex5"], 2],
            ]
        )

        g = BackgroundGraph(self.edges.values())
        a = ArrowGraph(self.edges.values())
        l = GraphLabel(self.vertices.values())

        self.add(g)
        self.add_foreground_mobject(a)
        self.add_foreground_mobject(l)

        # Flow 1
        flow_edges_1 = [
            self.edges["edge1"],
            self.edges["edge2"],
            self.edges["edge5"],
        ]

        f1 = FlowGraph(flow_edges_1, 0)
        f2 = FlowGraph(flow_edges_1, 2)

        self.play(ReplacementTransform(f1, f2, run_time=2))

        # Flow 2
        flow_edges_2 = [
            self.edges["edge1"],
            self.edges["edge3"],
            self.edges["edge4"],
        ]

        f3 = FlowGraph(flow_edges_2, 0)
        f4 = FlowGraph(flow_edges_2, 2)

        self.play(ReplacementTransform(f3, f4, run_time=2))

    def add_edges(self, lst):
        for id, start_node, end_node, max_capacity in lst:
            self.edges[id] = Edge(id, start_node, end_node, max_capacity)

    def add_vertices(self, lst):
        for id, x_coord, y_coord in lst:
            self.vertices[id] = Vertex(id, x_coord, y_coord)


class FlowGraph(Mobject):
    def __init__(self, edges: list[Edge], c):
        super().__init__()
        for edge in edges:
            g = GraphSegment(
                edge.start_node.to_np_array(),
                edge.end_node.to_np_array(),
                (edge.current_flow + c),
                GREY,
            )
            edge.add_to_current_flow(c)
            self.add(g)


class ArrowGraph(Mobject):
    def __init__(self, edges: list[Edge]):
        super().__init__()
        for edge in edges:
            a = CustomArrow(edge.start_node.to_np_array(), edge.end_node.to_np_array())
            self.add(a)


class CustomArrow(Mobject):
    def __init__(self, p1: ndarray, p2: ndarray):
        super().__init__()
        midpoint = (p1 + p2) / 2
        fixed_length = 1.5
        direction_vector = normalize(p2 - p1)
        start_point = midpoint - fixed_length / 2 * direction_vector
        end_point = midpoint + fixed_length / 2 * direction_vector

        arr = Arrow(start_point, end_point, tip_length=0.2)
        arr.set_fill(color=RED_E)
        arr.set_stroke(color=RED_E)

        self.add(arr)


class GraphLabel(Mobject):
    def __init__(self, vertecies: list[Vertex]):
        super().__init__()
        for i, vertex in enumerate(vertecies):
            label = Label(vertex, str(i))
            self.add(label)


class Label(Mobject):
    def __init__(self, vertex: Vertex, label: str):
        super().__init__()
        label = Tex(label, color=BLACK).set_x(vertex.x_coord).set_y(vertex.y_coord)

        self.add(label)


class BackgroundGraph(Mobject):
    def __init__(self, edges: list[Edge]):
        super().__init__()
        for edge in edges:
            g = GraphSegment(
                edge.start_node.to_np_array(),
                edge.end_node.to_np_array(),
                edge.max_capacity,
                WHITE,
            )
            b = GraphSegment(
                edge.start_node.to_np_array(),
                edge.end_node.to_np_array(),
                (edge.max_capacity + 0.2),
                BLACK,
            )

            self.add_to_back(b)
            self.add(g)


class GraphSegment(Mobject):
    def __init__(self, p1: ndarray, p2: ndarray, scale: int, color):
        super().__init__()
        l = Line(p1, p2)

        l.set_stroke(width=(scale * 16))

        c1 = Dot(p1).scale(scale)
        c2 = Dot(p2).scale(scale)

        g = VGroup(l, c1, c2)

        g.set_fill(color=color)
        g.set_stroke(color=color)

        self.add(g)
