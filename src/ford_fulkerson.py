from queue import Queue
from manim import *
from src.graph import FlowGraph


class FordFulkerson:
    def __init__(self, graph: FlowGraph):
        self.graph = graph
        self.path = {}

    def find_path_BFS(self, source, sink):
        marked_vertices = {}
        queue = Queue(maxsize=len(self.graph.vertices))

        marked_vertices[source.id] = True
        queue.put(source)

        while not queue.empty() and not marked_vertices.get(sink.id):
            current_vertex = queue.get()

            for edge in current_vertex.adjacent_edges:
                other_vertex = edge.get_other_vertex(current_vertex)

                if edge.get_residual_capacity_to(
                    other_vertex
                ) > 0 and not marked_vertices.get(other_vertex.id):
                    self.path[other_vertex.id] = edge
                    marked_vertices[other_vertex.id] = True
                    queue.put(other_vertex)

        return marked_vertices.get(sink.id)

    def find_max_flow(self, scene: Scene):
        maxflow = 0
        path_to_draw = []

        while self.find_path_BFS(self.graph.source, self.graph.sink):
            bottleneck = 9223372036854775807
            current_vertex = self.graph.sink

            while current_vertex.id is not self.graph.source.id:
                bottleneck = min(
                    bottleneck,
                    self.path.get(current_vertex.id).get_residual_capacity_to(
                        current_vertex
                    ),
                )
                current_vertex = self.path.get(current_vertex.id).get_other_vertex(
                    current_vertex
                )

            current_vertex = self.graph.sink

            while current_vertex.id is not self.graph.source.id:
                path_to_draw.insert(
                    0, (current_vertex.id, self.path.get(current_vertex.id))
                )  # insert the edge in the beginning of the list
                current_vertex = self.path.get(current_vertex.id).get_other_vertex(
                    current_vertex
                )

            for vertex, edge in path_to_draw:
                edge.add_current_flow_towards(vertex, bottleneck, scene)

            maxflow += bottleneck
            self.path = {}
            path_to_draw = []

        return maxflow
