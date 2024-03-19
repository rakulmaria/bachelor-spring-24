from manim import *
from src.graph_segments import GraphSegment


class Test_Segment(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        graphSegment = GraphSegment(np.array([0, 1, 0]), np.array([5, 1, 0]), 5, WHITE)
        backGroundGraphSegment = GraphSegment(
            np.array([0, 1, 0]), np.array([5, 1, 0]), 5.2, BLACK
        )

        self.add(backGroundGraphSegment)
        self.add(graphSegment)
