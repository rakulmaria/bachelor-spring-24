import random
from manim import *
from src.arrow import EdgeArrow
from src.utils import *

ratefunctions = [
    rate_functions.double_smooth,
    rate_functions.linear,
    rate_functions.ease_in_sine,
    rate_functions.ease_out_quad,
    rate_functions.ease_in_quint,
    rate_functions.ease_in_cubic,
    rate_functions.ease_in_out_circ,
]

color_list = color_gradient([AS2700.B32_POWDER_BLUE, AS2700.B45_SKY_BLUE], 6)


class Edge(VMobject):
    def __init__(
        self,
        start_vertex,
        end_vertex,
        max_capacity,
        current_flow=0,
        growth_scale=GrowthScale.SQRT,
        theme=Themes.Light,
        scene: Scene = None,
    ):
        super().__init__()
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow
        self.growth_scale = growth_scale
        self.theme = theme

        start_vertex.add_adjacent_edge(self)
        end_vertex.add_adjacent_edge(self)

        if max_capacity > start_vertex.biggest_capacity:
            start_vertex.biggest_capacity = max_capacity
        if max_capacity > end_vertex.biggest_capacity:
            end_vertex.biggest_capacity = max_capacity

        self.start_vertex_to_updater = {}

    def point_to_tuple(self, point):
        return (point[0], point[1])

    def tuple_to_point(self, tuple):
        return np.array([tuple[0], tuple[1], 0])

    def remove_updater_if_point_is_outside(
        self, scene: Scene, point, top, bottom, top2, bottom2
    ):
        (end_point, updater) = self.start_vertex_to_updater.get(
            self.point_to_tuple(point)
        )
        if not self.is_point_between_two_points(point, top, bottom):
            scene.remove(updater)
        elif not self.is_point_between_two_points(end_point, top2, bottom2):
            scene.remove(updater)

    def add_updater_if_point_is_inside(
        self, scene: Scene, point, top, bottom, top2, bottom2
    ):
        (end_point, updater) = self.start_vertex_to_updater.get(
            self.point_to_tuple(point)
        )
        if self.is_point_between_two_points(point, top, bottom):
            if self.is_point_between_two_points(end_point, top2, bottom2):
                scene.add(updater)

    def is_point_between_two_points(self, x, y, z, tol=1e-9):
        # Calculate the vectors
        vec_yx = x - y
        vec_yz = z - y

        # Check if x is collinear with y and z by seeing if vec_yx is a scalar multiple of vec_yz
        cross_product = np.cross(vec_yx, vec_yz)
        if np.linalg.norm(cross_product) > tol:
            # If the cross product is not (almost) zero, they are not collinear
            return False

        # Check if x lies between y and z
        dot_product = np.dot(vec_yx, vec_yz)
        if dot_product < 0:
            # x is behind y
            return False

        if np.linalg.norm(vec_yx) > np.linalg.norm(vec_yz):
            # x is farther from y than z is, so it's outside the segment
            return False

        # x lies on the line segment between y and z
        return True

    def find_random_points(self, flow_start_coord, flow_end_coord, flow):
        (
            start_fst_coord,
            end_fst_coord,
            start_snd_coord,
            end_snd_coord,
        ) = self.get_flow_coords_2(flow_start_coord, flow_end_coord, flow)
        random_start = start_snd_coord + random.uniform(0.1, 0.9) * (
            start_fst_coord - start_snd_coord
        )
        random_end = end_snd_coord + random.uniform(0.1, 0.9) * (
            end_fst_coord - end_snd_coord
        )
        return random_start, random_end

    def get_flow_coords_2(self, flow_start_coord, flow_end_coord, flow):
        a, b = (
            (flow_end_coord[0] - flow_start_coord[0]),
            (flow_end_coord[1] - flow_start_coord[1]),
        )
        orthogonal_vector = np.array([-b, a, 0])
        half_line_width = (flow * 8 / 100) / 2

        return self.get_offset_points_2(
            half_line_width, orthogonal_vector, flow_start_coord, flow_end_coord
        )

    def get_offset_points_2(
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

    def add_first_flow(self, scene: Scene):
        for i in range(int(self.max_capacity) * 20):
            random_start, random_end = self.find_random_points(
                self.start_vertex.to_np_array(),
                self.end_vertex.to_np_array(),
                self.max_capacity,
            )
            line = Line(random_start, random_end)
            dot = (
                Dot()
                .set_color(ManimColor.from_hex(random.choice(self.theme.get("DOTS"))))
                .scale(0.2)
            ).set_z_index(5)

            self.add(dot)

            ani = MoveAlongPath(
                dot,
                line,
                rate_func=ratefunctions[i % len(ratefunctions)],
                run_time=random.randint(5, 12),
            )

            updater = turn_animation_into_updater(ani, cycle=True)
            scene.remove(updater)
            self.start_vertex_to_updater.update(
                {self.point_to_tuple(random_start): (random_end, updater)}
            )

    def add_current_flow_towards(self, vertex_id, new_flow, scene: Scene):
        # if vertex is start_vertex, that means we want to 'undo' a previous choice
        if vertex_id is self.start_vertex.id:
            new_flow = -1 * new_flow

        self.current_flow += new_flow

        # (new_start_coord, new_end_coord) = self.get_flow_coords()
        # new_direction = self.get_direction()

    def add_flow(self, new_flow, scene: Scene, new_start_coord, new_end_coord):
        (
            start_top,
            end_top,
            start_bottom,
            end_bottom,
        ) = self.get_flow_coords_2(new_start_coord, new_end_coord, self.current_flow)

        if self.current_flow - new_flow == 0:
            self.add_first_flow(scene)

        if new_flow > 0:
            for i in self.start_vertex_to_updater.keys():
                self.add_updater_if_point_is_inside(
                    scene,
                    self.tuple_to_point(i),
                    start_top,
                    start_bottom,
                    end_top,
                    end_bottom,
                )
        else:
            for i in self.start_vertex_to_updater.keys():
                self.remove_updater_if_point_is_outside(
                    scene,
                    self.tuple_to_point(i),
                    start_top,
                    start_bottom,
                    end_top,
                    end_bottom,
                )

    def get_drawn_edge_size(self, capacity):
        return get_drawn_size(self.growth_scale, capacity) * 8

    def draw(self):
        background_line = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            color=self.theme.get("BORDER"),
            stroke_width=(self.get_drawn_edge_size(self.max_capacity) + 1.6),
        )

        self.foreground_line = (
            Line(
                start=self.start_vertex.to_np_array(),
                end=self.end_vertex.to_np_array(),
            )
            .set_stroke(
                width=self.get_drawn_edge_size(self.max_capacity),
                color=self.theme.get("OBJECT-BACKGROUND"),
            )
            .set_fill(color=self.theme.get("OBJECT-BACKGROUND"))
            .set_z_index(3)
        )

        self.arrow = EdgeArrow(
            self.start_vertex.to_np_array(), self.end_vertex.to_np_array(), self.theme
        )

        self.add(background_line, self.foreground_line, self.arrow)

    def get_direction(self):
        x_start = self.start_vertex.x_coord
        y_start = self.start_vertex.y_coord
        x_end = self.end_vertex.x_coord
        y_end = self.end_vertex.y_coord
        v1 = x_end - x_start
        v2 = y_end - y_start
        edge_vector = np.array([v1, v2, 0])

        return edge_vector / np.linalg.norm(edge_vector)

    def get_new_arrow_coords(self):
        a, b = self.get_vector_values()
        height_to_new_point = self.get_drawn_edge_size(self.current_flow) / 100 / 2
        orthogonal_vector = np.array([b, -a, 0])

        return self.get_offset_points(height_to_new_point, orthogonal_vector)

    def get_flow_coords(self):
        a, b = self.get_vector_values()
        orthogonal_vector = np.array([-b, a, 0])
        half_line_width = (self.get_drawn_edge_size(self.max_capacity) / 100) / 2
        height_to_new_point = half_line_width - (
            self.get_drawn_edge_size(self.current_flow) / 100 / 2
        )

        return self.get_offset_points(height_to_new_point, orthogonal_vector)

    def get_offset_points(self, offset, orthogonal_vector):
        orthogonal_unit_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector)
        scaled_orthogonal_vector = orthogonal_unit_vector * offset
        start_coord = self.start_vertex.to_np_array() + scaled_orthogonal_vector
        end_coord = self.end_vertex.to_np_array() + scaled_orthogonal_vector

        return (
            start_coord,
            end_coord,
        )

    def get_vector_values(self):
        x_start = self.start_vertex.x_coord
        y_start = self.start_vertex.y_coord
        x_end = self.end_vertex.x_coord
        y_end = self.end_vertex.y_coord

        return (x_end - x_start), (y_end - y_start)

    def get_residual_capacity_to(self, vertex):
        if vertex.id is self.end_vertex.id:
            return self.max_capacity - self.current_flow
        else:
            return self.current_flow

    def get_other_vertex(self, vertex):
        if vertex.id is self.end_vertex.id:
            return self.start_vertex
        else:
            return self.end_vertex

    def get_other_vertex_from_id(self, vertex_id):
        if vertex_id is self.end_vertex.id:
            return self.start_vertex
        else:
            return self.end_vertex

    def get_vertex_from_id(self, vertex_id):
        if vertex_id is self.end_vertex.id:
            return self.end_vertex
        else:
            return self.start_vertex

    def get_active_edges(self):
        active_edges = []
        if self.current_flow > 0:
            active_edges.append((self.end_vertex.id, self.start_vertex.id))
        if self.current_flow < self.max_capacity:
            active_edges.append((self.start_vertex.id, self.end_vertex.id))
        return active_edges
