# Practical Example 12: Private Messaging with Timeout
# This example simulates a chat system where users send private messages to each other, with a timeout mechanism to disconnect inactive users. It uses tasks and dictionaries to track conversations.

import asyncio

async def user_sender(user_id, recipient_id, messages, user_queues):
    queue = user_queues.setdefault(user_id, asyncio.Queue())
    for msg in messages:
        print(f"User {user_id} sending to User {recipient_id}: {msg}")
        await user_queues[recipient_id].put((user_id, msg))
        await asyncio.sleep(1)  # Simulate typing delay
    print(f"User {user_id} finished sending messages")

async def user_receiver(user_id, user_queues, timeout=5):
    queue = user_queues.setdefault(user_id, asyncio.Queue())
    try:
        while True:
            # Wait for a message with a timeout
            sender_id, message = await asyncio.wait_for(queue.get(), timeout=timeout)
            print(f"User {user_id} received from User {sender_id}: {message}")
            queue.task_done()
    except asyncio.TimeoutError:
        print(f"User {user_id} disconnected due to inactivity")

async def main():
    user_queues = {}  # Shared queues for each user
    
    # Define user conversations
    conversations = [
        (1, 2, ["Hey!", "How are you?", "See ya!"]),  # User 1 to User 2
        (2, 1, ["Hi!", "Good, you?"])                # User 2 to User 1
    ]
    
    # Start senders and receivers
    tasks = [
        user_sender(user_id, recipient_id, messages, user_queues)
        for user_id, recipient_id, messages in conversations
    ] + [
        user_receiver(user_id, user_queues)
        for user_id in {1, 2}  # Unique users
    ]
    
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())

# Why it’s useful: Demonstrates private messaging between users, a common feature in chat apps, with a timeout to clean up inactive sessions.
# Key feature: Uses a dictionary of asyncio.Queue objects to route messages between specific users, and asyncio.wait_for to implement timeouts.
# Real-world tip: Add persistent storage (e.g., a database) and replace queues with network sockets or WebSockets for a production system.
