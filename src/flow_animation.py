from manim import *
from src.edge import Edge
from src.vertex import Vertex
from src.graph_segments import ArrowGraph, BackgroundGraph, FlowGraph, GraphLabel


class NewFlowOpacity(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 30
        self.camera.resize_frame_shape(0)
        self.edges = {}
        self.vertices = {}

        self.add_vertices(
            [
                ["vertex0", -5, 0],
                ["vertex1", 0, 5],
                ["vertex2", 0, -5],
                ["vertex3", 5, 0],
            ]
        )

        self.add_edges(
            [
                ["edge0_to_1", self.vertices["vertex0"], self.vertices["vertex1"], 2],
                ["edge0_to_2", self.vertices["vertex0"], self.vertices["vertex2"], 1],
                ["edge1_to_2", self.vertices["vertex1"], self.vertices["vertex2"], 3],
                ["edge1_to_3", self.vertices["vertex1"], self.vertices["vertex3"], 1],
                ["edge2_to_3", self.vertices["vertex2"], self.vertices["vertex3"], 2],
            ]
        )

        for vertex in self.vertices.values():
            print(vertex.id, vertex.max_capacity)

        backgroundGraph = BackgroundGraph(self.edges.values())
        arrowGraph = ArrowGraph(self.edges.values())
        graphLabel = GraphLabel(self.vertices.values())
        # vertices = DotSegment(self.vertices.values())

        self.add(backgroundGraph)
        self.add_foreground_mobject(arrowGraph)
        # self.add_foreground_mobject(vertices)
        self.add_foreground_mobject(graphLabel)

        # Flow 1
        flow_edges_0_1_2_3 = [
            self.edges["edge0_to_1"],
            self.edges["edge1_to_2"],
            self.edges["edge2_to_3"],
        ]

        flow_1_before = FlowGraph(flow_edges_0_1_2_3, 0)
        flow_1_after = FlowGraph(flow_edges_0_1_2_3, 1)

        self.play(ReplacementTransform(flow_1_before, flow_1_after, run_time=2))
        self.wait(2)

        # Flow 2 is same flow

        flow_2_before = FlowGraph(flow_edges_0_1_2_3, 0)
        flow_2_after = FlowGraph(flow_edges_0_1_2_3, 1)

        self.play(ReplacementTransform(flow_2_before, flow_2_after, run_time=2))
        self.wait(2)

    def add_edges(self, lst):
        for id, start_vertex, end_vertex, max_capacity in lst:
            self.edges[id] = Edge(id, start_vertex, end_vertex, max_capacity)

            # add the max capacity of the edge to the start node and end node
            self.edges[id].start_vertex.add_to_max_capacity(max_capacity)
            self.edges[id].end_vertex.add_to_max_capacity(max_capacity)

            # also add to opacity
            self.edges[id].start_vertex.add_to_opacity(max_capacity)
            self.edges[id].end_vertex.add_to_opacity(max_capacity)

    def add_vertices(self, lst):
        for id, x_coord, y_coord in lst:
            self.vertices[id] = Vertex(id, x_coord, y_coord)
