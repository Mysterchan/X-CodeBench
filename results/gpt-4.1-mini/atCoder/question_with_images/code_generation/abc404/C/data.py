import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    # For a cycle graph with N vertices:
    # - Number of edges must be exactly N
    # - Each vertex must have degree 2
    # - The graph must be connected

    if M != N:
        print("No")
        return

    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # Check degree of each vertex
    for i in range(1, N+1):
        if len(adj[i]) != 2:
            print("No")
            return

    # Check connectivity using DFS
    visited = [False] * (N+1)
    def dfs(u):
        stack = [u]
        visited[u] = True
        count = 1
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
                    count += 1
        return count

    # Start DFS from vertex 1
    count = dfs(1)
    if count == N:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()