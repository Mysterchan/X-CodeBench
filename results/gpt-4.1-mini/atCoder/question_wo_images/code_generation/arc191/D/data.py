import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M, S, T = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # We want to find the minimum number of moves to get:
    # piece A: S -> T
    # piece B: T -> S
    # Moves: move either piece A or B along an edge, but they cannot be on the same vertex at any time.

    # State: (posA, posB)
    # Initial state: (S, T)
    # Goal state: (T, S)
    # Constraint: posA != posB at all times

    # BFS over states (posA, posB)
    # Number of states: up to N*N = 4*10^10, too large to store all.
    # But we can prune and use a visited set.

    # Since N can be up to 2*10^5, storing visited as a 2D array is impossible.
    # Use a dictionary or set for visited states.

    # BFS queue: store (posA, posB, dist)
    # At each step, try moving A or B to adjacent vertices, if new positions are different and not visited.

    # This is a classic two-agent shortest path problem with collision constraints.

    # Implementation details:
    # Use a set for visited states: visited = set()
    # Each state is a tuple (posA, posB)
    # Enqueue initial state (S, T, 0)
    # For each state, generate next states by moving A or B to neighbors, if posA != posB.

    # If we reach (T, S), return dist.

    # If queue empties, return -1.

    visited = set()
    queue = deque()
    queue.append((S, T, 0))
    visited.add((S, T))

    while queue:
        posA, posB, dist = queue.popleft()
        if posA == T and posB == S:
            print(dist)
            return

        # Move A
        for nxtA in graph[posA]:
            if nxtA != posB and (nxtA, posB) not in visited:
                visited.add((nxtA, posB))
                queue.append((nxtA, posB, dist+1))

        # Move B
        for nxtB in graph[posB]:
            if nxtB != posA and (posA, nxtB) not in visited:
                visited.add((posA, nxtB))
                queue.append((posA, nxtB, dist+1))

    print(-1)

if __name__ == "__main__":
    main()