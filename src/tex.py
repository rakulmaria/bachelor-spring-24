from manim import *


def create_and_align_tex(text: str, graph):
    tex = Tex(text, color=BLACK)
    if len(text) > 57:
        tex.set(width=config.frame_width - 1)
    else:
        tex.set(font_size=20)
    tex.align_to(graph, graph.get_critical_point(UP)).shift(0.7 * UP)

    return tex


def play_tex_animation_for_path(ford_fulkerson, graph, path, bottleneck, scene: Scene):
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
    newTex = create_and_align_tex(
        f"Tilføj {int(bottleneck)} enheder strømning til stien {tex_path}", graph
    )

    ford_fulkerson.tex = newTex
    scene.play(FadeIn(ford_fulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_tex_animation_for_residual_graph_before(ford_fulkerson, scene: Scene, graph):
    scene.play(FadeOut(ford_fulkerson.tex))

    newTex = create_and_align_tex(
        "Find en forbedrende sti i restgrafen", graph
    ).set_z_index(28)
    ford_fulkerson.tex = newTex
    scene.play(FadeIn(ford_fulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_tex_animation_for_residual_graph_after(ford_fulkerson, scene: Scene, graph):
    scene.play(FadeOut(ford_fulkerson.tex))

    newTex = create_and_align_tex("En forbedrende sti er fundet", graph).set_z_index(28)
    ford_fulkerson.tex = newTex
    scene.play(FadeIn(ford_fulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_initial_tex_animation(scene: Scene, graph):
    tex = create_and_align_tex(
        "Givet et strømningsnetværk, find en maksimal strømning i strømningsnetværket.",
        graph,
    )
    scene.play(FadeIn(tex))
    scene.wait(2, frozen_frame=False)
    scene.play(FadeOut(tex))


def play_final_tex_animation(ford_fulkerson, scene: Scene, graph, max_flow):
    scene.play(FadeOut(ford_fulkerson.tex))

    tex = Tex(
        r"En maksimal strømning i strømningsnetværket er fundet. \\Maksimal strømning = ",
        max_flow,
        color=BLACK,
    )
    tex.set(font_size=20)
    tex.align_to(graph, graph.get_critical_point(UP)).shift(0.7 * UP)

    scene.play(FadeIn(tex))
    scene.wait(2, frozen_frame=False)
    scene.play(FadeOut(tex))
