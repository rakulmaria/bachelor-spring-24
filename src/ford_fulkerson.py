from queue import Queue
from manim import *
from src.tex import TextHelper


class FordFulkerson:
    def __init__(self, graph, scene: Scene, scale=2, show_text=True):
        self.graph = graph
        self.scene = scene
        self.max_flow = 0
        self.path = {}
        self.text_helper = TextHelper(graph, scene, scale, show_text=show_text)

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

    def find_path_DFS(self, source, sink):
        marked_vertices = {}
        self.reverse = True
        return self.DFS_helper(source, sink, marked_vertices)

    def DFS_helper(self, current_vertex, sink, marked_vertices):
        if current_vertex == sink:
            return True

        marked_vertices[current_vertex.id] = True

        sorted_edges = sorted(
            current_vertex.adjacent_edges,
            key=lambda x: x.get_residual_capacity_to(
                x.get_other_vertex(current_vertex)
            ),
            reverse=self.reverse,
        )
        self.reverse = not self.reverse

        for edge in sorted_edges:
            other_vertex = edge.get_other_vertex(current_vertex)

            if edge.get_residual_capacity_to(
                other_vertex
            ) > 0 and not marked_vertices.get(other_vertex.id):
                self.path[other_vertex.id] = edge
                if self.DFS_helper(other_vertex, sink, marked_vertices):
                    return True

        return False

    def find_max_flow(self, BSF=True):
        self.max_flow = 0

        self.text_helper.play_initial_tex_animation()

        if BSF:
            while self.find_path_BFS(self.graph.source, self.graph.sink):
                self.max_flow += self.find_max_helper()
        else:
            while self.find_path_DFS(self.graph.source, self.graph.sink):
                self.max_flow += self.find_max_helper()

        self.text_helper.play_final_tex_animation(int(self.max_flow))

    def find_max_helper(self):
        bottleneck = 9223372036854775807
        current_vertex = self.graph.sink
        path_to_draw = []

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

        self.text_helper.play_tex_animation_for_residual_graph_before()

        self.graph.show_residual_graph(self.scene, path_to_draw, self.text_helper)

        self.text_helper.play_tex_animation_for_path(path_to_draw, bottleneck)

        for vertex, edge in path_to_draw:
            edge.add_current_flow_towards(vertex, bottleneck, self.scene)

        self.path = {}

        return bottleneck
