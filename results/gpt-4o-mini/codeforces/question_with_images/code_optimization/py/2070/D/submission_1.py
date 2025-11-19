import sys
from collections import defaultdict, deque

def input():
    return sys.stdin.readline().strip()

mod = 998244353

def solve():
    n = int(input())
    parents = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(n - 1):
        graph[parents[i]].append(i + 2)

    dp = [1] * (n + 1)
    level_size = [0] * (n + 1)

    # BFS to count the number of nodes in each level
    queue = deque([1])
    while queue:
        node = queue.popleft()
        level_size[len(queue) + 1] += 1  # Record the level size
        for neb in graph[node]:
            queue.append(neb)

    total_valid_sequences = 1  # Start with the sequence consisting only of root (1)

    # Calculate valid sequences at each level
    for level in range(1, n + 1):
        if level_size[level] == 0:
            break
        total_valid_sequences = total_valid_sequences * pow(level_size[level], dp[level - 1], mod) % mod

    print(total_valid_sequences)

t = int(input())
for _ in range(t):
    solve()