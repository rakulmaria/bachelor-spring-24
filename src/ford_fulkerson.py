from queue import Queue
from manim import *


class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.tex = Tex()
        self.max_flow = 0
        self.path = {}

    def show_primitive_graph(self, scene: Scene, path_to_draw):
        blur = Rectangle(
            width=200,
            height=200,
            fill_opacity=0.9,
            fill_color=WHITE,
            z_index=100,
        )
        scene.play(FadeIn(blur))

        edge_config = {
            "stroke_width": 2,
            "tip_config": {
                "tip_shape": StealthTip,
                "tip_length": 0.15,
            },
            "color": GREY,
        }

        di_graph = (
            DiGraph(
                self.graph.primitive_verticies,
                self.graph.get_active_edges(),
                edge_config=edge_config,
                layout=self.graph.get_layout_dict(),
            )
            .set_z_index(101)
            .set_color(GREY)
        )
        scene.play(FadeIn(di_graph))
        shown_path = self.highlight_path(scene, path_to_draw, di_graph)
        scene.play(Uncreate(VGroup(di_graph, shown_path)))

        scene.play(FadeOut(blur))

    def highlight_path(self, scene, path, di_graph):
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
                .add_tip(tip_length=0.15, tip=StealthTip())
                .set_color(BLACK)
                .set_z_index(102)
            )
            scene.play(Create(line))
            group.add(line)
        return group

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
        stack = []

        marked_vertices[source.id] = True
        stack.append(source)

        while len(stack) > 0 and not marked_vertices.get(sink.id):
            current_vertex = stack.pop()

            for edge in current_vertex.adjacent_edges:
                other_vertex = edge.get_other_vertex(current_vertex)

                if edge.get_residual_capacity_to(
                    other_vertex
                ) > 0 and not marked_vertices.get(other_vertex.id):
                    self.path[other_vertex.id] = edge
                    marked_vertices[other_vertex.id] = True
                    stack.append(other_vertex)

        return marked_vertices.get(sink.id)

    def find_max_flow(self, scene: Scene, BSF=True):
        self.max_flow = 0

        self.play_initial_tex_animation(scene)

        if BSF:
            while self.find_path_BFS(self.graph.source, self.graph.sink):
                self.max_flow += self.find_max_helper(scene)
        else:
            while self.find_path_DFS(self.graph.source, self.graph.sink):
                self.max_flow += self.find_max_helper(scene)

        self.play_final_tex_animation(scene)

        return self.max_flow

    def find_max_helper(self, scene):
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

        self.play_tex_animation_for_residual_graph_before(scene)

        self.show_primitive_graph(scene, path_to_draw)

        self.play_tex_animation_for_residual_graph_after(scene)

        self.play_tex_animation_for_path(path_to_draw, bottleneck, scene)

        for vertex, edge in path_to_draw:
            edge.add_current_flow_towards(vertex, bottleneck, scene)

        self.path = {}

        return bottleneck

    def play_tex_animation_for_path(self, path, bottleneck, scene: Scene):
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

    def play_tex_animation_for_residual_graph_before(self, scene: Scene):
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

    def play_tex_animation_for_residual_graph_after(self, scene: Scene):
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

    def play_initial_tex_animation(self, scene: Scene):
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

    def play_final_tex_animation(self, scene: Scene):
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
