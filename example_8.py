# Practical Example 6: Real-Time Chat Simulation
# Simulate a simple chat system where multiple users send messages asynchronously, processed by a central handler.

import asyncio
import random

async def user_send_message(user, queue):
    for _ in range(3):  # Each user sends 3 messages
        message = f"{user} says: Hello {random.randint(1, 100)}"
        print(f"Sending: {message}")
        await queue.put(message)
        await asyncio.sleep(random.uniform(0.5, 2))  # Random typing speed

async def chat_handler(queue):
    while True:
        message = await queue.get()
        if message is None:  # Exit signal
            break
        print(f"Chat broadcast: {message}")
        await asyncio.sleep(0.1)  # Simulate processing

async def main():
    queue = asyncio.Queue()
    users = ["Alice", "Bob", "Charlie"]
    await asyncio.gather(
        *(user_send_message(user, queue) for user in users),
        chat_handler(queue)
    )
    await queue.put(None)  # Stop the handler

asyncio.run(main())

# Why it’s useful: Models a real-time system like a chat server where messages arrive unpredictably.
# Key feature: Combines Queue with concurrent message producers and a single consumer.