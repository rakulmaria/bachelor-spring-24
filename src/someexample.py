from manim import *
from random import *


def calculate_random_points(p1, p2):
    t = uniform(0.0, 1.0)

    x = p1[0] + t * (p2[0] - p1[0])
    y = p1[1] + t * (p2[1] - p1[1])

    return (x, y)


# print(calculate_random_points((2,3),(8,7)))
def random_rate_functions():
    for rate_function in rate_functions:
        print(rate_function)


# class SomeExample(Scene):
#     def construct(self):
#         func = lambda pos: pos[0] * LEFT pos[1] * RIGHT
#         stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
#         self.add(stream_lines)
#         stream_lines.start_animation(warm_up=False, flow_speed=1.5)
#         self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
