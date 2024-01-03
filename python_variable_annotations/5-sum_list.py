#!/usr/bin/env python3
"""sumfloat"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    total_sum: float = 0.0
    for num in input_list:
        total_sum += num
        """floatsum"""
    return total_sum
