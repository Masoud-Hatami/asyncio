# Getting Started: Basic Syntax
import asyncio

# define a coroutine
async def say_hello():
    print("Hello")
    await asyncio.sleep(1) # Pauses the coroutine until the awaited operation completed
    print("World")

# Run the coroutine
asyncio.run(say_hello())

# When you run this, it prints "Hello", waits 1 second, then prints "World".
#  The sleep here mimics an I/O delay without blocking the thread.