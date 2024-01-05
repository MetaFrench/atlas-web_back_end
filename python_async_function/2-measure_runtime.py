#!/usr/bin/env python3
"""runtime"""

import asyncio
import time
from typing import List
from random import random
from typing import Generator


async def wait_random(max_delay: int = 10) -> float:
    return random() * max_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    return [await wait_random(max_delay) for _ in range(n)]


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n


# Test case
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay)))
