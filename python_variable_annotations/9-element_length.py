#!/usr/bin/env python3
"""length"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """returnvalue"""
    return [(i, len(i)) for i in lst]
