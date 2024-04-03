from manim import *
import math


class FlowPolygon(Line):
    def __init__(self, edge, flow):
        size = 9
        self.polygons = VGroup()
        darkBlue = AS2700.B24_HARBOUR_BLUE
        lightBlue = AS2700.B41_BLUEBELL
        borderBlue = AS2700.B21_ULTRAMARINE
        self.times = 0

        (flow_start_coord, flow_end_coord), direction = self.get_flow_coords(edge, flow)
        super().__init__(start=flow_start_coord, end=flow_end_coord, z_index=4)
        super().set_stroke(
            width=((math.sqrt(edge.max_capacity) * 8) / edge.max_capacity * flow),
            color=lightBlue,
        )
        super().set_fill(color=BLUE)

        # scale object down to 0.1
        scale_factor = 0.1
        position_list = [
            [0, 3, 0],  # top left
            [4, 3, 0],  # top right
            [6, 0, 0],  # middle right
            [4, -3, 0],  # bottom right
            [0, -3, 0],  # bottom left
            [2, 0, 0],  # middle left
        ]

        for _ in range(size):
            obj = Polygon(*position_list, z_index=5)
            obj.scale(scale_factor)
            obj.set_stroke(borderBlue, opacity=1.0, width=0.0)

            # set color of every other object to differ
            if len(self.polygons) % 3 == 0:
                obj.set_fill(darkBlue, 0.8)
            else:
                obj.set_fill(lightBlue, 0.8)
            self.polygons.add(obj)

        self.polygons.arrange(buff=-1, direction=LEFT)
        self.polygons.move_to(self.get_center())
        self.polygons.stretch_to_fit_width(self.get_length())
        self.polygons.stretch_to_fit_height(self.stroke_width / 100)
        self.polygons.rotate(self.angle_from_vector(direction))
        self.add(self.polygons)

        def update(mobject):
            self.times += 1
            changed = []
            if self.times > 10:
                for i, dot in enumerate(mobject):
                    if i in changed:
                        continue
                    self.times = 0
                    if dot.color == darkBlue:
                        mobject[i].set_fill(lightBlue)

                        if (1 + i) < len(mobject):
                            mobject[i + 1].set_fill(darkBlue)
                        else:
                            mobject[0].set_fill(darkBlue)
                        changed.append(i + 1)

        self.polygons.add_updater(update)

    def get_flow_coords(self, edge, flow):
        x_start = edge.start_vertex.x_coord
        y_start = edge.start_vertex.y_coord
        x_end = edge.end_vertex.x_coord
        y_end = edge.end_vertex.y_coord
        h_top = (edge.foregroundLine.stroke_width / 100) / 2
        h = h_top - (h_top / edge.max_capacity * flow)

        v1 = x_end - x_start
        v2 = y_end - y_start
        z1 = -v2
        z2 = v1

        vector = np.array([z1, z2, 0])
        original_vector = np.array([v1, v2, 0])

        direction = vector / np.linalg.norm(vector)
        direction_original = original_vector / np.linalg.norm(original_vector)
        scaled_vector = direction * h

        a = edge.start_vertex.to_np_array() + scaled_vector
        b = edge.end_vertex.to_np_array() + scaled_vector

        return (
            a,
            b,
        ), direction_original

    def angle_from_vector(self, vector):
        angle_rad = np.arctan2(vector[1], vector[0])
        angle_rad %= 2 * np.pi

        return angle_rad
