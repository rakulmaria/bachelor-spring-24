from manim import *
from shapely.geometry import LineString

"""
    Move along a path with a kilter, uses shapely to kilter the path.

    If the path is crossing itself, the kilter will not work as expected.
    This is caused by shapely's offset_curve function, that is expected to have zero area.
"""


class MoveAlongPathWithKilter(AnimationGroup):
    def __init__(
        self,
        path: VMobject,
        dot: Dot = Dot(color=ORANGE).scale(0.7),
        kilter: float = 0,
        offset: float = 0,
        run_time: float = 2,
        rate_func: callable = linear,
        **kwargs,
    ) -> None:
        path_points = path.get_points()
        path_coords = [(point[0], point[1]) for point in path_points]
        path_linestring = LineString(path_coords)

        offset_line1 = path_linestring.offset_curve(kilter)
        offset_points1 = np.array([[x, y, 0] for x, y in offset_line1.coords])

        path1 = VMobject()
        path1.set_points_as_corners(offset_points1)

        anim1 = MoveAlongPathWithOffset(
            dot,
            path1,
            rate_func=rate_func,
            offset=offset,
            run_time=run_time,
        )

        super().__init__(anim1, **kwargs)


"""
    Same as MoveAlongPath, but with an offset.
"""


class MoveAlongPathWithOffset(Animation):
    def __init__(
        self,
        mobject: Mobject,
        path: VMobject,
        suspend_mobject_updating: bool | None = False,
        offset: float = 0,
        **kwargs,
    ) -> None:
        self.path = path
        self.offset = offset
        super().__init__(
            mobject, suspend_mobject_updating=suspend_mobject_updating, **kwargs
        )

    def interpolate_mobject(self, alpha: float) -> None:
        point = self.path.point_from_proportion(
            self.rate_func((alpha + self.offset) % 1)
        )
        self.mobject.move_to(point)
