from manim import *
import random
from shapely.geometry import LineString


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


class WithKilter(Scene):
    def construct(self):
        path = VMobject(
            stroke_color=WHITE, stroke_width=1, joint_type=LineJointType.ROUND
        )
        path.set_points_as_corners((3 * UL, ORIGIN, [3, 0, 0], [0, -1, 0], 3 * DR))

        self.add(path)

        self.draw_path(path, 0.5)

        for i in range(100):
            a = turn_animation_into_updater(
                MoveAlongPathWithKilter(
                    path=path,
                    dot=Dot(color=BLUE).scale(0.7),
                    kilter=random.random() - 0.5,
                    offset=random.random(),
                    run_time=random.randint(3, 8),
                ),
                cycle=True,
            )

            self.add(a)

        # self.play(MoveAlongPathWithKilter(path=path, kilter=-0.1, offset=0.5))

        self.wait(3)

    def draw_path(self, path: VMobject, offset) -> None:
        path_points = path.get_points()
        path_coords = [(point[0], point[1]) for point in path_points]
        path_linestring = LineString(path_coords)

        offset_line1 = path_linestring.offset_curve(offset)
        offset_line2 = path_linestring.offset_curve(-offset)

        offset_points1 = np.array([[x, y, 0] for x, y in offset_line1.coords])
        offset_points2 = np.array([[x, y, 0] for x, y in offset_line2.coords])
        path2 = VMobject()

        path1 = VMobject()
        path2 = VMobject()

        path1.set_points_as_corners(offset_points1)
        path2.set_points_as_corners(offset_points2)

        path.add(path1)
        path.add(path2)


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
