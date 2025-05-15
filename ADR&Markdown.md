# Architectural Decision Record (ADR)

## DECISION TITLE
Choosing a concurrency model to avoid DeadLocks

## STATUS
Proposed

## CONTEXT
In our application, multiple tasks must be performed in parallel and access our shared resources; During the tests, a deadlock problem has been identified, where two or more tasks are blocked indefinitely waiting for resources that another task already has. A concurrency solution is sought where the risk of deadlocks is minimized and is efficient for our needs.