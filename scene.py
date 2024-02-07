from manim import *


class Graph(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        v0 = np.array([0, 6, 0])
        v1 = np.array([-4, 2, 0])
        v2 = np.array([4, 2, 0])
        v3 = np.array([-4, -2, 0])
        v4 = np.array([4, -2, 0])
        v5 = np.array([0, -6, 0])

        m1 = GraphSegment(p1, p2, 5, WHITE)
        b1 = GraphSegment(p1, p2, 5.5, BLACK)

        c2 = GraphSegment(p1, p2, 0, GREY_B)
        c3 = GraphSegment(p1, p2, 3, GREY_B)

        m2 = GraphSegment(p2, p3, 3, WHITE)
        b2 = GraphSegment(p2, p3, 3.5, BLACK)
        c4 = GraphSegment(p2, p3, 0, GREY_B)
        c5 = GraphSegment(p2, p3, 3, GREY_B)

        ar1 = CustomArrow(p1, p2)
        ar2 = CustomArrow(p2, p3)

        self.add(b1)
        self.add(b2)
        self.add(m1)
        self.add(m2)
        self.add_foreground_mobject(ar1)
        self.add_foreground_mobject(ar2)

        self.SetLabel(p1[0], p1[1], "1")
        self.SetLabel(p2[0], p2[1], "2")
        self.SetLabel(p3[0], p3[1], "3")

        self.play(Transform(c2, c3, run_time=2))
        self.wait(1)
        self.play(Transform(c4, c5, run_time=2))
    
    def SetLabel(self, x, y, label) -> VMobject:
        label = Tex(label, color=BLACK).set_x(x).set_y(y)

        self.add_foreground_mobject(label)


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
