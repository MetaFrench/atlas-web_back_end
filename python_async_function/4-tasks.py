#!/usr/bin/env python3
"""hello"""

import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """hello"""
    async def wait_random(max_delay: int) -> float:
        return random.uniform(0, max_delay)

    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
