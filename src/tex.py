from manim import *


def create_and_align_tex(text: str, graph):
    tex = Tex(text, color=BLACK)
    tex.align_to(graph, graph.get_critical_point(UP)).shift(0.7 * UP)

    if len(text) > 57:
        tex.set(width=config.frame_width - 1)
    else:
        tex.set(font_size=20)
    return tex


def play_tex_animation_for_path(FordFulkerson, graph, path, bottleneck, scene: Scene):
    scene.play(FadeOut(FordFulkerson.tex))
    # set the source to be the first vertex in the tex path
    tex_path = str(graph.source.id)

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

    newTex.align_to(graph, graph.get_critical_point(UL)).shift(0.5 * UP + 0.5 * LEFT)

    FordFulkerson.tex = newTex

    scene.play(FadeIn(FordFulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_tex_animation_for_residual_graph_before(FordFulkerson, scene: Scene, graph):
    scene.play(FadeOut(FordFulkerson.tex))

    newTex = create_and_align_tex(
        "Find en forbedrende sti i restgrafen", graph
    ).set_z_index(28)
    FordFulkerson.tex = newTex
    scene.play(FadeIn(FordFulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_tex_animation_for_residual_graph_after(FordFulkerson, scene: Scene, graph):
    scene.play(FadeOut(FordFulkerson.tex))

    newTex = create_and_align_tex("En forbedrende sti er fundet", graph).set_z_index(28)
    FordFulkerson.tex = newTex
    scene.play(FadeIn(FordFulkerson.tex))
    scene.wait(2, frozen_frame=False)


def play_initial_tex_animation(scene: Scene, graph):
    tex = create_and_align_tex(
        "Givet et strømningsnetværk, find en maksimal strømning i strømningsnetværket.",
        graph,
    )
    scene.play(FadeIn(tex))
    scene.wait(2, frozen_frame=False)
    scene.play(FadeOut(tex))


def play_final_tex_animation(FordFulkerson, scene: Scene, graph, max_flow):
    scene.play(FadeOut(FordFulkerson.tex))

    tex = Tex(
        r"En maksimal strømning i strømningsnetværket er fundet. \\Maksimal strømning = ",
        max_flow,
        color=BLACK,
    )
    tex.align_to(graph, graph.get_critical_point(UP)).shift(0.7 * UP)
    tex.set(font_size=20)

    scene.play(FadeIn(tex))
    scene.wait(2, frozen_frame=False)
    scene.play(FadeOut(tex))
