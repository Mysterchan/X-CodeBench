import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

def main():
    N, M = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))
    S_set = set(S)

    # We want to count ways to reach x = 2^N starting from x=0,
    # with transitions: x -> (x OR s_i) + 1 for any s_i in S.

    # Since x can go up to 2^N, but 2^N can be large (up to ~16 million),
    # we need an efficient method.

    # Key observations:
    # - x increases strictly by at least 1 each step (since +1).
    # - x can never exceed 2^N.
    # - We want dp[x] = number of ways to reach 2^N from x.
    # - dp[2^N] = 1 (base case).
    # - For x < 2^N:
    #   dp[x] = sum over s_i of dp[(x OR s_i) + 1] if (x OR s_i) + 1 <= 2^N.

    # We will compute dp from high to low (bottom-up):
    # dp[2^N] = 1
    # for x in [2^N-1 .. 0]:
    #   dp[x] = sum dp[(x OR s_i) + 1]

    # To optimize:
    # - Precompute dp array of size 2^N + 1 (max 16 million + 1).
    # - For each x, sum over M s_i transitions.
    # - M can be up to 2*10^5, so naive O(2^N * M) is too large.

    # Optimization:
    # - For each x, dp[x] depends on dp[(x OR s_i) + 1].
    # - We can try to process dp in decreasing order of x.
    # - For each s_i, we can update dp[x] from dp[(x OR s_i) + 1].
    # - But still O(2^N * M) is too large.

    # Alternative approach:
    # Since dp[x] depends on dp[(x OR s_i) + 1], and (x OR s_i) >= x,
    # the next state is always >= x + 1.
    # So dp[x] depends on dp[y] with y > x.
    # So we can process dp from high to low.

    # We can try to use a "meet in the middle" or bitset approach,
    # but here we can try to use a "sparse" approach:
    # Only states reachable from 0 matter.

    # BFS approach:
    # - Start from x=0, dp[0] = 1
    # - For each state in queue:
    #   For each s_i:
    #     nx = (x OR s_i) + 1
    #     if nx <= 2^N:
    #       dp[nx] += dp[x]
    #       if nx not visited:
    #         add nx to queue

    # This BFS approach counts ways from 0 to 2^N, but we want number of ways to reach 2^N from 0.
    # This is a forward DP.

    # Implement BFS with dp array and queue.

    from collections import deque

    limit = 1 << N
    dp = [0] * (limit + 1)
    dp[0] = 1
    visited = [False] * (limit + 1)
    visited[0] = True
    queue = deque([0])

    while queue:
        x = queue.popleft()
        ways = dp[x]
        for s in S:
            nx = (x | s) + 1
            if nx <= limit:
                if not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
                dp[nx] = (dp[nx] + ways) % MOD

    print(dp[limit] % MOD)

if __name__ == "__main__":
    main()