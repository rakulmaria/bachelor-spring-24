from manim import *


class FlowPolygon(VMobject):
    def __init__(self, size):
        super().__init__()
        self.polygons = VGroup()
        darkBlue = AS2700.B24_HARBOUR_BLUE
        lightBlue = AS2700.B41_BLUEBELL
        borderBlue = AS2700.B21_ULTRAMARINE
        self.times = 0

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
            # obj.stretch(2, dim=1)
            obj.set_stroke(borderBlue, opacity=1.0)

            # set color of every other object to differ
            if len(self.polygons) % 3 == 0:
                obj.set_fill(darkBlue, 0.8)
            else:
                obj.set_fill(lightBlue, 0.8)
            self.polygons.add(obj)

        # set buff to -1.0 if polygons should touch eachother
        # if buff is negative then the direction should be set to LEFT
        self.polygons.arrange(buff=-1, direction=LEFT)

        self.add(self.polygons)

        def update(mobject):
            self.times += 1
            changed = []
            if self.times > 10:
                for i, dot in enumerate(mobject):
                    if i in changed:
                        continue
                    self.times = 0
                    if dot.color == darkBlue:
                        mobject[i].set_fill(lightBlue)

                        if (1 + i) < len(mobject):
                            mobject[i + 1].set_fill(darkBlue)
                        else:
                            mobject[0].set_fill(darkBlue)
                        changed.append(i + 1)

        self.polygons.add_updater(update)


class PolygonExample(Scene):
    def construct(self):
        test = FlowPolygon(6)
        self.play(Create(test))

        # d = Dot()
        # d.move_to(UP)

        # self.play(Create(d), run_time=20)
        self.wait(2)
