class VerticesExamples:
    def SedgewickWayne():
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
        return vertices, edges, capacities

    def KleinbergTardosSmall():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 2),
            (0, 2, 1),
            (1, 2, 3),
            (1, 3, 1),
            (2, 3, 2),
        ]
        return vertices, edges, capacities

    def KleinbergTardos():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 20.0),
            (0, 2, 10.0),
            (1, 2, 30.0),
            (1, 3, 10.0),
            (2, 3, 20.0),
        ]
        return vertices, edges, capacities

    def CLRS():
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

        return vertices, edges, capacities

    def Jungnickel():
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
        return vertices, edges, capacities

    def KleinbergTardosExtreme():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        capacities = [
            (0, 1, 200),
            (0, 2, 1),
            (1, 2, 30),
            (1, 3, 100),
            (2, 3, 2),
        ]
        return vertices, edges, capacities

    def SimpleGraph():
        vertices = [0, 1]
        edges = [(0, 1)]
        capacities = [
            (0, 1, 10),
        ]
        return vertices, edges, capacities
