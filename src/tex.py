from manim import *


class _Tex:
    def create_and_align_tex(self, text: str):
        tex = Tex(text, color=BLACK)
        tex.align_to(self.graph, self.graph.get_critical_point(UP)).shift(0.8 * UP)

        if len(text) > 57:
            tex.set(width=config.frame_width - 1)
        else:
            tex.set(font_size=20)
        return tex

    def play_tex_animation_for_residual_graph_before(self, scene: Scene):
        scene.play(FadeOut(self.tex))

        newTex = self.create_and_align_tex(
            "Find en forbedrende sti i restgrafen"
        ).set_z_index(28)
        self.tex = newTex
        scene.play(FadeIn(self.tex))
        scene.wait(2, frozen_frame=False)

    def play_tex_animation_for_residual_graph_after(self, scene: Scene):
        scene.play(FadeOut(self.tex))

        newTex = self.create_and_align_tex("En forbedrende sti er fundet").set_z_index(
            28
        )
        self.tex = newTex
        scene.play(FadeIn(self.tex))
        scene.wait(2, frozen_frame=False)

    def play_initial_tex_animation(self, scene: Scene):
        tex = self.create_and_align_tex(
            "Givet et strømningsnetværk, find en maksimal strømning i strømningsnetværket."
        )
        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))

    def play_final_tex_animation(self, scene: Scene, max_flow):
        scene.play(FadeOut(self.tex))

        tex = Tex(
            r"En maksimal strømning i strømningsnetværket er fundet. \\Maksimal strømning = ",
            max_flow,
            color=BLACK,
        )
        tex.align_to(self.graph, self.graph.get_critical_point(UP)).shift(0.8 * UP)
        tex.set(font_size=20)

        scene.play(FadeIn(tex))
        scene.wait(2, frozen_frame=False)
        scene.play(FadeOut(tex))
