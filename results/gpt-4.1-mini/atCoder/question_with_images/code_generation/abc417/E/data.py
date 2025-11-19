import sys
import collections

input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N, M, X, Y = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        for __ in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        # Sort adjacency lists to ensure lex order traversal
        for i in range(1, N+1):
            graph[i].sort()

        # BFS to find lex smallest path from X to Y
        visited = [False]*(N+1)
        parent = [-1]*(N+1)
        queue = collections.deque()
        queue.append(X)
        visited[X] = True

        while queue:
            curr = queue.popleft()
            if curr == Y:
                break
            for nxt in graph[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[nxt] = curr
                    queue.append(nxt)

        # Reconstruct path from Y to X
        path = []
        cur = Y
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        path.reverse()

        print(*path)

if __name__ == "__main__":
    main()