import sys
input = sys.stdin.readline
mod = 998244353

def solve():
    n = int(input())
    parents = list(map(int, input().split()))
    
    # Build adjacency list
    graph = [[] for _ in range(n+1)]
    for i, p in enumerate(parents, start=2):
        graph[p].append(i)
    
    # BFS to get nodes by level
    from collections import deque
    queue = deque([1])
    levels = []
    while queue:
        size = len(queue)
        level_nodes = []
        for _ in range(size):
            node = queue.popleft()
            level_nodes.append(node)
            for child in graph[node]:
                queue.append(child)
        levels.append(level_nodes)
    
    dp = [1]*(n+1)
    # Precompute sum of dp for next level once per level
    for i in range(len(levels)-2, -1, -1):
        next_level = levels[i+1]
        s = 0
        for node in next_level:
            s += dp[node]
        s %= mod
        for node in levels[i]:
            val = (dp[node] + s) % mod
            for child in graph[node]:
                val -= dp[child]
            dp[node] = val % mod
    
    # The answer is sum of dp of last level + 1 (empty sequence)
    # But last level dp sum is s from last iteration or recompute
    # To avoid recomputing, just sum dp of last level
    last_level = levels[-1]
    ans = 0
    for node in last_level:
        ans += dp[node]
    ans %= mod
    print((ans + 1) % mod)

t = int(input())
for _ in range(t):
    solve()