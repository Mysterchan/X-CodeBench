import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    # 建樹
    children = [[] for __ in range(n+1)]
    for i, par in enumerate(p, start=2):
        children[par].append(i)

    # dp[u]: 有效序列數量，以u為根的子樹中可選擇的序列數（包含空序列）
    # 根節點1的答案是dp[1]-1（去掉空序列）
    def dfs(u):
        res = 1
        for c in children[u]:
            res = res * (dfs(c) + 1) % MOD
        return res

    ans = dfs(1) - 1
    if ans < 0:
        ans += MOD
    print(ans)