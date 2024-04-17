from queue import Queue
from manim import *


class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.tex = Tex()
        self.max_flow = 0
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
        self.get_initial_tex_animation(scene)
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

            self.get_path_tex_animation_for_residual_graph_before(scene)

            for vertex, edge in path_to_draw:
                edge.play_arrow_focus_animation_towards(vertex, scene)

            self.get_path_tex_animation_for_residual_graph_after(scene)

            self.get_path_tex_animation_for_primary_graph(
                path_to_draw, bottleneck, scene
            )

            for vertex, edge in path_to_draw:
                edge.add_current_flow_towards(vertex, bottleneck, scene)

            self.max_flow += bottleneck
            self.path = {}
            path_to_draw = []

        self.get_final_tex_animation(scene)

    def get_path_tex_animation_for_primary_graph(self, path, bottleneck, scene: Scene):
        scene.play(FadeOut(self.tex))
        # set the source to be the first vertex in the tex path
        tex_path = str(self.graph.source.id)

        for _, edge in path:
            tex_path = tex_path + "\N{RIGHTWARDS ARROW}" + str(edge.end_vertex.id)

        newTex = Tex(
            "Tilføj ",
            int(bottleneck),
            " enheder strømning til stien ",
            tex_path,
            color=BLACK,
            font_size=20,
        )

        newTex.align_to(self.graph, self.graph.get_critical_point(UL)).shift(
            0.5 * UP + 0.5 * LEFT
        )

        self.tex = newTex

        scene.play(FadeIn(self.tex))
        scene.wait(2, frozen_frame=False)

    def get_path_tex_animation_for_residual_graph_before(self, scene: Scene):
        scene.play(FadeOut(self.tex))

        newTex = Tex(
            "Find en forbedrende sti i restgrafen",
            color=BLACK,
            font_size=20,
        )

        newTex.align_to(self.graph, self.graph.get_critical_point(UL)).shift(
            0.5 * UP + 0.5 * LEFT
        )

        self.tex = newTex

        scene.play(FadeIn(self.tex))
        scene.wait(2, frozen_frame=False)

    def get_path_tex_animation_for_residual_graph_after(self, scene: Scene):
        scene.play(FadeOut(self.tex))

        newTex = Tex(
            "En forbedrende sti er fundet",
            color=BLACK,
            font_size=20,
        )

        newTex.align_to(self.graph, self.graph.get_critical_point(UL)).shift(
            0.5 * UP + 0.5 * LEFT
        )

        self.tex = newTex

        scene.play(FadeIn(self.tex))
        scene.wait(2, frozen_frame=False)

    def get_initial_tex_animation(self, scene: Scene):
        tex = Tex(
            "Givet et strømningsnetværk, find en maksimal strømning i strømningsnetværket.",
            color=BLACK,
            font_size=20,
        )
        tex.align_to(self.graph, self.graph.get_critical_point(UL)).shift(
            0.5 * UP + 0.5 * LEFT
        )

        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))

    def get_final_tex_animation(self, scene: Scene):
        scene.play(FadeOut(self.tex))

        tex = Tex(
            r"En maksimal strømning i strømningsnetværket er fundet. \\ Maksimal strømning = ",
            str(self.max_flow),
            color=BLACK,
            font_size=20,
        )
        tex.align_to(self.graph, self.graph.get_critical_point(UL)).shift(
            0.5 * UP + 0.5 * LEFT
        )
        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))
