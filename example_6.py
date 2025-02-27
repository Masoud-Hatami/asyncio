# Practical Example 6: Concurrent File Downloads with Progress Tracking

# Simulate downloading multiple files concurrently and tracking their progress.
#  This mimics a scenario where you’re fetching large files from the internet.

import asyncio
import random

async def download_file(filename, size_mb):
    print(f"Starting download: {filename} ({size_mb}MB)")
    for i in range(size_mb):
        await asyncio.sleep(0.5)  # Simulate downloading 1MB at a time
        print(f"{filename}: Downloaded {i+1}/{size_mb}MB")
    print(f"Completed: {filename}")
    return f"{filename} downloaded"

async def main():
    files = [
        ("video.mp4", 3),
        ("image.png", 2),
        ("document.pdf", 4)
    ]
    results = await asyncio.gather(*(download_file(name, size) for name, size in files))
    print(f"All downloads complete: {results}")

asyncio.run(main())

# Why it’s useful: Shows how asyncio can handle multiple independent tasks with progress updates, similar to a download manager.
# Key feature: Uses gather to run downloads concurrently, with simulated delays for each "chunk."