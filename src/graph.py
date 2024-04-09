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
        layout_scale=2,
        layout="spring",
        layers=[],
        growth_scale: GrowthScale = GrowthScale.SQRT,
    ):
        super().__init__()
        self.growth_scale = growth_scale

        self.vertices, self.edges = self.getEdgesAndVerticesAsMobjects(
            vertices, edges, capacities, layout_scale, layout, layers
        )

        for vertex in self.vertices:
            self.add(vertex)
            vertex.draw(self.getMinVertexCapacity(self.vertices))

        for edge in self.edges:
            self.add(edge)
            edge.draw()

    def getEdgesAndVerticesAsMobjects(
        self,
        vertices,
        edges,
        capacities,
        layout_scale=2,
        layout="spring",
        layers=[],
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

            vertex = Vertex(i, x, y, growth_scale=self.growth_scale)
            verticesAsObjects.update({i: vertex})

        for _from, to, capacity in capacities:
            edge = Edge(
                verticesAsObjects.get(_from),
                verticesAsObjects.get(to),
                capacity,
                growth_scale=self.growth_scale,
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

    def getMinVertexCapacity(self, vertices: list[Vertex]):
        return min(
            vertices, key=lambda x: x.get_max_drawn_capacity()
        ).get_max_drawn_capacity()

    def addToCurrentFlowTemp(self, flow, path, scene):
        for _, (_from, _to) in enumerate(path):
            for edge in self.edges:
                if edge.start_vertex.id == _from and edge.end_vertex.id == _to:
                    if edge.start_vertex.id == 0:
                        edge.start_vertex.add_to_current_flow(flow, scene)
                    edge.add_to_current_flow(flow, scene)
                    edge.end_vertex.add_to_current_flow(flow, scene)

    # temporary function to test the graph
    def add_to_current_flow_tmp(self, scene: Scene):
        scene.wait(2, frozen_frame=False)
        self.edges[0].add_to_current_flow(3, scene)
        scene.wait(2, frozen_frame=False)
        self.edges[0].add_to_current_flow(7, scene)
        scene.wait(3, frozen_frame=False)
        self.edges[0].add_to_current_flow(-7, scene)
        scene.wait(1, frozen_frame=False)
