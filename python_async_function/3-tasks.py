#!/usr/bin/env python3
"""random"""


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    return uniform(0, max_delay)


def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
