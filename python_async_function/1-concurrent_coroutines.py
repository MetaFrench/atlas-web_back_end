#!/usr/bin/env python3
"""concurency"""


import asyncio
from typing import List
from random import uniform
from asyncio import gather


async def wait_random(max_delay: int = 10) -> float:
    return uniform(0, max_delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await gather(*tasks)
    return sorted(results)

# Example usage:


async def main():
    delays = await wait_n(5, 8)
    print(delays)

# Run the event loop
asyncio.run(main())
