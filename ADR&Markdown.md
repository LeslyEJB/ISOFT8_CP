# Architectural Decision Record (ADR)

## Decision title
Choosing a concurrency model to avoid __DeadLocks__

## Status
Proposed

## Context
In our application, multiple tasks must be performed in parallel and access our shared resources; During the tests, a deadlock problem has been identified, where two or more tasks are blocked indefinitely waiting for resources that another task already has. A concurrency solution is sought where the risk of deadlocks is minimized and is efficient for our needs.

Three approaches are considered:

- __Multiprocessing__ 
  - Each process has its own memory  (avoids the issue of shared resources). 
  - Stable for heavy and parallel tasks.
  - Has higher resource consumption (each process consumes memory and CPU).
  - Communication between processes is more complex.
  - Slow for small or I/O tasks.
- __Multithreading__ 
  - Takes advantage of multiple CPU cores.
  - Works well for intensive parallel computation.
  - Uses shared memory (requires locks to protect data, can cause deadlocks).
  - Difficult to debug and maintain.
- __Asynchronicity__
  - Does not use locks (reduces the risk of deadlocks).
  - Less memory and CPU consumption.
  - Easy to read and maintain with async/await.
  - Ideal for I/O-intensive tasks.
  - Does not take advantage of multiple CPU cores for very heavy computational tasks.
  - Some libraries are not designed for asynchronicity and require adaptations.

## Decision
We decided to adopt the asynchronous programming model *(async/await)* to manage the concurrency of our system.