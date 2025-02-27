# Practical Example 9: Multi-User Chat Room
# This example simulates a chat room where multiple users send messages asynchronously, and a central broadcaster shares them with all participants. It uses an asyncio.Queue to handle message passing.

import asyncio
import random

async def user_client(user_id, queue):
    # Simulate a user sending 3 messages at random intervals
    for i in range(3):
        message = f"User {user_id}: Message {i + 1}"
        print(f"User {user_id} sending: {message}")
        await queue.put((user_id, message))
        await asyncio.sleep(random.uniform(0.5, 2))  # Random typing speed
    # Signal user is done
    await queue.put((user_id, None))

async def chat_broadcaster(queue, users):
    # Maintain a list of active users
    active_users = set(users)
    while active_users:
        user_id, message = await queue.get()
        if message is None:  # User has left
            active_users.remove(user_id)
            print(f"User {user_id} has left the chat. Remaining: {len(active_users)}")
        else:
            # Broadcast message to all (simulated by printing)
            print(f"Broadcasting to all: {message}")
        queue.task_done()
    print("Chat room closed")

async def main():
    queue = asyncio.Queue()
    users = [1, 2, 3]  # Simulate 3 users
    
    # Start user clients and broadcaster concurrently
    await asyncio.gather(
        *(user_client(user_id, queue) for user_id in users),
        chat_broadcaster(queue, users)
    )

asyncio.run(main())

# Why it’s useful: This mimics a basic chat room where users send messages at their own pace, and a central system broadcasts them to everyone.
# Key feature: Uses an asyncio.Queue to collect messages and a broadcaster coroutine to simulate real-time sharing. Users signal their exit with None.
# Real-world tip: In a real chat app, replace the print statements with WebSocket sends (e.g., using aiohttp).