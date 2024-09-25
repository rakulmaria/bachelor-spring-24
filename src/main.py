from manim import *
from src.DFS import DFS
from src.ford_fulkerson import FordFulkerson
from src.flow_network import FlowNetwork
from src.vertices_examples import VerticesExamples as V
from src.utils import GrowthScale
import random


class SedgewickWayne(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()
        layers = [1, 2, 2, 1]

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            scene=self,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
        )

        self.add(graph)
        ford_fulkerson = FordFulkerson(
            graph,
            self,
            show_text=False,
        )
        ford_fulkerson.find_max_flow()


class WikiExample(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.wiki_example()
        layers = [1, 5, 5, 3, 1]
        scale = 3

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
        )

        self.camera.frame_width = 4.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph, self, scale)
        ford_fulkerson.find_max_flow()


class BigGraph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.silkes_big_graph()
        lt = {
            1: [-5, 0, 0],
            2: [-3, 2, 0],
            3: [-3, 0, 0],
            4: [-3, -2, 0],
            5: [-1, 3, 0],
            6: [-1, 1, 0],
            7: [-1, -1, 0],
            8: [-1, -3, 0],
            9: [1, 3, 0],
            10: [1, 1, 0],
            11: [1, -1, 0],
            12: [1, -3, 0],
            13: [3, 2, 0],
            14: [3, 0, 0],
            15: [3, -2, 0],
            16: [5, 0, 0],
        }
        scale = 5

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout=lt,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
        )

        self.camera.frame_width = scale * 3.5
        self.camera.resize_frame_shape(0)
        self.add(graph)

        ford_fulkerson = FordFulkerson(graph, self, scale, show_text=False)
        ford_fulkerson.find_max_flow()


class ThoresExampleDFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()
        layers = [1, 2, 1]
        scale = 4

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
        )

        self.camera.frame_width = 3.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self, scale, path_finder=DFS())
        ford_fulkerson.find_max_flow()


class ThoresExampleBFS(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.kleinberg_tardos_x_thore()
        layers = [1, 2, 1]
        scale = 4

        graph = FlowNetwork(
            vertices,
            edges,
            capacities,
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
            layout_scale=scale,
        )

        self.camera.frame_width = 3.5 * scale
        self.camera.resize_frame_shape(0)
        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self, scale=scale)
        ford_fulkerson.find_max_flow()


class Bacteria(Dot):
    def __init__(self, point=ORIGIN, **kwargs):
        Dot.__init__(self, point=point, color=GREEN, **kwargs)
        self.velocity = 6 * np.random.random_sample(3) - 3  # [-3, 3] interval


