from manim import *
from src.edge import Edge
from src.vertex import Vertex
from src.utils import *


class FlowNetwork(VMobject):
    def __init__(
        self,
        vertices,
        edges,
        capacities,
        source,
        sink,
        scene: Scene = None,
        layout_scale=2,
        layout="spring",
        layers=[],
        growth_scale: GrowthScale = GrowthScale.SQRT,
        theme: Themes = Themes.Light,
    ):
        self.theme = theme
        self.scene = scene
        self.scene.camera.background_color = theme.get("FRAME-BACKGROUND")
        super().__init__()
        self.growth_scale = growth_scale

        self.primitive_verticies = vertices
        self.primitive_edges = edges

        graph = self.get_graph_for_layout(vertices, edges, layout_scale, layout, layers)
        self.vertices, self.edges = self.initialize_vertices_and_edges(
            vertices, edges, source, sink, capacities, graph
        )

        self.draw_vertices_and_edges()

    def draw_vertices_and_edges(self):
        # vertex has in and outgoing capacity here
        for vertex in self.vertices:
            self.add(vertex)
            vertex.draw(self.get_min_vertex_capacity(self.vertices))

        for edge in self.edges:
            self.add(edge)
            edge.draw()

    def initialize_vertices_and_edges(
        self, vertices, edges, source, sink, capacities, graph
    ):
        vertices = self.initialize_vertices(graph, source, sink)
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
                scene=self.scene,
                theme=self.theme,
            )
            edges_as_objects.append(edge)

        return edges_as_objects

    def initialize_vertices(self, graph, source, sink):
        vertices_as_objects = {}

        for _, id in enumerate(graph.vertices):
            x, y, _ = graph._layout[id]

            vertex = Vertex(id, x, y, self.growth_scale, self.theme)
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

    def show_residual_graph(self, scene: Scene, path_to_draw, text_helper):
        blur = Rectangle(
            width=200,
            height=200,
            fill_opacity=0.9,
            fill_color=WHITE,
        ).set_z_index(20)
        scene.play(FadeIn(blur))

        edge_config = {
            "stroke_width": 2,
            "tip_config": {
                "tip_length": 0.20,
                "tip_width": 0.18,
            },
            "color": GREY,
        }

        di_graph = (
            DiGraph(
                self.primitive_verticies,
                self.get_active_edges(),
                edge_config=edge_config,
                layout=self.get_layout_dict(),
            )
            .set_z_index(24)
            .set_color(GREY)
        )
        scene.play(FadeIn(di_graph))
        scene.wait(1.5, frozen_frame=False)

        shown_path = self.highlight_path_in_residual_graph(
            scene, path_to_draw, di_graph
        )

        text_helper.play_tex_animation_for_residual_graph_after()

        scene.play(Uncreate(VGroup(di_graph, shown_path)))
        scene.play(FadeOut(blur))

    def highlight_path_in_residual_graph(self, scene, path, di_graph):
        group = VGroup()
        for vertex, edge in path:
            old_edge = di_graph._remove_edge(
                (
                    edge.get_other_vertex_from_id(vertex).id,
                    edge.get_vertex_from_id(vertex).id,
                )
            )
            line = (
                Line(
                    old_edge.get_start(),
                    old_edge.get_end(),
                )
                .add_tip(
                    tip_length=0.20, tip_width=0.18, tip_shape=ArrowTriangleFilledTip
                )
                .set_color(BLACK)
                .set_z_index(26)
            )
            scene.play(Create(line))
            group.add(line)
        return group


# fjern flow-objekt og lav en linje i stedet for
#   evt. med start fra venstre til højre første gang (vokser diagonalt).
#   ellers vokser horisontalt

# find ud af, hvordan hele path'en skal hænge sammen mellem hver edge
#   hvordan får vi en path, som prikkerne kan følge, fra source til sink
#   og hvor skal dens logik høre hjemme

# prikker skal slettes undervejs og hvordan
# kan vi finde ud af til hvilke kanter prikker skal tilføjes, hvis de ikke er en del af path'en
