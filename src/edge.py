from manim import *
from src.arrow import EdgeArrow
from src.flow_object import FlowPolygon
from src.utils import GrowthScale, get_drawn_size


class Edge(VMobject):
    def __init__(
        self,
        start_vertex,
        end_vertex,
        max_capacity,
        current_flow=0,
        growth_scale=GrowthScale.SQRT,
    ):
        super().__init__()

        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow
        self.growth_scale = growth_scale

        (init_start_coord, init_end_coord), init_direction = self.get_flow_coords(0)

        self.flow_object = FlowPolygon(
            init_start_coord,
            init_end_coord,
            init_direction,
            0,
            growth_scale=self.growth_scale,
        )

        start_vertex.add_adjacent_edge(self)
        end_vertex.add_adjacent_edge(self)

        start_vertex.add_to_max_outgoing_capacity(max_capacity)
        end_vertex.add_to_max_ingoing_capacity(max_capacity)

    def add_current_flow_towards(self, vertex, new_flow, scene: Scene):
        # if the vertex is start_vertex, we're regret a previous flow
        # we found another augmenting path
        if vertex is self.start_vertex.id:
            new_flow = -1 * new_flow
        if new_flow + self.current_flow > self.max_capacity:
            print("Error: New capacity exceeds maximum capacity")
        if new_flow + self.current_flow < 0:  # for negative values
            print("Error: New capacity gives a negative flow")
        else:
            self.current_flow += new_flow

            (new_start_coord, new_end_coord), new_direction = self.get_flow_coords(
                self.current_flow
            )
            new_flow_object = FlowPolygon(
                new_start_coord,
                new_end_coord,
                new_direction,
                flow=self.current_flow,
                growth_scale=self.growth_scale,
            )

            arrow_animation = None

            if self.current_flow == self.max_capacity:
                arrow_animation = Uncreate(self.arrow)
            else:
                (a, b), _ = self.get_flow_coords(new_flow, arrow_coords=True)
                new_arrow = EdgeArrow(a, b)
                arrow_animation = ReplacementTransform(self.arrow, new_arrow)
                self.arrow = new_arrow

            scene.play(
                ReplacementTransform(self.flow_object, new_flow_object), arrow_animation
            )
            self.flow_object = new_flow_object

    def get_drawn_edge_size(self, cap):
        return get_drawn_size(growth_scale=self.growth_scale, size=cap) * 8

    def draw(self):
        backgroundLine = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            z_index=0,
            color=BLACK,
            stroke_width=(self.get_drawn_edge_size(self.max_capacity) + 1.6),
        )
        self.foregroundLine = (
            Line(
                start=self.start_vertex.to_np_array(),
                end=self.end_vertex.to_np_array(),
                z_index=3,
            )
            .set_stroke(width=self.get_drawn_edge_size(self.max_capacity), color=WHITE)
            .set_fill(color=WHITE)
        )
        self.arrow = EdgeArrow(
            self.start_vertex.to_np_array(), self.end_vertex.to_np_array()
        )

        self.add(backgroundLine)
        self.add(self.foregroundLine)
        self.add(self.arrow)

    def get_flow_coords(self, new_flow, arrow_coords=False):
        x_start = self.start_vertex.x_coord
        y_start = self.start_vertex.y_coord
        x_end = self.end_vertex.x_coord
        y_end = self.end_vertex.y_coord
        half_line_width = (self.get_drawn_edge_size(self.max_capacity) / 100) / 2
        height_to_new_point = half_line_width - (
            self.get_drawn_edge_size(new_flow) / 100 / 2
        )

        v1 = x_end - x_start
        v2 = y_end - y_start
        z1 = -v2
        z2 = v1

        vector = np.array([z1, z2, 0])
        original_vector = np.array([v1, v2, 0])

        if arrow_coords:
            height_to_new_point = self.get_drawn_edge_size(self.current_flow) / 100 / 2
            vector = np.array([-z1, -z2, 0])

        direction = vector / np.linalg.norm(vector)
        scaled_vector = direction * height_to_new_point

        direction_original = original_vector / np.linalg.norm(original_vector)

        start_coord = self.start_vertex.to_np_array() + scaled_vector
        end_coord = self.end_vertex.to_np_array() + scaled_vector

        return (
            start_coord,
            end_coord,
        ), direction_original

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
