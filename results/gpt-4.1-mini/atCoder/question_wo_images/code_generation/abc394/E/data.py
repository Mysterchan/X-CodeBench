from collections import deque

def main():
    N = int(input())
    C = [input() for _ in range(N)]

    # dist[i][j] = shortest length of palindrome path from i to j
    # We'll use 0-based indexing internally
    # The problem: find shortest path from i to j such that the concatenation of edge labels is a palindrome.

    # Key idea:
    # We consider pairs of vertices (u,v) representing the "front" and "back" of the palindrome path.
    # Initially, for all i, dist[i][i] = 0 (empty path, palindrome)
    # For edges (u->v) with label c, dist[u][v] = 1 (single edge path, palindrome of length 1)
    # Then we try to extend palindrome paths by matching edges from front and back with the same label.

    # We'll do a BFS on pairs (u,v) representing the minimal palindrome path from u to v.

    dist = [[-1]*N for _ in range(N)]
    queue = deque()

    # Initialize:
    # 1) dist[i][i] = 0 (empty path)
    for i in range(N):
        dist[i][i] = 0
        queue.append((i,i))

    # 2) For edges (u->v) with label c, dist[u][v] = 1 (single edge palindrome)
    for u in range(N):
        for v in range(N):
            if C[u][v] != '-':
                if dist[u][v] == -1 or dist[u][v] > 1:
                    dist[u][v] = 1
                    queue.append((u,v))

    # BFS on pairs (u,v)
    # From (u,v), try to extend palindrome by adding edges with same label c:
    # For all edges u->u2 with label c and v2->v with label c,
    # if dist[u2][v2] not set or can be improved, update dist[u2][v2] = dist[u][v] + 2
    while queue:
        u, v = queue.popleft()
        cur_dist = dist[u][v]
        # Try to extend palindrome by adding matching edges at front and back
        for u2 in range(N):
            c1 = C[u][u2]
            if c1 == '-':
                continue
            for v2 in range(N):
                c2 = C[v2][v]
                if c2 == '-':
                    continue
                if c1 == c2:
                    nd = cur_dist + 2
                    if dist[u2][v2] == -1 or dist[u2][v2] > nd:
                        dist[u2][v2] = nd
                        queue.append((u2,v2))

    # Print results
    for i in range(N):
        print(' '.join(str(dist[i][j]) for j in range(N)))

if __name__ == "__main__":
    main()