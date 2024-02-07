from manim import *
from numpy import ndarray
from edge import Edge
from vertex import Vertex

class Flow(Scene):
    def construct(self):
        self.camera.background_color = WHITE
<<<<<<< HEAD
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
=======

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
>>>>>>> main
            ]
        )

        g = BackgroundGraph(self.edges.values())
        a = ArrowGraph(self.edges.values())
        l = GraphLabel(self.vertices.values())

        self.SetLabel(v0[0], v0[1], "0")
        self.SetLabel(v1[0], v1[1], "1")
        self.SetLabel(v2[0], v2[1], "2")
        self.SetLabel(v3[0], v3[1], "3")
        self.SetLabel(v4[0], v4[1], "4")
        self.SetLabel(v5[0], v5[1], "5")

        self.add(g)
        self.add_foreground_mobject(a)
        self.add_foreground_mobject(l)

<<<<<<< HEAD
        # Flow 1
        flow_edges_1 = [
            self.edges["edge1"],
            self.edges["edge2"],
            self.edges["edge5"],
=======
        self.camera.frame_width = 25
        self.camera.resize_frame_shape(0)

        # Flow
        flow_edges_0_1_3_5 = [
            self.edges["edge0_to_1"],
            self.edges["edge1_to_3"],
            self.edges["edge3_to_5"],
>>>>>>> main
        ]

        flow_1_before = FlowGraph(flow_edges_0_1_3_5, 0)
        flow_1_after = FlowGraph(flow_edges_0_1_3_5, 2)

<<<<<<< HEAD
        self.play(ReplacementTransform(f1, f2, run_time=2))

        # Flow 2
        flow_edges_2 = [
            self.edges["edge1"],
            self.edges["edge3"],
            self.edges["edge4"],
=======
        t1 = Tex(r"Add 2 units of flow along 0 $\rightarrow$ 1 $\rightarrow$ 3 $\rightarrow$ 5", color=BLACK).set_x(-7).set_y(4)
        
        self.play(Write(t1, run_time=1))

        self.play(ReplacementTransform(flow_1_before, flow_1_after, run_time=2))

        flow_edges_0_2_4_5 = [
            self.edges["edge0_to_2"],
            self.edges["edge2_to_4"],
            self.edges["edge4_to_5"],
>>>>>>> main
        ]

        flow_2_before = FlowGraph(flow_edges_0_2_4_5, 0)
        flow_2_after = FlowGraph(flow_edges_0_2_4_5, 1)

<<<<<<< HEAD
        self.play(ReplacementTransform(f3, f4, run_time=2))
=======
        self.play(FadeOut(t1))
        
        t2 = Tex(r"Add 1 unit of flow along 0 $\rightarrow$ 2  $\rightarrow$ 4 $\rightarrow$ 5", color=BLACK).set_x(-7).set_y(4)
        
        self.play(Write(t2, run_time=1))

        self.play(ReplacementTransform(flow_2_before, flow_2_after, run_time=2))

        flow_edges_0_1_4_5 = [
            self.edges["edge0_to_1"],
            self.edges["edge1_to_4"],
            self.edges["edge4_to_5"],
        ]

        self.play(FadeOut(t2))

        t3 = Tex(r"Redirect 1 unit of flow from 1 $\rightarrow$ 3 $\rightarrow$ 5  to 1 $\rightarrow$ 4 $\rightarrow$ 5", color=BLACK).set_x(-7).set_y(4)

        self.play(Write(t3, run_time=1))

        self.play(ReplacementTransform(flow_1_after, FlowGraph(flow_edges_0_1_3_5, -1), run_time=2))

        flow_3_before = FlowGraph(flow_edges_0_1_4_5, 0)
        flow_3_after = FlowGraph(flow_edges_0_1_4_5, 1)

        self.play(ReplacementTransform(flow_3_before, flow_3_after, run_time=2))

        flow_edges_0_2_3_5 = [
            self.edges["edge0_to_2"],
            self.edges["edge2_to_3"],
            self.edges["edge3_to_5"],
        ]

        self.play(FadeOut(t3))
        t4 = Tex(r"Add 1 unit of flow along 0 $\rightarrow$ 2 $\rightarrow$ 3 $\rightarrow$ 5", color=BLACK).set_x(-7).set_y(4)

        self.play(Write(t4, run_time=1))


        flow_4_before = FlowGraph(flow_edges_0_2_3_5, 0)
        flow_4_after = FlowGraph(flow_edges_0_2_3_5, 1)

        self.play(ReplacementTransform(flow_4_before, flow_4_after, run_time=2))

    def SetLabel(self, x, y, label) -> VMobject:
        label = Tex(label, color=BLACK).set_x(x).set_y(y)

        self.add_foreground_mobject(label)
>>>>>>> main

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
<<<<<<< HEAD
                edge.start_node.to_np_array(),
                edge.end_node.to_np_array(),
                (edge.current_flow + c),
                GREY,
            )
            edge.add_to_current_flow(c)
=======
                edge.start_node, edge.end_node, (c + edge.current_capacity), GREY
                )
            edge.add_to_current_capacity(c)
>>>>>>> main
            self.add(g)


class ArrowGraph(Mobject):
    def __init__(self, edges: list[Edge]):
        super().__init__()
        for edge in edges:
            a = CustomArrow(edge.start_node.to_np_array(), edge.end_node.to_np_array())
            self.add(a)


<<<<<<< HEAD
=======
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

>>>>>>> main
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
<<<<<<< HEAD
    def __init__(self, p1: ndarray, p2: ndarray, scale: int, color):
=======
    def __init__(self, p1, p2, scale, color, label=None):
>>>>>>> main
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
