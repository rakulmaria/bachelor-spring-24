from manim import *
from edge import Edge


class Flow(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_center = np.array([2, 0, 0])
        self.edges = {}

        p1 = np.array([-4, 0, 0])
        p2 = np.array([0, 0, 0])
        p3 = np.array([6, 2, 0])
        p4 = np.array([7, -1, 0])
        p5 = np.array([8, 2, 0])

        self.add_edges(
            [
                ["edge1", p1, p2, 4],
                ["edge2", p2, p3, 3],
                ["edge3", p2, p4, 2],
                ["edge4", p4, p5, 3],
                ["edge5", p3, p5, 2],
            ]
        )

        g = BackgroundGraph(self.edges.values())
        a = ArrowGraph(self.edges)

        self.add(g)
        self.add_foreground_mobject(a)

        # Flow

        flow_edges_1 = [
            self.edges["edge1"],
            self.edges["edge2"],
            self.edges["edge5"],
        ]

        f1 = FlowGraph(flow_edges_1, 0)
        f2 = FlowGraph(flow_edges_1, 2)

        self.play(Transform(f1, f2, run_time=2))

        # Should be done another way

        flow_edges_2 = [
            self.edges["edge1"],
            self.edges["edge3"],
            self.edges["edge4"],
        ]

        f3 = FlowGraph(flow_edges_2, 0)
        f4 = FlowGraph(flow_edges_2, 2)

        self.play(Transform(f3, f4, run_time=2))

    def add_edges(self, lst):
        for id, start_node, end_node, max_capacity in lst:
            self.edges[id] = Edge(id, start_node, end_node, max_capacity)


class FlowGraph(Mobject):
    def __init__(self, edge_points, c):
        super().__init__()
        for edge in edge_points:
            g = GraphSegment(
                edge.start_node, edge.end_node, (c + edge.current_capacity), GREY
            )
            edge.add_to_current_capacity(c)
            self.add(g)


class ArrowGraph(Mobject):
    def __init__(self, edges: dict):
        super().__init__()
        for edge in edges.values():

            a = CustomArrow(edge.start_node, edge.end_node)

            self.add(a)


class BackgroundGraph(Mobject):
    def __init__(self, edges: dict):
        super().__init__()
        for edge in edges:
            g = GraphSegment(
                edge.get_start_node(), edge.end_node, edge.max_capacity, WHITE
            )
            b = GraphSegment(
                edge.start_node, edge.end_node, (edge.max_capacity + 0.2), BLACK
            )

            self.add_to_back(b)
            self.add(g)


class CustomArrow(Mobject):
    def __init__(self, p1, p2):
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


class GraphSegment(Mobject):
    def __init__(self, p1, p2, scale, color):
        super().__init__()
        l = Line(p1, p2)

        l.set_stroke(width=(scale * 16))

        c1 = Dot(p1).scale(scale)
        c2 = Dot(p2).scale(scale)

        g = VGroup(l, c1, c2)

        g.set_fill(color=color)
        g.set_stroke(color=color)

        self.add(g)
