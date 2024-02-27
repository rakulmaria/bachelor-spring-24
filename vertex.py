from manim import *


class Vertex:
    def __init__(self, id, x_coord, y_coord):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord

    def to_np_array(self):
        return np.array([self.x_coord, self.y_coord, 0])