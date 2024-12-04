from manim import *
from src.utils import *


class Vertex(VMobject):
    def __init__(
        self,
        id,
        x_coord,
        y_coord,
        growth_scale=GrowthScale.SQRT,
        theme=Themes.Light,
        is_sink=False,
        is_source=False,
    ):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.growth_scale = growth_scale
        self.theme = theme
        self.outgoing_capacity = 0
        self.ingoing_capacity = 0
        self.current_flow = 0
        self.adjacent_edges = []
        self.is_sink = is_sink
        self.is_source = is_source
        self.flow_object = None
        self.foreground_dot = None
        self.biggest_capacity = 0

        super().__init__()

    def get_drawn_dot_size(self):
        return get_drawn_size(self.growth_scale, self.biggest_capacity) / 2

    def get_drawn_label_size(self, scale=1):
        return (get_drawn_size(self.growth_scale, scale) + 1.5) * 0.1

    def draw(self, scale=1):
        self.foreground_dot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size())
            .set_fill(self.theme.get("OBJECT-BACKGROUND"))
            .set_z_index(10)
        )

        background_dot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size() + 0.1)
            .set_fill(self.theme.get("BORDER"))
        )

        label = (
            Tex(self.id, color=self.theme.get("TEXT"))
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

    def add_adjacent_edge(self, edge):
        self.adjacent_edges.append(edge)

    def get_max_drawn_capacity(self):
        return self.biggest_capacity
