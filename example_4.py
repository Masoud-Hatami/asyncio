# Example 4 : Task Management with Error handeling
# What if a task fails? Let's handle exceptions and cancel tasks if needed.

import asyncio

async def risky_task(name, delay, fail=False):
    print(f"{name} starting")
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(f"{name} failed!" )
    print(f"{name} completed!")
    return f"Result from {name}"

async def main():
    task = [
        risky_task("Task 1", 1),
        risky_task("Task 2", 2, fail=True),
        risky_task("Task 3 ", 1)
    ]
    try:
      results = await asyncio.gather(*task, return_exceptions=True)
      for result in results:
          if isinstance(result, Exception):
              print(f"Task raised: {result}")
          else:
              print(f"Success: {result}")
    except Exception as e:
        print(f"Caught exception: {e}")

asyncio.run(main())
# "return_exceptions=True" in gather prevents the exception from stopping other tasks.
# We can inspect results to distinguish successes from failures.