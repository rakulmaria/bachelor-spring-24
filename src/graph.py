from manim import *
from src.edge import Edge
from src.vertex import Vertex
from src.utils import GrowthScale


class FlowGraph(VMobject):
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

        self.vertices, self.edges = self.get_edges_and_vertices_as_mobjects(
            vertices, edges, source, sink, capacities, layout_scale, layout, layers
        )

        for vertex in self.vertices:
            self.add(vertex)
            vertex.draw(self.get_min_vertex_capacity(self.vertices))

        for edge in self.edges:
            self.add(edge)
            edge.draw()

    def get_edges_and_vertices_as_mobjects(
        self,
        vertices,
        edges,
        source,
        sink,
        capacities,
        layout_scale=2,
        layout="spring",
        layers=[],
    ):
        partitions = self.get_partitions(layers)
        graph = []
        if partitions != []:
            graph = Graph(
                vertices,
                edges,
                layout_scale=layout_scale,
                layout="partite",
                partitions=partitions,
            )
        else:
            graph = Graph(
                vertices,
                edges,
                layout_scale=layout_scale,
                layout=layout,
                layout_config={"seed": 100},
            )

        vertices_as_objects = {}
        edges_as_objects = []

        for dot, id in enumerate(graph.vertices):
            x, y, _ = graph._layout[dot]

            vertex = Vertex(id, x, y, self.growth_scale)
            if vertex.id == source:
                self.source = vertex
            if vertex.id == sink:
                self.sink = vertex

            vertices_as_objects.update({id: vertex})

        for _from, to, capacity in capacities:
            edge = Edge(
                vertices_as_objects.get(_from),
                vertices_as_objects.get(to),
                capacity,
                growth_scale=self.growth_scale,
            )
            edges_as_objects.append(edge)

        return vertices_as_objects.values(), edges_as_objects

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
