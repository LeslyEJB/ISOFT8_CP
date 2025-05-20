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

## Justification
1. Avoid traditional deadlocks. The asynchronous model doesn't use multiple threads or parallel processes competing for shared resources. Instead, tasks cooperate by relinquishing control via await, which eliminates the need for locks and thus reduces the risk of deadlocks to virtually zero.
2. Predictable execution flow. Unlike multithreading, where the operating system can change the execution context at any time, asynchrony works with a single main thread, and execution is more controlled. This makes concurrent behavior easier to reason about and debug.
3. Efficiency in I/O tasks. Since many of our operations are input/output (such as file reads, network connections, or database queries), asynchrony is ideal. It allows the main thread not to be blocked while waiting for an external response, improving system efficiency without creating extra threads or processes.
4. Lower resource consumption. Creating and managing threads or processes involves significant overhead in terms of memory and CPU usage. Asynchrony, on the other hand, uses fewer resources, which translates into greater scalability, especially in web applications or systems with multiple simultaneous connections.
5. Readability and maintainability. With async/await, code follows a clear, sequential structure, making it easier to write, read, and maintain. This is especially valuable when compared to nested callbacks or the complexity of thread synchronization.
## Consequences
1. Practical elimination of deadlocks due to thread blocking, since traditional locks and critical sections are not used.
2. Risk of "starvation" if a long task doesn't relinquish control in a timely manner; it's necessary to design chunks or use timers to maintain flow.
3. Some libraries may not be fully asynchronous, requiring adaptation or wrapping of blocking APIs so they don't interfere with the event loop.
4. High scalability for intensive I/O operations, allowing for a high degree of concurrency with low memory and CPU usage.

#### CATLovers Team + 2

- Adiel Nefthali Delgado Silva
- Virgen Jazmin Morales Carrillo
- Alberto Carlos Navarrete Garcia
- Alan Ismael Franquez Conchas
- Lesly Elizabeth Jimenez Burriola.

##### *Date:Thursday, May 15, 2025*
