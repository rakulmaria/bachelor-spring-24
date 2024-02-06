from manim import *


class Flow(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_center = np.array([2, 0, 0])

        p1 = np.array([-4, 0, 0])
        p2 = np.array([0, 0, 0])
        p3 = np.array([6, 2, 0])
        p4 = np.array([7, -1, 0])
        p5 = np.array([8, 2, 0])

        edge_points_and_cap = [
            ((p1, p2), 4),
            ((p2, p3), 3),
            ((p2, p4), 2),
            ((p4, p5), 3),
            ((p3, p5), 2),
        ]

        g = BackgroundGraph(edge_points_and_cap)
        a = ArrowGraph(edge_points_and_cap)

        self.add(g)
        self.add_foreground_mobject(a)

        # Flow

        flow_edges_1 = [
            (p1, p2),
            (p2, p3),
            (p3, p5),
        ]

        f1 = FlowGraph(flow_edges_1, 0)
        f2 = FlowGraph(flow_edges_1, 2)

        self.play(Transform(f1, f2, run_time=2))

        # Should be done another way

        custom_flow11 = GraphSegment(p1, p2, 2, GREY)
        custom_flow12 = GraphSegment(p2, p4, 0, GREY)
        custom_flow13 = GraphSegment(p4, p5, 0, GREY)
        g1 = Group(custom_flow11, custom_flow12, custom_flow13)

        custom_flow21 = GraphSegment(p1, p2, 4, GREY)
        custom_flow22 = GraphSegment(p2, p4, 2, GREY)
        custom_flow23 = GraphSegment(p4, p5, 2, GREY)
        g2 = Group(custom_flow21, custom_flow22, custom_flow23)
        self.play(Transform(g1, g2, run_time=2))


class FlowGraph(Mobject):
    def __init__(self, edge_points, c):
        super().__init__()
        for i in range(len(edge_points)):
            (p1, p2) = edge_points[i]
            g = GraphSegment(p1, p2, c, GREY)
            self.add(g)


class ArrowGraph(Mobject):
    def __init__(self, edge_points):
        super().__init__()
        for i in range(len(edge_points)):
            (p1, p2), c = edge_points[i]

            a = CustomArrow(p1, p2)

            self.add(a)


class BackgroundGraph(Mobject):
    def __init__(self, edge_points_and_cap):
        super().__init__()
        for i in range(len(edge_points_and_cap)):
            (p1, p2), c = edge_points_and_cap[i]

            g = GraphSegment(p1, p2, c, WHITE)
            b = GraphSegment(p1, p2, (c + 0.2), BLACK)

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
