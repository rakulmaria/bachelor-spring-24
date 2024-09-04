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
            layout="partite",
            layers=layers,
            growth_scale=GrowthScale.LINEAR,
            source=source,
            sink=sink,
        )

        self.add(graph)
        ford_fulkerson = FordFulkerson(graph, self)
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
        x_start = -4
        y_start = 1
        x_end = 4
        y_end = -1
        width = 100
        line = Line(
            [x_start, y_start, 0], [x_end, y_end, 0], stroke_width=width, color=BLUE
        )
        orthogonal_vector = np.array([-(y_end - y_start), (x_end - x_start), 0])
        (st, en) = get_offset_points(
            width / 100 / 2, orthogonal_vector, x_start, x_end, y_start, y_end
        )

        (st_1, en_1) = get_offset_points(
            -(width / 100 / 2), orthogonal_vector, x_start, x_end, y_start, y_end
        )

        self.add(line)

        d_start = (
            Dot([x_start, y_start, 0], color=BLUE).scale(width / 14).set_z_index(10)
        )
        self.add(d_start)
        d_end = Dot([x_end, y_end, 0], color=BLUE).scale(width / 14).set_z_index(10)
        self.add(d_end)

        # ---- find point between -----
        ratefunctions = [
            rate_functions.double_smooth,
            rate_functions.linear,
            rate_functions.ease_in_sine,
            rate_functions.ease_out_quad,
            rate_functions.ease_in_quint,
            rate_functions.ease_in_cubic,
            rate_functions.ease_in_out_circ,
        ]
        for i in range(50):
            t = random.uniform(0.05, 0.95)
            x = st_1 + t * (st - st_1)
            t2 = random.uniform(0, 1)
            x2 = en_1 + t2 * (en - en_1)
            path_line = Line(x, x2)

            d1 = Dot().set_color(WHITE).scale(0.5)
            self.add(d1)
            rumtime = random.randint(3, 12)
            ani = MoveAlongPath(
                d1,
                path_line,
                rate_func=ratefunctions[i % len(ratefunctions)],
                run_time=rumtime,
            )
            turn_animation_into_updater(ani, cycle=True)
        self.wait(15)


def get_offset_points(offset, orthogonal_vector, x_start, x_end, y_start, y_end):
    orthogonal_unit_vector = orthogonal_vector / np.linalg.norm(orthogonal_vector)
    scaled_orthogonal_vector = orthogonal_unit_vector * offset
    start_coord = [x_start, y_start, 0] + scaled_orthogonal_vector
    end_coord = [x_end, y_end, 0] + scaled_orthogonal_vector

    return (
        start_coord,
        end_coord,
    )
