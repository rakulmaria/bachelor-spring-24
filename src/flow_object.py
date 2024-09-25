import random
from manim import *

from src.arrow import EdgeArrow
from src.utils import GrowthScale, get_drawn_size
import src.colors as colors
from src.updaters import update

ratefunctions = [
    rate_functions.double_smooth,
    rate_functions.linear,
    rate_functions.ease_in_sine,
    rate_functions.ease_out_quad,
    rate_functions.ease_in_quint,
    rate_functions.ease_in_cubic,
    rate_functions.ease_in_out_circ,
]


class FlowObject(Line):
    def __init__(
        self,
        flow_start_coord,
        flow_end_coord,
        direction,
        flow,
        growth_scale=GrowthScale.SQRT,
    ):
        self.growth_scale = growth_scale

        super().__init__(start=flow_start_coord, end=flow_end_coord, z_index=4)
        super().set_stroke(
            width=(self.get_drawn_flow_size(flow)),
            color=colors.light_blue,
        )

        if flow > 0:
            self.arrow = EdgeArrow(flow_end_coord, flow_start_coord)
            self.add(self.arrow)

            self.dot_animations = []
            # setup the dots
            for i in range(int(flow) * 20):
                random_start, random_end = self.find_random_points(
                    flow_start_coord, flow_end_coord, flow
                )
                line = Line(random_start, random_end)

                dot = (
                    Dot()
                    .set_color(ManimColor.from_hex(random.choice(colors.color_list)))
                    .scale(0.2)
                ).set_z_index(5)

                # self.dot_group.add(dot)
                # self.line_group.add(line)
                self.add(dot)

                ani = MoveAlongPath(
                    dot,
                    line,
                    rate_func=ratefunctions[i % len(ratefunctions)],
                    run_time=random.randint(3, 12),
                )

                self.dot_animations.append(ani)

    def find_random_points(self, flow_start_coord, flow_end_coord, flow):
        (
            start_fst_coord,
            end_fst_coord,
            start_snd_coord,
            end_snd_coord,
        ) = self.get_flow_coords(flow_start_coord, flow_end_coord, flow)
        random_start = start_snd_coord + random.uniform(0.1, 0.9) * (
            start_fst_coord - start_snd_coord
        )
        random_end = end_snd_coord + random.uniform(0.1, 0.9) * (
            end_fst_coord - end_snd_coord
        )
        return random_start, random_end

    def get_flow_coords(self, flow_start_coord, flow_end_coord, flow):
        a, b = (
            (flow_end_coord[0] - flow_start_coord[0]),
            (flow_end_coord[1] - flow_start_coord[1]),
        )
        orthogonal_vector = np.array([-b, a, 0])
        half_line_width = (flow * 8 / 100) / 2

        return self.get_offset_points(
            half_line_width, orthogonal_vector, flow_start_coord, flow_end_coord
        )

    def get_offset_points(
        self, offset, orthogonal_vector, flow_start_coord, flow_end_coord
    ):
        orthogonal_unit_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector)
        scaled_orthogonal_vector_fst = orthogonal_unit_vector * offset
        scaled_orthogonal_vector_snd = orthogonal_unit_vector * (-1 * offset)

        start_fst_coord = flow_start_coord + scaled_orthogonal_vector_fst
        end_fst_coord = flow_end_coord + scaled_orthogonal_vector_fst
        start_snd_coord = flow_start_coord + scaled_orthogonal_vector_snd
        end_snd_coord = flow_end_coord + scaled_orthogonal_vector_snd

        return (start_fst_coord, end_fst_coord, start_snd_coord, end_snd_coord)

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
