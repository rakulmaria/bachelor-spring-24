from src.path_finder import PathFinder


class DFS(PathFinder):
    def find_path(self, source, sink, graph_length=0):
        marked_vertices = {}
        self.reverse = True
        path = {}
        return self.DFS_helper(source, sink, marked_vertices, path)

    def DFS_helper(self, current_vertex, sink, marked_vertices, path):
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
                path[other_vertex.id] = edge
                if self.DFS_helper(other_vertex, sink, marked_vertices, path):
                    return path

        return None