class Ex(Scene):
    def construct(self):
        x_start = -3
        y_start = 0
        x_end = 0
        y_end = 0
        width = 100
        flow_width = 70

        (e2_st, e2_en, e2_st_1, e2_en_1) = self.create_edge(x_end, y_end, 3, 2, 30, 30)

        (e1_st, e1_en, e1_st_1, e1_en_1) = self.create_edge(x_end, y_end, 4, -3, 80, 40)

        (st, en, st_1, en_1) = self.create_edge(
            x_start, y_start, x_end, y_end, width, flow_width
        )

        ratefunctions = [
            rate_functions.double_smooth,
            rate_functions.linear,
            rate_functions.ease_in_sine,
            rate_functions.ease_out_quad,
            rate_functions.ease_in_quint,
            rate_functions.ease_in_cubic,
            rate_functions.ease_in_out_circ,
        ]

        color_list = color_gradient(
            [AS2700.B32_POWDER_BLUE, AS2700.B22_HOMEBUSH_BLUE], 6
        )

        for i in range(flow_width):
            (p1, p2, p3, p4) = (st, en, st_1, en_1)
            if i < 30:
                (p1, p2, p3, p4) = (e2_st, e2_en, e2_st_1, e2_en_1)
            else:
                (p1, p2, p3, p4) = (e1_st, e1_en, e1_st_1, e1_en_1)

            x, x2 = self.find_points_between(st, en, st_1, en_1)
            x3, x4 = self.find_points_between(p1, p2, p3, p4)

            mob = VMobject(stroke_width=4, color=GREEN).set_points_as_corners(
                [
                    x,
                    x2,
                    x3,
                    x4,
                ]
            )

            d1 = (
                Dot()
                .set_color(ManimColor.from_hex(random.choice(color_list)))
                .scale(0.5)
            ).set_z_index(2)
            self.add(d1)

            ani = MoveAlongPath(
                d1,
                mob,
                rate_func=ratefunctions[i % len(ratefunctions)],
                run_time=random.randint(3, 12),
            )

            turn_animation_into_updater(ani, cycle=True)
        self.wait(15)

    def find_points_between(self, st, en, st_1, en_1):
        x = st_1 + random.uniform(0.1, 0.9) * (st - st_1)
        x2 = en_1 + random.uniform(0.1, 0.9) * (en - en_1)

        return x, x2

    def create_edge(self, x_start, y_start, x_end, y_end, width, flow_width):
        start = [x_start, y_start, 0]
        end = [x_end, y_end, 0]
        baseline = Line(
            start,
            end,
            stroke_width=width,
            color=WHITE,
        ).set_z_index(-1)

        orthogonal_vector = np.array([-(y_end - y_start), (x_end - x_start), 0])

        line = Line(
            start,
            end,
            stroke_width=flow_width,
            color=AS2700.B21_ULTRAMARINE,
        ).set_z_index(1)

        b_dot = (
            Dot(
                start,
                color=AS2700.B21_ULTRAMARINE,
            )
            .scale(flow_width / 16)
            .set_z_index(1)
        )

        b_dot_2 = (
            Dot(
                end,
                color=AS2700.B21_ULTRAMARINE,
            )
            .scale(flow_width / 16)
            .set_z_index(1)
        )

        self.add(line, b_dot, b_dot_2)

        d_start = Dot(start, color=WHITE).scale(width / 12).set_z_index(0)
        self.add(d_start)
        d_end = Dot(end, color=WHITE).scale(width / 12).set_z_index(0)
        self.add(d_end)

        d_back = Dot(start, color=BLACK).scale(width / 11.9).set_z_index(-4)
        self.add(d_back)
        d_end_back = Dot(end, color=BLACK).scale(width / 11.9).set_z_index(-4)
        self.add(d_end_back)

        self.add(baseline)

        stroke = Line(
            start,
            end,
            stroke_width=width * 1.01,
            color=BLACK,
        ).set_z_index(-2)

        self.add(stroke)

        (st, en) = get_offset_points(
            (flow_width) / 100 / 2,
            orthogonal_vector,
            start[0],
            end[0],
            start[1],
            end[1],
        )

        (st_1, en_1) = get_offset_points(
            -((flow_width) / 100 / 2),
            orthogonal_vector,
            start[0],
            end[0],
            start[1],
            end[1],
        )

        return (st, en, st_1, en_1)


def get_offset_points(offset, orthogonal_vector, x_start, x_end, y_start, y_end):
    orthogonal_unit_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector)
    scaled_orthogonal_vector = orthogonal_unit_vector * offset
    start_coord = [x_start, y_start, 0] + scaled_orthogonal_vector
    end_coord = [x_end, y_end, 0] + scaled_orthogonal_vector

    return (
        start_coord,
        end_coord,
    )


class Ex2(Scene):
    def construct(self):
        p1 = [-1, -1, 0]
        p2 = [-1, 1, 0]
        line = Line(p1, p2, color=BLUE_A)
        dot = Dot(color=ORANGE).set_z_index(2)
        self.add(dot, line)
        a = turn_animation_into_updater(
            MoveAlongPath(
                dot,
                line,
            ),
            cycle=True,
        )
        self.wait(3)
        self.remove(a)
        self.wait(2)
        self.add(a)
        self.wait(2)
        self.remove(a)
        self.wait(2)


# knuder muligvis alle samme størrelse
# og ingen farve, sådan at man kan se hvordan
# strømningsprikkerne fordeler sig i hver knude
#
# strømning i midten af kanterne
#   eller muligvis stadig i siden ?
#
# ingen røde pile for restgrafen
# restgrafen simpel ligesom italienske kvinde
#
# lad Inge være med til næste møde, muligvis online
#
# thore: jeg vil se med strømning inde i midten af knude
#        og på en hel graf!
