from manim import *
from src.graph import FlowGraph
from src.auto_layout_graph import getEdgesAndVerticesAsMobjects
from src.vertices_examples import VerticesExamples as V
import math


class Test(Scene):
    def construct(self):
        vertices, edges, capacities = V.SedgewickWayne()
        lt = {
            0: [-2, 0, 0],
            1: [-1, 1, 0],
            2: [-1, -1, 0],
            3: [1, 1, 0],
            4: [1, -1, 0],
            5: [2, 0, 0],
        }

        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout=lt
        )
        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE

        self.add(graph)


class Test2(Scene):
    def construct(self):
        vertices, edges, capacities = V.SimpleGraph()

        lt = {
            0: [-2, 0, 0],
            1: [2, 0, 0],
        }
        vertices, edges = getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout=lt
        )

        graph = FlowGraph(vertices, edges)
        self.camera.background_color = WHITE

        self.add(graph)
        cap = 3

        (a, b) = get_flow_coords(edges[0], cap)
        print(a, "a")
        print(b, "b")
        e = (
            Line(
                a,
                b,
                z_index=4,
            )
            .set_stroke(width=(math.sqrt(cap) * 8), color=BLUE)
            .set_fill(color=BLUE)
        )

        self.add(e)


def get_flow_coords(edge, cap):
    x_start = edge.start_vertex.x_coord
    y_start = edge.start_vertex.y_coord
    x_end = edge.end_vertex.x_coord
    y_end = edge.end_vertex.y_coord
    h_top = (edge.foregroundLine.stroke_width / 100) / 2
    h = (h_top - get_line_width(cap)) / 4
    print(get_line_width(cap), "cap")
    print(h_top, "htop")
    print(h, "h")

    v1 = x_end - x_start
    v2 = y_end - y_start
    z1 = -v2
    z2 = v1

    x_start_final = x_start + h * z1
    y_start_final = y_start + h * z2

    x_end_final = x_end + h * z1
    y_end_final = y_end + h * z2

    return (
        np.array([x_start_final, y_start_final, 0]),
        np.array([x_end_final, y_end_final, 0]),
    )


def get_line_width(cap):
    line = Line().set_stroke(width=(math.sqrt(cap) * 8))
    width = line.stroke_width
    print(width, "real width")
    return width / 100 / 2
