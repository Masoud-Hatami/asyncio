# Practical Example 9: Task Retry Mechanism
# Implement a retry mechanism for flaky tasks (e.g., network calls that might fail temporarily).

import asyncio
import random

async def flaky_task(name, max_attempts=3):
    attempt = 1
    while attempt <= max_attempts:
        try:
            print(f"{name}: Attempt {attempt}")
            await asyncio.sleep(1)  # Simulate work
            if random.random() < 0.7:  # 70% chance of failure
                raise ValueError("Temporary failure")
            print(f"{name}: Succeeded")
            return f"Result from {name}"
        except ValueError as e:
            print(f"{name}: {e}, retrying...")
            attempt += 1
            await asyncio.sleep(0.5)  # Backoff
    print(f"{name}: All attempts failed")
    return None

async def main():
    tasks = [
        flaky_task("Task A"),
        flaky_task("Task B"),
        flaky_task("Task C")
    ]
    results = await asyncio.gather(*tasks)
    print(f"Final results: {results}")

asyncio.run(main())

# Why it’s useful: Network operations often fail temporarily; retries can improve reliability.
# Key feature: Implements a loop with backoff inside a coroutine, running multiple tasks concurrently.