import random
from manim import *
from src.path import *
from src.utils import *

"""
    The Flow class creates 30 dots to move along an augmenting path.
    Currently, this only works if no backwards edges are used in the path, meaning that the path
    is not "undooing" a previous flow.

    Uncomment the offset parameter in the MoveAlongPathWithKilter class to make the dots start with a random offset.
"""


class Flow(VMobject):
    def __init__(
        self,
        path: VMobject,
        scene: Scene,
        kilter_start: float = 0,
        kilter_end: float = 0,
        theme: Themes = Themes.Light,
    ):
        # self.draw_path(path, (kilter_end * 0.9), scene)

        for _ in range(30):
            a = turn_animation_into_updater(
                MoveAlongPathWithKilter(
                    path=path,
                    dot=Dot(color=random.choice(theme.get("DOTS")))
                    .scale(0.2)
                    .set_z_index(100),
                    kilter=random.uniform((kilter_start * 0.9), (kilter_end * 0.9)),
                    run_time=random.uniform(3, 8),
                    # offset=random.uniform(0, 3),
                ),
                cycle=True,
            )
            scene.add(a)

        super().__init__()

    """
        Helper function to draw the path with kilter. Uncomment line 13 to use this function.
    """

    def draw_path(self, path: VMobject, offset, scene: Scene) -> None:
        path_points = path.get_points()
        path_coords = [(point[0], point[1]) for point in path_points]
        path_linestring = LineString(path_coords)

        offset_line1 = path_linestring.offset_curve(offset)
        offset_line2 = path_linestring.offset_curve(-offset)

        offset_points1 = np.array([[x, y, 0] for x, y in offset_line1.coords])
        offset_points2 = np.array([[x, y, 0] for x, y in offset_line2.coords])
        path2 = VMobject()

        path1 = VMobject(color=PINK).set_z_index(200)
        path2 = VMobject(color=PINK).set_z_index(200)

        path1.set_points_as_corners(offset_points1)
        path2.set_points_as_corners(offset_points2)

        scene.add(path1)
        scene.add(path2)
