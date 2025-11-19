import sys
from collections import deque

sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); index += 2
        edges = []
        adj = [[] for _ in range(n)]
        for i in range(m):
            u = int(data[index]); v = int(data[index+1]); index += 2
            u -= 1; v -= 1
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)

        if n <= 15 or m <= 40:
            dp = [dict() for _ in range(m+1)]
            init_state = tuple(0 for _ in range(n))
            dp[0][init_state] = True
            for i in range(m):
                for state in dp[i]:
                    state_list = list(state)
                    if state not in dp[i+1]:
                        dp[i+1][state] = False
                    u, v = edges[i]
                    if state_list[u] < 2 and state_list[v] < 2:
                        new_state_list = state_list[:]
                        new_state_list[u] += 1
                        new_state_list[v] += 1
                        new_state = tuple(new_state_list)
                        dp[i+1][new_state] = True
            best = 0
            for state in dp[m]:
                total_edges = sum(state) // 2
                if total_edges > best:
                    best = total_edges
            results.append(str(best))
        else:
            initial_degrees = [len(adj[i]) for i in range(n)]
            edges_sorted = sorted(edges, key=lambda e: initial_degrees[e[0]] + initial_degrees[e[1]], reverse=True)
            found = False
            max_k = min(m, n)
            for k in range(max_k, 0, -1):
                degrees = [0] * n
                if dfs(0, 0, degrees, k, edges_sorted, m):
                    results.append(str(k))
                    found = True
                    break
            if not found:
                results.append("0")
    print("\n".join(results))

def dfs(i, count, degrees, k, edges, m):
    if count == k:
        return True
    if i == m:
        return False
    cap = 0
    for d in degrees:
        if d < 2:
            cap += (2 - d)
    max_additional = min(m - i, cap // 2)
    if count + max_additional < k:
        return False
    if dfs(i+1, count, degrees, k, edges, m):
        return True
    u, v = edges[i]
    if degrees[u] < 2 and degrees[v] < 2:
        degrees[u] += 1
        degrees[v] += 1
        if dfs(i+1, count+1, degrees, k, edges, m):
            return True
        degrees[u] -= 1
        degrees[v] -= 1
    return False

if __name__ == "__main__":
    main()
