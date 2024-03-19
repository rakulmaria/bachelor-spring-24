class VerticesExamples:
    def SedgewickWayne():
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 5), (4, 5)]
        return vertices, edges

    def KleinbergTardos():
        vertices = [0, 1, 2, 3]
        edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
        return vertices, edges

    def CLRS():
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 5), (4, 3), (4, 5)]
        return vertices, edges

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
        return vertices, edges
