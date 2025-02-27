#Example 3: Simulating Network Requests
# Let’s simulate fetching data from multiple websites. 
# In a real app, you’d use a library like aiohttp, 
# but here we’ll use asyncio.sleep to mimic delays.

import asyncio
import time 

async def fetch_data(site, delay):
    print(f"Fetching {site}..,")
    await asyncio.sleep(delay)
    print(f"Finished fetching {site}")
    return f"Data from {site}"

async def main():
    start_time = time.time()

    # Run multiple fetches concurrently
    results = await asyncio.gather(
        fetch_data("site1.com", delay=2),
        fetch_data("site2.com", delay=1),
        fetch_data("site3.com", delay=3)
    )

    print(f"Results: {results}")
    print(f"Total Time: {time.time()- start_time:.2f}s")

asyncio.run(main())

#In a synchronous version, this would take 2 + 1 + 3 = 6 seconds. 
# With asyncio, it takes only as long as the slowest task (3 seconds),because they run concurrently.