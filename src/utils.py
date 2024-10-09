from enum import Enum
import math
from manim import color_gradient


class GrowthScale(Enum):
    SQRT = "sqrt"
    LINEAR = "linear"
    LOG2 = "log2"


class Themes(Enum):
    Light = {
        "BACKGROUND": "#FFFFFF",
        "BORDER": "#000000",  # or '#2726D9',
        "FLOW-BACKGROUND": "#FFFFFF",
        "FLOW": "#5B94D1",
        "DOTS": color_gradient(["#B7C8DB", "#7DB7C7"], 6),
        "TEXT": "#000000",
        "ARROW": "#CF5044",
    }
    Dark = {}
    Pacman = {
        "BACKGROUND": "#0D0503",
        "BORDER": "#1A199A",  # or '#2726D9',
        "FLOW-BACKGROUND": "#FFFFFF",
        "FLOW": "#FEBAE1",
        "DOTS": color_gradient(["#FFE7DF", "#FEE9FF"], 6),
        "TEXT": "#FFFF01",
        "ARROW": "#F20505",
    }

    def __getitem__(self, key):
        return self.value[key]

    def get(self, key, default=None):
        return self.value.get(key, default)


def get_drawn_size(growth_scale, size):
    if growth_scale == GrowthScale.LINEAR:
        return size
    if size == 0:
        return 0
    if growth_scale == GrowthScale.SQRT:
        if size < 0:
            return math.sqrt(-1 * size) * -1
        else:
            return math.sqrt(size)
    if growth_scale == GrowthScale.LOG2:
        if size < 0:
            return math.log2(-1 * size) * -1
        else:
            return math.log2(size) + 1
