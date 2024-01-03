#!/usr/bin/env python3
"""multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier."""
    def multiplier_function(number: float) -> float:
        return number * multiplier
    return multiplier_function
