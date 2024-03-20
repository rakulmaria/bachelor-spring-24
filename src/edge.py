from manim import *
from src.arrow import EdgeArrow


class Edge(Line):
    def __init__(
        self, start_vertex, end_vertex, max_capacity, current_flow=0, **kwargs
    ):
        super().__init__(
            start=start_vertex.to_np_array(),
            end=end_vertex.to_np_array(),
            z_index=0,
            color=BLACK,
            stroke_width=((max_capacity + 0.2) * 16),
        )

        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow

        # add the max capacity of the edge to the start node and end node
        start_vertex.add_to_max_capacity(max_capacity)
        end_vertex.add_to_max_capacity(max_capacity)

        # also add to opacity
        # start_vertex.add_to_opacity(max_capacity)
        # end_vertex.add_to_opacity(max_capacity)

        forgroundLine = (
            Line(
                start=start_vertex.to_np_array(),
                end=end_vertex.to_np_array(),
                z_index=3,
            )
            .set_stroke(width=(max_capacity * 16), color=WHITE)
            .set_fill(color=WHITE)
        )

        self.add(forgroundLine)

        arrow = EdgeArrow(start_vertex.to_np_array(), end_vertex.to_np_array())
        self.add(arrow)

    def add_to_current_flow(self, new_flow):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
        else:
            print("Error: New capacity exceeds maximum capacity")


"""
class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        v1 = Vertex("vertex0", -4, 0, 5)

        v2 = Vertex("vertex1", 4, 2, 4)
        e = Edge("vertex0", v1, v2, 4)
        self.add(v1)
        self.add(v2)
        self.add(e)
        self.wait(1)
 """
