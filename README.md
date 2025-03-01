# Python Asyncio Examples

A collection of practical examples demonstrating the power and flexibility of Python's asyncio library for asynchronous programming.

## Examples

### Basic Examples

1. **Basic Syntax** (`example_1.py`)
   - Simple coroutine definition and execution
   - Introduction to asyncio.sleep() for simulating I/O delays

2. **Event Loop in Action** (`example_2.py`)
   - Multiple coroutines running concurrently
   - Using asyncio.gather() for managing multiple tasks

3. **Simulating Network Requests** (`example_3.py`)
   - Concurrent data fetching simulation
   - Measuring performance improvements from concurrency

4. **Task Management with Error Handling** (`example_4.py`)
   - Handling exceptions in concurrent tasks
   - Using return_exceptions=True with gather()

5. **Producer-Consumer Pattern** (`example_5.py`)
   - Using asyncio.Queue for communication between coroutines
   - Implementing a simple pipeline

### Advanced Examples

6. **Concurrent File Downloads with Progress Tracking** (`example_6.py`)
   - Simulating multiple file downloads running concurrently
   - Tracking and displaying download progress

7. **Rate-Limited API Requests** (`example_7.py`)
   - Using semaphores to respect API rate limits
   - Maximizing throughput while staying within limits

8. **Periodic Background Task** (`example_10.py`)
   - Running continuous background monitoring
   - Task cancellation when main work completes

9. **Task Retry Mechanism** (`example_9.py`)
   - Implementing retry logic for flaky operations
   - Handling transient failures gracefully

### Chat Application Examples

10. **Real-Time Chat Simulation** (`example_8.py`)
    - Modeling asynchronous message broadcasting
    - Handling unpredictable message timing

11. **Multi-User Chat Room** (`example_11.py`)
    - Managing multiple users joining and leaving
    - Central broadcaster for message distribution

12. **Private Messaging with Timeout** (`example_12.py`)
    - Direct messaging between specific users
    - Timeout mechanism for inactive connections

## Getting Started

### Prerequisites

- Python 3.7 or higher (asyncio syntax is most elegant in Python 3.7+)

## When to Use Asyncio

Asyncio shines in scenarios involving:

- **I/O-bound operations**: Network requests, file operations, database queries
- **High-concurrency needs**: Handling many connections simultaneously
- **Event-driven applications**: Chat systems, notification services
- **API servers**: Efficiently processing multiple requests

## Key Benefits

- **Improved throughput**: Handle more operations concurrently without threads
- **Resource efficiency**: Lower memory footprint than traditional threading
- **Simplified concurrency**: Avoid common threading issues like race conditions
- **Deterministic execution**: Easier to reason about than preemptive multitasking
