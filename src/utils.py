from enum import Enum
import math
from manim import core


class GrowthScale(Enum):
    SQRT = "sqrt"
    LINEAR = "linear"
    LOG2 = "log2"


class Themes(Enum):
    Light = {
        "BACKGROUND": "#FFFFFF",
        "BORDER": "#000000",  # or '#2726D9',
        "OBJECT-BACKGROUND": "#FFFFFF",  # color of the edge and dot without the flow
        "FLOW": "#5B94D1",
        "DOTS": core.color_gradient(["#B7C8DB", "#7DB7C7"], 6),
        "TEXT": "#000000",
        "ARROW": "#CF5044",
    }
    Dark = {
        "BACKGROUND": "#303240",  # Dark background
        "BORDER": "#708090",  # White or light grey for contrast
        "OBJECT-BACKGROUND": "#262626",  # Slightly lighter dark color for flow background
        "FLOW": "#446688",  # Muted blue for flow
        "DOTS": core.color_gradient(
            ["#81AAC2", "#2F4E60"], 6
        ),  # Darker gradient colors for dots
        "TEXT": "#FFFFFF",  # White text for readability
        "ARROW": "#FF6F61",  # Soft red for arrows, with good contrast
    }
    Pacman = {
        "BACKGROUND": "#0D0503",
        "BORDER": "#1A1F73",  # or '#2726D9',
        "OBJECT-BACKGROUND": "#232CD9",
        "FLOW": "#787CDF",
        "DOTS": core.color_gradient(["#FFB747", "#FBB8DB", "#05F2C7", "#F20505"], 6),
        "TEXT": "#FFC3A0",
        "ARROW": "#FFC3A0",
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
