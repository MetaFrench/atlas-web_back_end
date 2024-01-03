#!/usr/bin/env python3
"""tuples"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple with k and square v"""
    squared_value = float(v) ** 2
    return k, squared_value
