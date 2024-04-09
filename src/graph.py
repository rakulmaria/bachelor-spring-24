from manim import *
from src.edge import Edge
from src.vertex import Vertex


class FlowGraph(VMobject):
    def __init__(
        self,
        vertices,
        edges,
        capacities,
        layout_scale=2,
        layout="spring",
        layers=[],
        growth_scale="sqrt",
    ):
        super().__init__()

        self.vertices, self.edges = self.getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout_scale, layout, layers
        )

        for vertex in self.vertices:
            self.add(vertex)
            vertex.draw(self.getMinVertexCapacity(self.vertices), growth_scale)

        for edge in self.edges:
            self.add(edge)
            edge.draw(growth_scale)

    def getEdgesAndVerticesAsMobjects(
        self, vertices, edges, capacities, layout_scale=2, layout="spring", layers=[]
    ):
        partitions = self.getPartitions(layers)
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

        verticesAsObjects = {}
        edgesAsObjects = []

        for dot, i in enumerate(graph.vertices):
            x, y, _ = graph._layout[dot]

            vertex = Vertex(i, x, y, 1)
            verticesAsObjects.update({i: vertex})

        for _from, to, capacity in capacities:
            edge = Edge(
                verticesAsObjects.get(_from), verticesAsObjects.get(to), capacity
            )
            edgesAsObjects.append(edge)

        return verticesAsObjects.values(), edgesAsObjects

    def getPartitions(self, layers):
        partitions = []
        c = -1

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i

        return partitions

    def getMaxCapacity(self, capacities):
        return max(capacities, key=lambda x: x[2])[2]

    def getMinVertexCapacity(self, vertices: list[Vertex]):
        return min(vertices, key=lambda x: x.max_capacity).max_capacity
