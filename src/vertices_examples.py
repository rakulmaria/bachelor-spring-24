class VerticesExamples:
    def sedgewick_wayne():
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5)]
        capacities = [
            (0, 1, 2.0),
            (0, 2, 3.0),
            (1, 3, 3.0),
            (1, 4, 1.0),
            (2, 3, 1.0),
            (2, 4, 1.0),
            (3, 5, 2.0),
            (4, 5, 3.0),
        ]
        source = 0
        sink = 5
        return vertices, edges, capacities, source, sink

    def kleinberg_tardos_small():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 2),
            (0, 2, 1),
            (1, 2, 3),
            (1, 3, 1),
            (2, 3, 2),
        ]
        source = 0
        sink = 3
        return vertices, edges, capacities, source, sink

    def kleinberg_tardos():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 20.0),
            (0, 2, 10.0),
            (1, 2, 30.0),
            (1, 3, 10.0),
            (2, 3, 20.0),
        ]
        source = 0
        sink = 3
        return vertices, edges, capacities, source, sink

    def clrs():
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 5), (4, 3), (4, 5)]
        capacities = [
            (0, 1, 16),
            (0, 2, 13),
            (1, 3, 12),
            (2, 1, 4),
            (2, 4, 14),
            (3, 2, 9),
            (3, 5, 20),
            (4, 3, 7),
            (4, 5, 4),
        ]
        source = 0
        sink = 5

        return vertices, edges, capacities, source, sink

    def jungnickel():
        vertices = [0, 1, 2, 3, 4, 5, 6, 7]
        edges = [
            (3, 5),
            (3, 4),
            (4, 5),
            (2, 3),
            (1, 4),
            (1, 3),
            (0, 2),
            (0, 1),
            (1, 2),
            (4, 7),
            (5, 7),
            (3, 7),
            (6, 7),
            (3, 6),
            (0, 6),
            (4, 2),
        ]
        capacities = [
            (3, 5, 8),
            (3, 4, 20),
            (4, 5, 1),
            (2, 3, 26),
            (1, 4, 13),
            (1, 3, 10),
            (0, 2, 1),
            (0, 1, 38),
            (1, 2, 8),
            (4, 7, 7),
            (5, 7, 7),
            (3, 7, 1),
            (6, 7, 27),
            (3, 6, 24),
            (0, 6, 2),
            (4, 2, 2),
        ]
        source = 0
        sink = 7
        return vertices, edges, capacities, source, sink

    def kleinberg_tardos_extreme():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 200),
            (0, 2, 1),
            (1, 2, 30),
            (1, 3, 100),
            (2, 3, 2),
        ]
        source = 0
        sink = 5
        return vertices, edges, capacities, source, sink

    def simple_graph():
        vertices = [0, 1]
        edges = [(0, 1)]
        capacities = [
            (0, 1, 10),
        ]
        source = 0
        sink = 1
        return vertices, edges, capacities, source, sink

    def bigger_partite_graph():
        vertecies = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
        edges = [
            (9, 0),
            (9, 1),
            (9, 2),
            (0, 3),
            (0, 4),
            (1, 4),
            (1, 5),
            (2, 3),
            (2, 7),
            (3, 6),
            (3, 7),
            (4, 6),
            (4, 8),
            (5, 8),
            (6, 10),
            (7, 10),
            (8, 10),
        ]
        capacities = [
            (9, 0, 7),
            (9, 1, 2),
            (9, 2, 1),
            (0, 3, 2),
            (0, 4, 4),
            (1, 4, 5),
            (1, 5, 6),
            (2, 3, 4),
            (2, 7, 8),
            (3, 6, 7),
            (3, 7, 1),
            (4, 6, 3),
            (4, 8, 3),
            (5, 8, 3),
            (6, 10, 1),
            (7, 10, 3),
            (8, 10, 4),
        ]
        source = 9
        sink = 10
        return vertecies, edges, capacities, source, sink

    def wiki_example():
        verticies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 6),
            (1, 8),
            (2, 6),
            (2, 9),
            (3, 8),
            (4, 10),
            (5, 7),
            (5, 10),
            (6, 11),
            (7, 11),
            (8, 12),
            (9, 13),
            (10, 13),
            (11, 14),
            (12, 14),
            (13, 14),
        ]
        capacities = [
            (0, 1, 1),
            (0, 2, 1),
            (0, 3, 1),
            (0, 4, 1),
            (0, 5, 1),
            (1, 6, 1),
            (1, 8, 1),
            (2, 6, 1),
            (2, 9, 1),
            (3, 8, 1),
            (4, 10, 1),
            (5, 7, 1),
            (5, 10, 1),
            (6, 11, 1),
            (7, 11, 1),
            (8, 12, 1),
            (9, 13, 1),
            (10, 13, 1),
            (11, 14, 3),
            (12, 14, 3),
            (13, 14, 3),
        ]
        source = 0
        sink = 14
        return verticies, edges, capacities, source, sink

    def silkes_big_graph():
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        edges = [
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (2, 7),
            (3, 6),
            (3, 11),
            (8, 3),
            (4, 7),
            (4, 8),
            (5, 9),
            (5, 10),
            (6, 9),
            (6, 10),
            (6, 11),
            (11, 7),
            (7, 12),
            (8, 12),
            (9, 13),
            (10, 13),
            (11, 14),
            (11, 15),
            (12, 15),
            (13, 16),
            (14, 16),
            (15, 16),
        ]
        capacities = [
            (1, 2, 4),
            (1, 3, 3),
            (1, 4, 3),
            (2, 5, 2),
            (2, 7, 3),
            (3, 6, 3),
            (3, 11, 1),
            (8, 3, 1),
            (4, 7, 1),
            (4, 8, 2),
            (5, 9, 3),
            (5, 10, 1),
            (6, 9, 1),
            (6, 10, 1),
            (6, 11, 3),
            (11, 7, 1),
            (7, 12, 3),
            (8, 12, 1),
            (9, 13, 2),
            (10, 13, 3),
            (11, 14, 2),
            (11, 15, 1),
            (12, 15, 4),
            (13, 16, 4),
            (14, 16, 3),
            (15, 16, 4),
        ]
        source = 1
        sink = 16
        return vertices, edges, capacities, source, sink

    def kleinberg_tardos_x_thore():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 8),
            (0, 2, 8),
            (1, 2, 1),
            (1, 3, 8),
            (2, 3, 8),
        ]
        source = 0
        sink = 3
        return vertices, edges, capacities, source, sink
