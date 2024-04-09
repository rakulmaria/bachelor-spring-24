from manim import *
import math

lightBlue = AS2700.B41_BLUEBELL


class Vertex(VMobject):
    def __init__(self, id, x_coord, y_coord):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.outgoing_capacity = 0
        self.ingoing_capacity = 0
        self.current_flow = 0
        self.flow_object = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size("sqrt"))
            .set_fill(lightBlue)
            .set_opacity(0)
            .set_z_index(12)
        )
        self.foregroundDot = None

        super().__init__()

    def get_drawn_dot_size(self, growth_scale="sqrt"):
        if growth_scale == "sqrt":
            return math.sqrt(self.get_max_drawn_capacity()) / 2
        if growth_scale == "linear":
            return self.get_max_drawn_capacity() / 2
        if growth_scale == "log2":
            return math.log2(self.get_max_drawn_capacity()) / 2

    def get_drawn_label_size(self, scale=1, growth_scale="sqrt"):
        if growth_scale == "sqrt":
            return math.sqrt(scale) * 0.2
        if growth_scale == "linear":
            return scale * 0.2
        if growth_scale == "log2":
            return math.log2(scale) * 0.2

    def draw(self, scale=1, growth_scale="sqrt"):
        self.foregroundDot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size(growth_scale))
            .set_fill(WHITE)
            .set_z_index(10)
        )

        self.add(self.foregroundDot)

        backgroundDot = (
            Dot(self.to_np_array())
            .scale(self.get_drawn_dot_size(growth_scale) + 0.1)
            .set_fill(BLACK)
            .set_z_index(0)
        )

        self.add(backgroundDot)

        label = Tex(self.id, color=BLACK).set_x(self.x_coord).set_y(self.y_coord)
        label.set_z_index(20)
        label.scale(self.get_drawn_label_size(scale, growth_scale))
        self.add(label)

    def to_np_array(self):
        return np.array([self.x_coord, self.y_coord, 0])

    def add_to_max_ingoing_capacity(self, capacity):
        self.ingoing_capacity += capacity

    def add_to_max_outgoing_capacity(self, capacity):
        self.outgoing_capacity += capacity

    def get_opacity(self, flow):
        return flow / self.get_max_opacity()

    def get_max_drawn_capacity(self):
        return max(self.outgoing_capacity, self.ingoing_capacity)

    # helper function
    def get_max_opacity(self):
        # edge case for source and sink vertices
        if self.ingoing_capacity == 0 or self.outgoing_capacity == 0:
            return max(self.ingoing_capacity, self.outgoing_capacity)
        return min(self.ingoing_capacity, self.outgoing_capacity)

    def add_to_current_flow(self, new_flow, scene):
        if new_flow <= self.get_max_opacity():
            self.current_flow += new_flow
            new_flow_object = (
                Dot(self.to_np_array())
                .scale(self.get_drawn_dot_size("sqrt"))
                .set_fill(lightBlue)
                .set_opacity(self.get_opacity(self.current_flow))
                .set_z_index(13)
            )
            scene.play(ReplacementTransform(self.flow_object, new_flow_object))
            self.flow_object = new_flow_object
        else:
            print("Error: New capacity exceeds maximum capacity")


"""
class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        v = Vertex("vertex0", 0, 0, 5)
        self.add(v)
        self.wait(1)

        v2 = Vertex("vertex1", 2, 2, 4)
        self.add(v2)
        self.wait(1)
 """
