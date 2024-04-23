from manim import *
from src.edge import Edge
from src.vertex import Vertex
from src.utils import GrowthScale


class FlowNetwork(VMobject):
    def __init__(
        self,
        vertices,
        edges,
        capacities,
        source,
        sink,
        layout_scale=2,
        layout="spring",
        layers=[],
        growth_scale: GrowthScale = GrowthScale.SQRT,
    ):
        super().__init__()
        self.growth_scale = growth_scale

        self.primitive_verticies = vertices
        self.primitive_edges = edges

        graph = self.get_graph_for_layout(vertices, edges, layout_scale, layout, layers)
        self.vertices, self.edges = self.initialize_edges_and_verticies(
            vertices, edges, source, sink, capacities, graph
        )

        self.draw_vertices_and_edges()

    def draw_vertices_and_edges(self):
        for vertex in self.vertices:
            self.add(vertex)
            vertex.draw(self.get_min_vertex_capacity(self.vertices))

        for edge in self.edges:
            self.add(edge)
            edge.draw()

    def initialize_edges_and_verticies(
        self, vertices, edges, source, sink, capacities, graph
    ):
        vertices = self.initialize_vertecies(graph, source, sink)
        edges = self.initialize_edges(vertices, capacities)

        return vertices.values(), edges

    def initialize_edges(self, vertices_as_objects, capacities):
        edges_as_objects = []

        for _from, to, capacity in capacities:
            edge = Edge(
                vertices_as_objects.get(_from),
                vertices_as_objects.get(to),
                capacity,
                growth_scale=self.growth_scale,
            )
            edges_as_objects.append(edge)

        return edges_as_objects

    def initialize_vertecies(self, graph, source, sink):
        vertices_as_objects = {}

        for _, id in enumerate(graph.vertices):
            x, y, _ = graph._layout[id]

            vertex = Vertex(id, x, y, self.growth_scale)
            if vertex.id == source:
                self.source = vertex
                vertex.set_source()
            if vertex.id == sink:
                self.sink = vertex
                vertex.set_sink()

            vertices_as_objects.update({id: vertex})

        return vertices_as_objects

    def get_graph_for_layout(self, vertices, edges, layout_scale, layout, layers):
        partitions = self.get_partitions(layers)
        if partitions != []:
            return Graph(
                vertices,
                edges,
                layout_scale=layout_scale,
                layout="partite",
                partitions=partitions,
            )
        else:
            return Graph(
                vertices,
                edges,
                layout_scale=layout_scale,
                layout=layout,
                layout_config={"seed": 100},
            )

    # helper method, if you want to create a partite graph and use layers to display it
    def get_partitions(self, layers):
        partitions = []
        c = -1

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i

        return partitions

    def get_min_vertex_capacity(self, vertices):
        return min(
            vertices, key=lambda x: x.get_max_drawn_capacity()
        ).get_max_drawn_capacity()

    def get_layout_dict(self):
        layout_dict = {}

        for vertex in self.vertices:
            layout_dict[vertex.id] = vertex.to_np_array()

        return layout_dict

    def get_active_edges(self):
        active_edges = []

        for edge in self.edges:
            active_edges.extend(edge.get_active_edges())

        return active_edges
