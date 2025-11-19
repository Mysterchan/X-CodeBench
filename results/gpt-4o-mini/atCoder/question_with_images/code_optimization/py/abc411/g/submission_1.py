N, M = map(int, input().split())
mod = 998244353

graph = [[0] * N for _ in range(N)]
for _ in range(M):
    U, V = map(lambda x: int(x) - 1, input().split())
    graph[U][V] += 1
    graph[V][U] += 1

ans = 0

# Counting cycles in the graph
for s in range(2, N + 1):
    DP = [[0] * s for _ in range(1 << s)]
    DP[1 << (s - 1)][s - 1] = 1
    
    for bit in range(1 << s):
        for i in range(s):
            if (bit >> i) & 1:
                for j in range(s):
                    if (bit >> j) & 1:
                        continue
                    DP[bit | (1 << j)][j] += DP[bit][i] * graph[i][j]
                    DP[bit | (1 << j)][j] %= mod
    
    for i in range(s):
        DP[(1 << s) - 1][i] -= graph[i][s - 1]
    
    for bit in range(1 << s):
        for i in range(s):
            if (bit >> i) & 1:
                ans += DP[bit][i] * graph[i][s - 1]
                ans %= mod

ans = (ans * pow(2, mod - 2, mod)) % mod

# Remove double counting edges
for i in range(N):
    for j in range(i + 1, N):
        ans = (ans + graph[i][j] * (graph[i][j] - 1) // 2) % mod

print(ans)