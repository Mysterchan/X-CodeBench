import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(u):
    total = 0
    odd_count = 0
    for v in g[u]:
        m, s = dfs(v)
        total += s
        odd_count += m
    # If odd_count is even, we can pair all odd subtrees
    # If odd_count is odd, one subtree remains unpaired
    pairs = odd_count - (odd_count & 1)
    return (pairs, total + 1)

T = int(input())
for _ in range(T):
    n = int(input())
    parents = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for i, p in enumerate(parents, 2):
        g[p].append(i)
    res, _ = dfs(1)
    print((n - res) >> 1)