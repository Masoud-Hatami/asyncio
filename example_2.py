# the Event loop in action
# The event loop is the engine of asyncio.
#  You don’t often interact with it directly when using asyncio.run(), but understanding it is key. 
# Here's an example with multiple coroutines:

import asyncio

async def task(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay=2)
    print(f"{name} done after {delay}s")

async def main():
    await asyncio.gather(
        task("task 1", 1),
        task("Task 2", 2),
        task("Task 3", 3)
    )

asyncio.run(main())

#asyncio.gather() 
#runs multiple coroutines concurrently.
#The event loop switches between tasks while they’re awaiting, making it feel like they’re running in parallel.