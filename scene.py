from manim import *
from edge import Edge

class Flow(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        v0 = np.array([0, 6, 0])
        v1 = np.array([-4, 2, 0])
        v2 = np.array([4, 2, 0])
        v3 = np.array([-4, -2, 0])
        v4 = np.array([4, -2, 0])
        v5 = np.array([0, -6, 0])

        # m1 = GraphSegment(p1, p2, 5, WHITE)
        # b1 = GraphSegment(p1, p2, 5.5, BLACK)
        # c2 = GraphSegment(p1, p2, 0, GREY_B)
        # c3 = GraphSegment(p1, p2, 3, GREY_B)

        self.edges = {}

        self.add_edges(
            [
                ["edge0_to_1", v0, v1, 2],
                ["edge0_to_2", v0, v2, 3],
                ["edge1_to_3", v1, v3, 3],
                ["edge1_to_4", v1, v4, 1],
                ["edge2_to_3", v2, v3, 1],
                ["edge2_to_4", v2, v4, 1],
                ["edge3_to_5", v3, v5, 3],
                ["edge4_to_5", v4, v5, 3],
            ]
        )

        g = BackgroundGraph(self.edges.values())
        a = ArrowGraph(self.edges)

        self.add(g)
        self.add_foreground_mobject(a)

        self.camera.frame_width = 25
        self.camera.resize_frame_shape(0)

        # Flow
        flow_edges_0_1_3_5 = [
            self.edges["edge0_to_1"],
            self.edges["edge1_to_3"],
            self.edges["edge3_to_5"],
        ]

        flow_1_before = FlowGraph(flow_edges_0_1_3_5, 0)
        flow_1_after = FlowGraph(flow_edges_0_1_3_5, 2)

        self.play(ReplacementTransform(flow_1_before, flow_1_after, run_time=2))

        flow_edges_0_2_4_5 = [
            self.edges["edge0_to_2"],
            self.edges["edge2_to_4"],
            self.edges["edge4_to_5"],
        ]

        flow_2_before = FlowGraph(flow_edges_0_2_4_5, 0)
        flow_2_after = FlowGraph(flow_edges_0_2_4_5, 1)

        self.play(ReplacementTransform(flow_2_before, flow_2_after, run_time=2))

        flow_edges_0_1_4_5 = [
            self.edges["edge0_to_1"],
            self.edges["edge1_to_4"],
            self.edges["edge4_to_5"],
        ]

        flow_edges_1_3_5 = [
            self.edges["edge1_to_3"],
            self.edges["edge3_to_5"],
        ]

        flow_edges_4_5 = [
            self.edges["edge4_to_5"],
        ]


        #flow_1_redirect1 = FlowGraph(flow_edges_1_3_5, 0, False)
        #flow_1_redirect2 = FlowGraph(flow_edges_1_3_5, 1, False)

        #self.play(Transform(flow_1_after, flow_1_before, run_time=2))
        
        self.play(ReplacementTransform(flow_1_after, FlowGraph(flow_edges_0_1_3_5, -1), run_time=2))

        flow_3_before = FlowGraph(flow_edges_0_1_4_5, 0)
        flow_3_after = FlowGraph(flow_edges_0_1_4_5, 1)

        self.play(ReplacementTransform(flow_3_before, flow_3_after, run_time=2))

        flow_edges_0_2_3_5 = [
            self.edges["edge0_to_2"],
            self.edges["edge2_to_3"],
            self.edges["edge3_to_5"],
        ]

        flow_edges_0_2 = [
            self.edges["edge0_to_2"],
        ]

        flow_edge_3_5 = [
            self.edges["edge3_to_5"],
        ]


        flow_4_before = FlowGraph(flow_edges_0_2_3_5, 0)
        flow_4_after = FlowGraph(flow_edges_0_2_3_5, 1)

        self.play(ReplacementTransform(flow_4_before, flow_4_after, run_time=2))



        # flow_edges_1 = [
        #     self.edges["edge1"],
        #     self.edges["edge2"],
        #     self.edges["edge5"],
        # ]

        # f1 = FlowGraph(flow_edges_1, 0)
        # f2 = FlowGraph(flow_edges_1, 2)

        # self.play(Transform(f1, f2, run_time=2))

        # # Should be done another way

        # flow_edges_2 = [
        #     self.edges["edge1"],
        #     self.edges["edge3"],
        #     self.edges["edge4"],
        # ]

        # f3 = FlowGraph(flow_edges_2, 0)
        # f4 = FlowGraph(flow_edges_2, 2)

        # self.play(Transform(f3, f4, run_time=2))

    def SetLabel(self, x, y, label) -> VMobject:
        label = Tex(label, color=BLACK).set_x(x).set_y(y)

        self.add_foreground_mobject(label)

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
    def __init__(self, p1, p2, scale, color, label=None):
        super().__init__()
        
        l = Line(p1, p2)

        if label!= None:
            label = Text(label, color=BLACK)
            self.add(label).set_x(p1[0])

        l.set_stroke(width=(scale * 16))

        c1 = Dot(p1).scale(scale)
        c2 = Dot(p2).scale(scale)

        g = VGroup(l, c1, c2)

        g.set_fill(color=color)
        g.set_stroke(color=color)


        self.add(g)
