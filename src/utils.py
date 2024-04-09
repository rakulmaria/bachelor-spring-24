from enum import Enum
import math


class GrowthScale(Enum):
    SQRT = "sqrt"
    LINEAR = "linear"
    LOG2 = "log2"


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
