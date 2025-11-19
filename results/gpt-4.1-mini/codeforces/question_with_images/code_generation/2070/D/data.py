import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    parents = list(map(int, input().split()))
    
    # Build adjacency list
    children = [[] for _ in range(n+1)]
    for i, p in enumerate(parents, start=2):
        children[p].append(i)
    
    # dp[v] = number of valid sequences starting at v (including just [v])
    # For leaves dp[v] = 1 (only the sequence [v])
    # For internal nodes:
    # dp[v] = product over children c of (1 + dp[c])
    # Explanation:
    # - We can choose to include or not include sequences from each child's subtree
    # - The +1 accounts for the option to skip that child's subtree
    # - Multiplying because choices for different children are independent
    
    dp = [0]*(n+1)
    
    def dfs(v):
        res = 1
        for c in children[v]:
            dfs(c)
            res = (res * (1 + dp[c])) % MOD
        dp[v] = res
    
    dfs(1)
    print(dp[1] % MOD)