from manim import *
from src.arrow import EdgeArrow
from src.flow_object import FlowObject
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

        # initial flow_object is empty
        (init_start_coord, init_end_coord) = self.get_flow_coords()
        init_direction = self.get_direction()
        self.flow_object = FlowObject(
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

    def add_current_flow_towards(self, vertex, new_flow, scene: Scene, run_time=2):
        # if vertex is start_vertex, we found another augmenting path and want to 'undo' a previous mistake
        if vertex is self.start_vertex.id:
            new_flow = -1 * new_flow
        if new_flow + self.current_flow > self.max_capacity:
            print("Error: New capacity exceeds maximum capacity")
        if new_flow + self.current_flow < 0:  # for negative values
            print("Error: New capacity gives a negative flow")
        else:
            vertex_animation = self.start_vertex.add_to_current_flow(new_flow)

            self.current_flow += new_flow

            (new_start_coord, new_end_coord) = self.get_flow_coords()
            new_direction = self.get_direction()

            new_flow_object = FlowObject(
                new_start_coord,
                new_end_coord,
                new_direction,
                self.current_flow,
                self.growth_scale,
            )
            edge_animation = ReplacementTransform(self.flow_object, new_flow_object)
            arrow_to_use = self.focused_arrow
            if new_flow < 0:
                arrow_to_use = self.arrow
            if self.current_flow == self.max_capacity:
                arrow_animation = Uncreate(arrow_to_use)
            else:
                (
                    new_arrow_start_coord,
                    new_arrow_end_coord,
                ) = self.get_new_arrow_coords()

                new_arrow = (
                    EdgeArrow(new_arrow_start_coord, new_arrow_end_coord)
                    .scale(1.2)
                    .set_color(YELLOW)
                )

                self.arrow = EdgeArrow(new_arrow_start_coord, new_arrow_end_coord)
                arrow_animation = ReplacementTransform(arrow_to_use, self.arrow)
                self.focused_arrow = new_arrow

                self.focused_arrow = (
                    EdgeArrow(new_arrow_start_coord, new_arrow_end_coord)
                    .scale(1.2)
                    .set_color(YELLOW)
                )

            scene.play(
                edge_animation,
                vertex_animation,
                arrow_animation,
                run_time=run_time,
            )

            # edge case for end vertex. end by playing the animation by coloring the sink vertex blue
            if self.end_vertex.is_sink:
                vertex_animation_end_vertex = self.end_vertex.add_to_current_flow(
                    new_flow
                )
                scene.play(vertex_animation_end_vertex)

            self.flow_object = new_flow_object

    def get_arrow_animation_towards(self, vertex):
        if vertex is self.end_vertex.id:
            return Indicate(self.arrow)
        else:
            return Indicate(self.flow_object.arrow)

    def play_arrow_focus_animation_towards(self, vertex, scene):
        if vertex is self.end_vertex.id:
            scene.play(ReplacementTransform(self.arrow, self.focused_arrow))
        else:
            scene.play(
                ReplacementTransform(
                    self.flow_object.arrow, self.flow_object.focused_arrow
                )
            )

    def get_drawn_edge_size(self, capacity):
        return get_drawn_size(self.growth_scale, capacity) * 8

    def draw(self):
        background_line = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            z_index=0,
            color=BLACK,
            stroke_width=(self.get_drawn_edge_size(self.max_capacity) + 1.6),
        )
        foreground_line = (
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

        self.focused_arrow = (
            EdgeArrow(self.start_vertex.to_np_array(), self.end_vertex.to_np_array())
            .scale(1.2)
            .set_color(YELLOW)
        )

        self.add(background_line)
        self.add(foreground_line)
        self.add(self.arrow)

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
