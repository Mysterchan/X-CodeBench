from collections import defaultdict, deque

MOD = 998244353

N, M = map(int, input().split())
S = list(map(int, input().split()))
target = 1 << N

dp = defaultdict(int)
dp[0] = 1
queue = deque()
queue.append(0)

while queue:
    x = queue.popleft()
    for s in S:
        nx = (x | s) + 1
        if nx > target:
            continue
        dp[nx] = (dp[nx] + dp[x]) % MOD
        queue.append(nx)

print(dp[target] % MOD)