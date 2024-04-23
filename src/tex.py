from manim import *


class TextHelper:
    def __init__(self, scale=2, show_text=True):
        self.scale = scale
        self.show_text = show_text

    def create_and_align_tex(self, text: str, graph):
        if not self.show_text:
            return
        tex = Tex(text, color=BLACK)
        tex.set(font_size=(10 * self.scale))
        tex.align_to(graph, UP).shift(0.95 * UP)

        return tex

    def play_tex_animation_for_path(
        self, ford_fulkerson, graph, path, bottleneck, scene: Scene
    ):
        if not self.show_text:
            return
        scene.play(FadeOut(ford_fulkerson.tex))

        tex_path = ""
        for vertex, edge in path:
            tex_path = (
                tex_path
                + str(edge.get_other_vertex_from_id(vertex).id)
                + " \N{RIGHTWARDS ARROW} "
            )

        # set the sink to be the last vertex in the tex path
        tex_path = f"{tex_path}{graph.sink.id}"
        newTex = self.create_and_align_tex(
            f"Tilføj {int(bottleneck)} enheder strømning til stien {tex_path}", graph
        )

        ford_fulkerson.tex = newTex
        scene.play(FadeIn(ford_fulkerson.tex))
        scene.wait(2, frozen_frame=False)

    def play_tex_animation_for_residual_graph_before(
        self, ford_fulkerson, scene: Scene, graph
    ):
        if not self.show_text:
            return
        scene.play(FadeOut(ford_fulkerson.tex))

        newTex = self.create_and_align_tex(
            "Find en forbedrende sti i restgrafen", graph
        ).set_z_index(28)
        ford_fulkerson.tex = newTex
        scene.play(FadeIn(ford_fulkerson.tex))
        scene.wait(2, frozen_frame=False)

    def play_tex_animation_for_residual_graph_after(
        self, ford_fulkerson, scene: Scene, graph
    ):
        if not self.show_text:
            return
        scene.play(FadeOut(ford_fulkerson.tex))

        newTex = self.create_and_align_tex(
            "En forbedrende sti er fundet", graph
        ).set_z_index(28)
        ford_fulkerson.tex = newTex
        scene.play(FadeIn(ford_fulkerson.tex))
        scene.wait(2, frozen_frame=False)

    def play_initial_tex_animation(self, scene: Scene, graph):
        if not self.show_text:
            return
        tex = self.create_and_align_tex(
            "Givet et strømningsnetværk, find en maksimal strømning i strømningsnetværket.",
            graph,
        )
        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))

    def play_final_tex_animation(self, ford_fulkerson, scene: Scene, graph, max_flow):
        if not self.show_text:
            return
        scene.play(FadeOut(ford_fulkerson.tex))

        tex = self.create_and_align_tex(
            f"Strømningsnetværkets maksimal strømningværdi = {int(max_flow)}",
            graph,
        )

        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))
