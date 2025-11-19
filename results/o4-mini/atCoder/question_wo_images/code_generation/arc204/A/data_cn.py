import sys
input = sys.stdin.readline

MOD = 998244353

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[j]: dict mapping from current C value to count of ways
# j = number of elements currently in Q (queue length)
# We process i from 0 to N (number of pushed elements)
# At each step, we can either push (if i < N) or pop (if j > 0)
# After 2N steps, i = N and j = 0

# To optimize memory, we keep dp as a list of dicts for j in [0..N]
# Initially dp[0][0] = 1
dp = [dict() for _ in range(N+1)]
dp[0][0] = 1

for i in range(N+1):
    ndp = [dict() for _ in range(N+1)]
    for j in range(N+1):
        if not dp[j]:
            continue
        for c, ways in dp[j].items():
            # Action 1: push i+1 (if i < N)
            if i < N:
                c1 = c - A[i]
                if c1 < 0:
                    c1 = 0
                # push i+1: j+1
                nd = ndp[j+1]
                nd[c1] = (nd.get(c1, 0) + ways) % MOD
            # Action 2: pop (if j > 0)
            if j > 0:
                # The first element in Q corresponds to some index x
                # But we don't track the order explicitly.
                # The problem states the queue is FIFO, and the order of pushed elements is 1..N
                # The first element in Q is the earliest pushed but not popped.
                # Since we process in order, the first pushed element not popped is i - j + 1
                x = i - j
                c2 = c + B[x]
                nd = ndp[j-1]
                nd[c2] = (nd.get(c2, 0) + ways) % MOD
    dp = ndp

# After all 2N operations, i = N, j = 0
# Sum dp[0][c] for c in [L, R]
ans = 0
for c, ways in dp[0].items():
    if L <= c <= R:
        ans = (ans + ways) % MOD

print(ans)