from manim import *
from src.arrow import EdgeArrow
from src.flow_object import FlowPolygon
import math


class Edge(VMobject):
    def __init__(self, start_vertex, end_vertex, max_capacity, current_flow=0):
        super().__init__()

        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.max_capacity = max_capacity
        self.current_flow = current_flow
        self.flow_object = None

        start_vertex.add_to_max_capacity(max_capacity)
        end_vertex.add_to_max_capacity(max_capacity)

        # also add to the vertex opacity
        # also add opacity to source vertex (has no ingoing edges)
        if self.start_vertex.id == 0:
            start_vertex.add_to_opacity(max_capacity)
        end_vertex.add_to_opacity(max_capacity)

    def add_to_current_flow(self, new_flow, scene):
        if new_flow <= self.max_capacity:
            self.current_flow += new_flow
            new_flow_object = FlowPolygon(self, self.current_flow)
            if self.flow_object is None:
                self.flow_object = FlowPolygon(self, 0)
            scene.play(ReplacementTransform(self.flow_object, new_flow_object))
            self.flow_object = new_flow_object

        else:
            print("Error: New capacity exceeds maximum capacity")

    def get_drawn_edge_size(self, growth_scale="sqrt"):
        if growth_scale == "sqrt":
            return math.sqrt(self.max_capacity) * 8
        if growth_scale == "linear":
            return self.max_capacity * 8
        if growth_scale == "log2":
            return math.log2(self.max_capacity) * 8

    def draw(self, growth_scale="sqrt"):
        backgroundLine = Line(
            start=self.start_vertex.to_np_array(),
            end=self.end_vertex.to_np_array(),
            z_index=0,
            color=BLACK,
            stroke_width=(self.get_drawn_edge_size(growth_scale) + 1.6),
        )
        self.foregroundLine = (
            Line(
                start=self.start_vertex.to_np_array(),
                end=self.end_vertex.to_np_array(),
                z_index=3,
            )
            .set_stroke(width=self.get_drawn_edge_size(growth_scale), color=WHITE)
            .set_fill(color=WHITE)
        )
        self.arrow = EdgeArrow(
            self.start_vertex.to_np_array(), self.end_vertex.to_np_array()
        )

        self.add(backgroundLine)
        self.add(self.foregroundLine)
        self.add(self.arrow)


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
