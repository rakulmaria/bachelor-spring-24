from manim import *
from src.edge import Edge
import math


class FlowPolygon(Line):
    def __init__(self, edge: Edge, cap):
        size = 9
        self.polygons = VGroup()
        darkBlue = AS2700.B24_HARBOUR_BLUE
        lightBlue = AS2700.B41_BLUEBELL
        borderBlue = AS2700.B21_ULTRAMARINE
        self.times = 0
        (a, b) = get_flow_coords(edge, cap)
        print(a, b, "a,b")
        super().__init__(start=a, end=b, z_index=4)
        super().set_stroke(
            width=((math.sqrt(edge.max_capacity) * 8) / edge.max_capacity * cap),
            color=lightBlue,
        )
        super().set_fill(color=BLUE)

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
            obj = Polygon(*position_list, z_index=5)
            obj.scale(scale_factor)
            obj.set_stroke(borderBlue, opacity=1.0, width=0.0)
            obj.rotate(PI / 2)

            # set color of every other object to differ
            if len(self.polygons) % 3 == 0:
                obj.set_fill(darkBlue, 0.8)
            else:
                obj.set_fill(lightBlue, 0.8)
            self.polygons.add(obj)

        # set buff to -1.0 if polygons should touch eachother
        # if buff is negative then the direction should be set to LEFT
        self.polygons.arrange(buff=-1, direction=UP)
        self.polygons.move_to(self.get_center())
        # self.polygons.stretch_to_fit_height(self.height)
        self.polygons.stretch_to_fit_width(self.stroke_width / 100)
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


def get_flow_coords(edge, cap):
    x_start = edge.start_vertex.x_coord
    y_start = edge.start_vertex.y_coord
    x_end = edge.end_vertex.x_coord
    y_end = edge.end_vertex.y_coord
    h_top = (edge.foregroundLine.stroke_width / 100) / 2
    h = h_top - (h_top / edge.max_capacity * cap)

    v1 = x_end - x_start
    v2 = y_end - y_start
    z1 = -v2
    z2 = v1

    vector = np.array([z1, z2, 0])

    direction = vector / np.linalg.norm(vector)
    print(direction, "direction")
    scaled_vector = direction * h
    print(scaled_vector, "scaled_vector")

    a = edge.start_vertex.to_np_array() + scaled_vector
    b = edge.end_vertex.to_np_array() + scaled_vector

    return (
        a,
        b,
    )


class PolygonExample(Scene):
    def construct(self):
        test = FlowPolygon(6)
        # self.play(Create(test))

        d = Dot()
        d.move_to(UP)

        self.add(test)
        self.play(Create(d), run_time=20)
        self.wait(2)
