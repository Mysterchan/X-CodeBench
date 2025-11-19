import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    N, L, R = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    # dp[i][j] = dict: key = current C, value = count of ways
    # i = number of push operations done (1-based indexing for i)
    # j = number of pop operations done
    # We must have j <= i always (queue can't be empty when popping)
    # At the end, i = N, j = N, total 2N operations done.

    # To optimize memory and speed, we use two arrays of dicts:
    # dp[j]: dict of C -> count for fixed i and j
    # We'll iterate i from 0 to N, and for each i, j from 0 to i

    from collections import defaultdict

    dp_prev = [defaultdict(int) for _ in range(N+1)]
    dp_prev[0][0] = 1  # start: no push, no pop, C=0

    for i in range(N):
        dp_curr = [defaultdict(int) for _ in range(N+1)]
        a = A[i]
        b = B[i]
        for j in range(i+1):
            d = dp_prev[j]
            if not d:
                continue
            # For each state (C, count)
            for c_val, ways in d.items():
                # Action 1: push i+1
                # i+1-th push: i is zero-based, so push index = i+1
                # C' = max(0, c - A[i])
                c1 = c_val - a
                if c1 < 0:
                    c1 = 0
                dp_curr[j][c1] = (dp_curr[j][c1] + ways) % MOD

                # Action 2: pop front if j < i+1 (queue not empty)
                if j < i+1:
                    c2 = c_val + b
                    dp_curr[j+1][c2] = (dp_curr[j+1][c2] + ways) % MOD
        dp_prev = dp_curr

    # After all N pushes, we must do N pops to empty the queue
    # So final dp is dp_prev[N], keys are possible C values after all pops
    ans = 0
    for c_val, ways in dp_prev[N].items():
        if L <= c_val <= R:
            ans = (ans + ways) % MOD

    print(ans)

threading.Thread(target=main).start()