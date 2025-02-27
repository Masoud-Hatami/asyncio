# Practical Example 5: Rate-Limited API Requests
# Simulate making API requests with a rate limit (e.g., 2 requests per second) using a semaphore to control concurrency.

import asyncio
import time

async def fetch_api(endpoint, semaphore):
    async with semaphore:  # Limit concurrency
        print(f"Requesting {endpoint} at {time.time():.2f}")
        await asyncio.sleep(1)  # Simulate API call
        print(f"Received response from {endpoint}")
        return f"Response from {endpoint}"

async def main():
    semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent requests
    endpoints = ["api/users", "api/posts", "api/comments", "api/photos"]
    start_time = time.time()
    results = await asyncio.gather(*(fetch_api(ep, semaphore) for ep in endpoints))
    print(f"Results: {results}")
    print(f"Total time: {time.time() - start_time:.2f}s")

asyncio.run(main())

# Why it’s useful: Many APIs enforce rate limits; this shows how to respect them while maximizing throughput.
#Key feature: asyncio.Semaphore ensures only 2 requests run at once, batching the work efficiently.
