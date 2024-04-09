from manim import *
import math

from src.utilities import GrowthScale


class Vertex(VMobject):
    def __init__(
        self, id, x_coord, y_coord, max_capacity, growth_scale=GrowthScale.SQRT
    ):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.max_capacity = max_capacity
        self.opacity = 0
        self.current_flow = 0
        self.growth_scale = growth_scale

        super().__init__()

    def get_drawn_dot_size(self):
        if self.growth_scale == GrowthScale.SQRT:
            return math.sqrt(self.max_capacity) / 2
        if self.growth_scale == GrowthScale.LINEAR:
            return self.max_capacity / 2
        if self.growth_scale == GrowthScale.LOG2:
            return math.log2(self.max_capacity) / 2

    def get_drawn_label_size(self, scale=1):
        if self.growth_scale == GrowthScale.SQRT:
            return math.sqrt(scale) * 0.2
        if self.growth_scale == GrowthScale.LINEAR:
            return scale * 0.2
        if self.growth_scale == GrowthScale.LOG2:
            return math.log2(scale) * 0.2

    def draw(self, scale=1):
        self.foregroundDot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size())
            .set_fill(WHITE)
            .set_z_index(10)
        )

        self.add(self.foregroundDot)

        backgroundDot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size() + 0.1)
            .set_fill(BLACK)
            .set_z_index(0)
        )

        self.add(backgroundDot)

        label = Tex(self.id, color=BLACK).set_x(self.x_coord).set_y(self.y_coord)
        label.set_z_index(20)
        label.scale(self.get_drawn_label_size(scale))
        self.add(label)

    def to_np_array(self):
        return np.array([self.x_coord, self.y_coord, 0])

    def add_to_max_capacity(self, capacity):
        if self.max_capacity < capacity:
            self.max_capacity = capacity

    def add_to_opacity(self, amount):
        self.opacity += amount

    def get_opacity(self, flow):
        return flow / self.opacity

    def get_max_capacity(self):
        return self.max_capacity

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")
