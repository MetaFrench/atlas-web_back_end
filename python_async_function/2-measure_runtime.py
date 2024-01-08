#!/usr/bin/env python3
"""runtime"""

import time
from typing import Callable


async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
