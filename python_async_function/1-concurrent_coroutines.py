#!/usr/bin/env python3
"""concurrent"""


import asyncio
# Importing wait_random from the previous file
from random_delay import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)


async def main():
    # Example: wait for 5 random delays up to 10 seconds each
    delays = await wait_n(5, 10)
    print(delays)  # Print the sorted list of delays

if __name__ == "__main__":
    asyncio.run(main())
