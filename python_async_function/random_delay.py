#!/usr/bin/env python3
"""delay"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    """randomdelay"""
    return delay
