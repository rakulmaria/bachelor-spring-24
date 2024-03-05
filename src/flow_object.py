from manim import *


class FlowPolygon(VMobject):
    def __init__(self, size):
        super().__init__()
        self.polygons = VGroup()

        # scale object down to 0.1
        scale_factor = 0.1
        position_list = [
            [0, 3, 0],  # top left
            [4, 3, 0],  # top right
            [6, 0, 0],  # middle right
            [4, -3, 0],  # bottom right
            [0, -3, 0],  # bottom left
            [2, 0, 0],  # middle left
        ]

        for _ in range(size):
            obj = Polygon(*position_list)
            obj.scale(scale_factor)
            obj.set_stroke(AS2700.B21_ULTRAMARINE, opacity=1.0)

            # set color of every other object to differ
            if len(self.polygons) % 2 == 0:
                obj.set_fill(AS2700.B41_BLUEBELL, 0.8)
            else:
                obj.set_fill(AS2700.B24_HARBOUR_BLUE, 0.8)
            self.polygons.add(obj)

        # set buff to -1.0 if polygons should touch eachother
        self.polygons.arrange(buff=0.0)

        self.add(self.polygons)


class PolygonExample(Scene):
    def construct(self):
        test = FlowPolygon(10)

        self.play(Write(test))
        self.wait(1)
