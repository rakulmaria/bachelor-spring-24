from manim import *

from src.arrow import EdgeArrow
from src.utils import GrowthScale, get_drawn_size


class FlowPolygon(Line):
    def __init__(
        self,
        flow_start_coord,
        flow_end_coord,
        direction,
        flow,
        growth_scale=GrowthScale.SQRT,
    ):
        size = 9
        self.polygons = VGroup()
        self.growth_scale = growth_scale
        dark_blue = AS2700.B24_HARBOUR_BLUE
        light_blue = AS2700.B41_BLUEBELL
        border_blue = AS2700.B21_ULTRAMARINE
        self.times = 0

        super().__init__(start=flow_start_coord, end=flow_end_coord, z_index=4)
        super().set_stroke(
            width=(self.get_drawn_flow_size(flow)),
            color=light_blue,
        )

        if flow > 0:
            self.add(EdgeArrow(flow_end_coord, flow_start_coord))

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
            object = Polygon(*position_list, z_index=5)
            object.scale(scale_factor)
            object.set_stroke(border_blue, opacity=1.0, width=0.0)

            # set color of every other object to differ
            if len(self.polygons) % 3 == 0:
                object.set_fill(dark_blue, 0.8)
            else:
                object.set_fill(light_blue, 0.8)
            self.polygons.add(object)

        self.polygons.arrange(buff=-1, direction=LEFT)
        self.polygons.move_to(self.get_center())
        self.polygons.stretch_to_fit_width(self.get_length())
        self.polygons.stretch_to_fit_height(self.stroke_width / 100)
        self.polygons.rotate(self.angle_from_vector(direction))
        self.add(self.polygons)

        def update(mobject):
            self.times += 1
            changed = []
            if self.times > 10:
                for i, dot in enumerate(mobject):
                    if i in changed:
                        continue
                    self.times = 0
                    if dot.color == dark_blue:
                        mobject[i].set_fill(light_blue)

                        if (1 + i) < len(mobject):
                            mobject[i + 1].set_fill(dark_blue)
                        else:
                            mobject[0].set_fill(dark_blue)
                        changed.append(i + 1)

        self.polygons.add_updater(update)

    def get_drawn_flow_size(self, flow):
        return get_drawn_size(self.growth_scale, flow) * 8

    def angle_from_vector(self, vector):
        angle_rad = np.arctan2(vector[1], vector[0])
        angle_rad %= 2 * np.pi

        return angle_rad
