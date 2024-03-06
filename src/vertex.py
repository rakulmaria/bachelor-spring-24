from manim import *


class Vertex:
    def __init__(self, id, x_coord, y_coord):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.max_capacity = 0
        self.opacity = 0
        self.current_flow = 0

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
