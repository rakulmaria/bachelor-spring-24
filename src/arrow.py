from manim import *
from numpy import ndarray
from src.utils import Themes


class EdgeArrow(Arrow):
    def __init__(self, p1: ndarray, p2: ndarray, theme: Themes):
        midpoint = (p1 + p2) / 2
        fixed_length = 1.5
        direction_vector = normalize(p2 - p1)
        start_point = midpoint - fixed_length / 2 * direction_vector
        end_point = midpoint + fixed_length / 2 * direction_vector

        super().__init__(start_point, end_point, tip_length=0.08)
        super().set_fill(color=theme.get("ARROW"))
        super().set_stroke(color=theme.get("ARROW"))
        super().scale(0.5)

        super().set_z_index(20)
