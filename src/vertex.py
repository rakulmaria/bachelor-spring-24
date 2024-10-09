from manim import *
from src.utils import GrowthScale, get_drawn_size
import src.colors as colors


class Vertex(VMobject):
    def __init__(
        self,
        id,
        x_coord,
        y_coord,
        growth_scale=GrowthScale.SQRT,
        is_sink=False,
        is_source=False,
    ):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.growth_scale = growth_scale
        self.outgoing_capacity = 0
        self.ingoing_capacity = 0
        self.current_flow = 0
        self.adjacent_edges = []
        self.is_sink = is_sink
        self.is_source = is_source
        self.flow_object = None
        self.foreground_dot = None

        super().__init__()

    def get_drawn_dot_size(self):
        return (
            get_drawn_size(self.growth_scale, self.get_max_drawn_capacity()) / 2 + 0.5
        )

    def get_drawn_label_size(self, scale=1):
        return (get_drawn_size(self.growth_scale, scale) + 0.5) * 0.2

    def draw(self, scale=1):
        self.foreground_dot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size())
            .set_fill(WHITE)
            .set_z_index(10)
        )

        background_dot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size() + 0.1)
            .set_fill(BLACK)
        )

        label_text = self.id

        if self.is_sink:
            label_text = "t"
        elif self.is_source:
            label_text = "s"

        label = (
            Tex(label_text, color=BLACK)
            .set_x(self.x_coord)
            .set_y(self.y_coord)
            .set_z_index(20)
            .scale(self.get_drawn_label_size(scale))
        )

        self.add(background_dot, self.foreground_dot, label)

    def to_np_array(self):
        return np.array([self.x_coord, self.y_coord, 0])

    def set_sink(self):
        self.is_sink = True

    def set_source(self):
        self.is_source = True

    def add_to_max_ingoing_capacity(self, capacity):
        self.ingoing_capacity = capacity

    def add_to_max_outgoing_capacity(self, capacity):
        self.outgoing_capacity = capacity

    def add_adjacent_edge(self, edge):
        self.adjacent_edges.append(edge)

    def get_max_drawn_capacity(self):
        return max(self.outgoing_capacity, self.ingoing_capacity)

    def get_opacity(self):
        return self.current_flow / self.get_max_opacity()

    def get_max_opacity(self):
        # edge case for source and sink vertices
        if self.ingoing_capacity == 0 or self.outgoing_capacity == 0:
            return max(self.ingoing_capacity, self.outgoing_capacity)
        return min(self.ingoing_capacity, self.outgoing_capacity)

    def add_to_current_flow(self, new_flow):
        if self.flow_object is None:
            self.flow_object = (
                Dot(self.to_np_array())
                .scale(self.get_drawn_dot_size())
                .set_fill(colors.light_blue)
                .set_opacity(0)
                .set_z_index(12)
            )

        self.current_flow += new_flow
        new_flow_object = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size())
            .set_fill(colors.light_blue)
            .set_opacity(self.get_opacity())
            .set_z_index(12)
        )

        vertex_animation = ReplacementTransform(self.flow_object, new_flow_object)
        self.flow_object = new_flow_object
        return vertex_animation
