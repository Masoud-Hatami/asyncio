# Example 5: Producer-Consumer Pattern
# Let’s simulate a pipeline where one coroutine produces data and another consumes it, using an asyncio.Queue.

import asyncio 
import random

async def producer(queue):
    for i in range(5):
        item = f" Item {i}"
        print(f" Producing {item}")
        await queue.put(item)
        await asyncio.sleep(random.uniform(0.5, 1))  # Random delay
    await queue.put(None)  # Signal end of production

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:  # Check for end signal
            break
        print(f"Consuming {item}")
        await asyncio.sleep(1)  # Simulate processing time
    print("Consumer done")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())

# "asyncio.Queue" safely handles communication between producers and consumers.
# The None sentinel signals the consumer to stop.