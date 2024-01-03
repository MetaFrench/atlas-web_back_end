#!/usr/bin/env python3
"""union"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of integers and floats in list"""
    return sum(mxd_lst)
