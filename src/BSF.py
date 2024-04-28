from queue import Queue
from src.path_finder import PathFinder


class BSF(PathFinder):
    def find_path(self, source, sink, graph_length):
        marked_vertices = {}
        queue = Queue(maxsize=graph_length)
        path = {}

        marked_vertices[source.id] = True
        queue.put(source)

        while not queue.empty() and not marked_vertices.get(sink.id):
            current_vertex = queue.get()

            for edge in current_vertex.adjacent_edges:
                other_vertex = edge.get_other_vertex(current_vertex)

                if edge.get_residual_capacity_to(
                    other_vertex
                ) > 0 and not marked_vertices.get(other_vertex.id):
                    path[other_vertex.id] = edge
                    marked_vertices[other_vertex.id] = True
                    queue.put(other_vertex)

        if marked_vertices.get(sink.id):
            return path
        else:
            return None
