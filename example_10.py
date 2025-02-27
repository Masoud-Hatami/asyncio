# Practical Example 8: Periodic Background Task
# Run a background task (e.g., polling a resource) alongside other work, cancellable when done.

import asyncio

async def poll_status():
    while True:
        print("Polling status...")
        await asyncio.sleep(2)  # Poll every 2 seconds

async def main_work():
    print("Starting main work")
    await asyncio.sleep(5)  # Simulate some work
    print("Main work completed")

async def main():
    poller = asyncio.create_task(poll_status())  # Start background task
    await main_work()
    poller.cancel()  # Stop polling when main work is done
    try:
        await poller
    except asyncio.CancelledError:
        print("Polling stopped")

asyncio.run(main())

# Why it’s useful: Common in applications needing periodic checks (e.g., monitoring, heartbeat signals).
# Key feature: Uses create_task for a background coroutine and demonstrates cancellation.