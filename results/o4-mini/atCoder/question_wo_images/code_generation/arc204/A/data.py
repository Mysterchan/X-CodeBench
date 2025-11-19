import sys
input = sys.stdin.readline

MOD = 998244353

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# The problem is a classic DP with a stack-like structure Q.
# We perform 2N operations:
# - Action 1: push i into Q, C = max(0, C - A[i]), i++
# - Action 2: pop from Q front, C += B[x]
# We want the number of ways to perform these 2N operations so that final C in [L,R].

# Key observations:
# - The sequence of operations corresponds to a valid parenthesis sequence:
#   Action 1 = push (open), Action 2 = pop (close)
# - At any point, number of Action 1 performed >= number of Action 2 performed.
# - After 2N operations, all pushed elements are popped.
# - The order of popping is FIFO (queue), so the order of popping is fixed by the order of pushing.
# - We want to count the number of valid sequences of push/pop with the given constraints on C.

# DP state:
# dp[i][j][c] = number of ways after performing i pushes and j pops,
# with current C = c.
# But c can be large (sum B up to 5000*5000=25,000,000), too large for direct DP.

# Optimization:
# - C is always >= 0.
# - After push: C = max(0, C - A[i])
# - After pop: C = C + B[x], where x is the oldest pushed element not popped yet.
# The order of popped elements is fixed by the queue order.

# We can use a 2D DP with a compressed dimension for C using a dictionary or sparse representation.
# But that would be too slow for N=5000.

# Further optimization:
# - The problem is from AtCoder DP contest style.
# - We can use a 2D DP with a compressed dimension for C using a Fenwick tree or segment tree.
# But still complicated.

# Alternative approach:
# Since the queue is FIFO, the order of popped elements is fixed.
# The sequence of operations corresponds to a Dyck path of length 2N.
# The order of popped elements is fixed: first pushed is first popped.

# Let's define dp[i][j][c] as number of ways after i pushes and j pops with current C = c.
# i >= j, i,j in [0..N]
# At each step:
# - If i < N, can push: c' = max(0, c - A[i])
# - If j < i, can pop: c' = c + B[j]

# We can implement dp with rolling arrays and compress c dimension using a dictionary.

# Implementation details:
# - Use two arrays dp and next_dp: dp[c] = count
# - For each state (i,j), we keep dp for all c.
# - For push: dp_next[c'] += dp[c]
# - For pop: dp_next[c'] += dp[c]

# Since c can be large, we use dict to store only reachable c.

# Complexity:
# - Worst case O(N^2 * number_of_c_states)
# - But pruning and max(0, c - A[i]) reduces states.

from collections import defaultdict

dp = [defaultdict(int) for _ in range(N+1)]
# dp[j]: dict mapping c -> ways after i pushes and j pops
# We will iterate i from 0 to N
# For each i, we update dp for j in [0..i]

dp[0][0] = 1  # 0 pushes, 0 pops, C=0

for i in range(N):
    next_dp = [defaultdict(int) for _ in range(N+1)]
    for j in range(i+1):
        cur = dp[j]
        if not cur:
            continue
        # Action 1: push i-th element (0-based)
        # c' = max(0, c - A[i])
        for c, ways in cur.items():
            c_push = c - A[i]
            if c_push < 0:
                c_push = 0
            next_dp[j][c_push] = (next_dp[j][c_push] + ways) % MOD
        # Action 2: pop if j < i
        if j < i:
            for c, ways in cur.items():
                c_pop = c + B[j]
                next_dp[j+1][c_pop] = (next_dp[j+1][c_pop] + ways) % MOD
    dp = next_dp

# After all pushes done (i = N), we must pop all remaining elements
# So we do pops until j = N
for j in range(N):
    cur = dp[j]
    next_dp = defaultdict(int)
    for c, ways in cur.items():
        c_pop = c + B[j]
        next_dp[c_pop] = (next_dp[c_pop] + ways) % MOD
    dp[j+1] = next_dp

# Now dp[N] contains ways with all pushes and pops done
# Sum ways with c in [L,R]
ans = 0
for c, ways in dp[N].items():
    if L <= c <= R:
        ans = (ans + ways) % MOD

print(ans)