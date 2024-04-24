from manim import *

from src.arrow import EdgeArrow
from src.utils import GrowthScale, get_drawn_size
import src.colors as colors
from src.updaters import update


class FlowObject(Line):
    def __init__(
        self,
        flow_start_coord,
        flow_end_coord,
        direction,
        flow,
        growth_scale=GrowthScale.SQRT,
    ):
        self.polygons = VGroup()
        self.growth_scale = growth_scale

        super().__init__(start=flow_start_coord, end=flow_end_coord, z_index=4)
        super().set_stroke(
            width=(self.get_drawn_flow_size(flow)),
            color=colors.light_blue,
        )

        if flow > 0:
            self.arrow = EdgeArrow(flow_end_coord, flow_start_coord)
            self.add(self.arrow)

        self.add_polygons(direction)

    def get_drawn_flow_size(self, flow):
        return get_drawn_size(self.growth_scale, flow) * 8

    def angle_from_vector(self, vector):
        angle_rad = np.arctan2(vector[1], vector[0])
        angle_rad %= 2 * np.pi

        return angle_rad

    def add_polygons(self, direction, size=9):
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
            object.scale(0.1)
            object.set_stroke(colors.border_blue, opacity=1.0, width=0.0)

            if len(self.polygons) % 3 == 0:
                object.set_fill(colors.dark_blue, 0.8)
            else:
                object.set_fill(colors.light_blue, 0.8)
            self.polygons.add(object)

        self.polygons.arrange(buff=-1, direction=LEFT)
        self.polygons.move_to(self.get_center())
        self.polygons.stretch_to_fit_width(self.get_length())
        self.polygons.stretch_to_fit_height(self.stroke_width / 100)
        self.polygons.rotate(self.angle_from_vector(direction))
        self.polygons.add_updater(update)

        self.add(self.polygons)
