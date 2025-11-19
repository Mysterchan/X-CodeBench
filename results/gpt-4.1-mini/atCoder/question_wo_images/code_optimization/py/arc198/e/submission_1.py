MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = list(map(int, input().split()))

    MAX = 1 << N
    dp = [0] * (MAX + 1)
    dp[0] = 1

    # Precompute for each s the offset = s + 1
    offsets = [s + 1 for s in S]

    # Process dp in order, for each x, add dp[x] to dp[(x|s)+1]
    # To speed up, we process dp in order and for each s, update dp[(x|s)+1]
    # Since dp[x] can be zero, skip zeros

    # To optimize, we can process dp in order and for each s, update dp[(x|s)+1]
    # But this is still O(MAX*M), so we try to optimize by grouping by s

    # Instead, we process dp in order and for each s, update dp[(x|s)+1]
    # But we can try to process dp in order and for each s, update dp[(x|s)+1]
    # This is the best we can do given constraints.

    # Use local variables for speed
    dp_append = dp.__setitem__
    dp_get = dp.__getitem__

    for x in range(MAX):
        val = dp_get(x)
        if val == 0:
            continue
        for off in offsets:
            nx = (x | (off - 1)) + 1
            if nx <= MAX:
                dp[nx] = (dp[nx] + val) % MOD

    print(dp[MAX] % MOD)

if __name__ == "__main__":
    main()