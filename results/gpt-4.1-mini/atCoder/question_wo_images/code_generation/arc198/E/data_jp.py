import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

def main():
    N, M = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))

    goal = 1 << N

    # dp[x]: number of ways to reach state x
    # We want dp[goal]
    # Initial state: dp[0] = 1
    # Transition:
    # For each x, for each s_i:
    #   next_x = (x | s_i) + 1
    #   if next_x <= goal:
    #       dp[next_x] += dp[x]

    # Since N can be up to 24, dp array size = 2^N + 1 = up to ~16 million
    # This is large but possibly feasible with efficient implementation and pruning.
    # However, we can optimize by noting that dp[x] = 0 for many x.
    # We'll use a dictionary to store only reachable states.

    from collections import defaultdict, deque

    dp = defaultdict(int)
    dp[0] = 1
    queue = deque([0])
    visited = set([0])

    while queue:
        x = queue.popleft()
        ways = dp[x]
        for s in S:
            nx = (x | s) + 1
            if nx > goal:
                continue
            if nx not in dp:
                queue.append(nx)
            dp[nx] = (dp[nx] + ways) % MOD

    print(dp[goal] % MOD)

if __name__ == "__main__":
    main()