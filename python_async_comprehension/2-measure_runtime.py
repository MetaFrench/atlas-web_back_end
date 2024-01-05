#!/usr/bin/env python3
"""measure"""

import asyncio
from typing import List
from time import perf_counter


async def measure_runtime() -> float:
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time
