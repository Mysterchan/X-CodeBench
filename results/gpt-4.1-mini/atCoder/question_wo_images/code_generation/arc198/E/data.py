import sys
input = sys.stdin.readline

MOD = 998244353

def main():
    N, M = map(int, input().split())
    s = list(map(int, input().split()))

    # We want to count ways to reach x = 2^N starting from x=0,
    # with transitions: x -> (x OR s_i) + 1 for some i.

    # The maximum x we consider is 2^N.
    # dp[x] = number of ways to reach x.
    # dp[0] = 1 (start)
    # For each x < 2^N, for each s_i:
    #   y = (x | s_i) + 1
    #   if y <= 2^N:
    #       dp[y] += dp[x]

    # Naive approach is O(M * 2^N), which is too large for N=24 and M up to 2e5.

    # Optimization:
    # We only need dp for x in [0, 2^N].
    # We can process dp in increasing order of x.
    # For each x, we try all s_i:
    #   y = (x | s_i) + 1
    #   if y <= 2^N:
    #       dp[y] += dp[x]

    # But M can be large, so iterating all s_i for each x is too slow.

    # Key insight:
    # For fixed s_i, the transition is monotone in x:
    #   y = (x | s_i) + 1
    # For fixed s_i, if x1 < x2, then (x1 | s_i) <= (x2 | s_i),
    # so y1 <= y2.

    # We can try to group states by their OR with s_i.

    # Another approach:
    # Since dp[x] depends only on dp of smaller x,
    # and transitions are monotone increasing,
    # we can use a BFS-like approach or a queue.

    # But still, M is large.

    # Alternative approach:
    # We can use a "meet in the middle" or bitset DP approach.

    # However, since s_i are sorted and distinct,
    # and s_i < 2^N,
    # we can try to use a map from s_i to indices.

    # Let's try a different approach:
    # We can precompute for each s_i the set of x that can reach y = (x | s_i) + 1.

    # But this is complicated.

    # Let's try to implement the straightforward DP with pruning and fast I/O,
    # and see if it passes.

    MAX = 1 << N
    dp = [0] * (MAX + 1)
    dp[0] = 1

    # To speed up, we can precompute for each s_i the list of y reachable from x.
    # But that is the same as the transition.

    # We will process dp in increasing order of x.
    # For each x, if dp[x] > 0:
    #   For each s_i:
    #       y = (x | s_i) + 1
    #       if y <= MAX:
    #           dp[y] += dp[x]

    # This is O(M * 2^N) worst case, but we can try to prune.

    # Since M can be large, we can try to use a dictionary to store dp states,
    # but that might be slower.

    # Let's try to implement the straightforward DP with some pruning.

    # To speed up, we can note that for fixed x,
    # (x | s_i) is at least s_i,
    # so (x | s_i) + 1 >= s_i + 1,
    # so y >= s_i + 1.

    # We can try to binary search s_i to skip those s_i where s_i + 1 > MAX.

    # But s_i < MAX, so s_i + 1 <= MAX always.

    # Let's implement the straightforward DP and rely on fast I/O and efficient code.

    # To speed up, we can convert s to a list and use local variables.

    s_arr = s
    dp_arr = dp

    for x in range(MAX):
        ways = dp_arr[x]
        if ways == 0:
            continue
        for si in s_arr:
            y = (x | si) + 1
            if y > MAX:
                continue
            dp_arr[y] = (dp_arr[y] + ways) % MOD

    print(dp_arr[MAX] % MOD)

if __name__ == "__main__":
    main()