from enum import Enum
import math
from manim import core


class GrowthScale(Enum):
    SQRT = "sqrt"
    LINEAR = "linear"
    LOG2 = "log2"


class Themes(Enum):
    Light = {
        "FRAME-BACKGROUND": "#FFFFFF",
        "BORDER": "#000000",
        "OBJECT-BACKGROUND": "#FFFFFF",  # color of the edge and dot without the flow
        "FLOW": "#5B94D1",
        "DOTS": core.color_gradient(["#B7C8DB", "#7DB7C7"], 6),
        "TEXT": "#000000",
        "ARROW": "#CF5044",
    }
    Dark = {
        "FRAME-BACKGROUND": "#303240",
        "BORDER": "#708090",
        "OBJECT-BACKGROUND": "#262626",
        "FLOW": "#446688",
        "DOTS": core.color_gradient(["#81AAC2", "#2F4E60"], 6),
        "TEXT": "#FFFFFF",
        "ARROW": "#FF6F61",
    }
    Pacman = {
        "FRAME-BACKGROUND": "#0D0503",
        "BORDER": "#1A1F73",  # or '#2726D9',
        "OBJECT-BACKGROUND": "#232CD9",
        "FLOW": "#787CDF",
        "DOTS": core.color_gradient(["#FFB747", "#FBB8DB", "#05F2C7", "#F20505"], 6),
        "TEXT": "#FFC3A0",
        "ARROW": "#FFC3A0",
    }
    Pastel = {
        "FRAME-BACKGROUND": "#FCE4EC",  # Soft cream for the background
        "BORDER": "#C5C6D0",  # Light lavender-gray for a subtle border
        "OBJECT-BACKGROUND": "#E8EAF6",  # Pastel blue-gray for the object background
        "FLOW": "#A6D8D4",  # Minty pastel teal for flow elements
        "DOTS": ["#A3C4F3", "#FEB1A9", "#FEF2CD", "#CFF2B8", "#A6D8DB", "#BD9CF9"],
        "TEXT": "#4B4B4B",  # Dark gray text for readability without harshness
        "ARROW": "#FFABAB",  # Soft coral for arrows to add warmth
    }
    LGBT = {
        "FRAME-BACKGROUND": "#FFFFFF",
        "BORDER": "#000000",
        "OBJECT-BACKGROUND": "#FFFFFF",  # color of the edge and dot without the flow
        "FLOW": "#5B94D1",
        "DOTS": ["#FF3D00", "#FF9800", "#FFEB3B", "#4CAF50", "#2196F3", "#9C27B0"],
        "TEXT": "#000000",
        "ARROW": "#CF5044",
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
