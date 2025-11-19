import sys
input = sys.stdin.readline

MOD = 998244353

def solve():
    n, m, d = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    # Holds positions per row
    holds = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                holds[i].append(j)

    # If bottom row has no holds, no routes
    if not holds[-1]:
        print(0)
        return

    # dp1[i][k]: number of ways to form routes on row i using exactly 1 hold (holds[i][k])
    # dp2[i][k]: number of ways to form routes on row i using exactly 2 holds (holds[i][k])
    # We'll store dp1 and dp2 as lists aligned with holds[i]

    dp1 = [0] * len(holds[-1])
    dp2 = [0] * len(holds[-1])
    # Base case: bottom row, one hold routes count as 1
    for idx in range(len(holds[-1])):
        dp1[idx] = 1

    # Precompute squared d for distance comparison
    d_sq = d * d

    # Process from bottom-1 row up to top row (i from n-2 down to 0)
    for i in range(n - 2, -1, -1):
        cur = holds[i]
        nxt = holds[i + 1]
        if not cur or not nxt:
            # If no holds in current or next row, no routes possible
            print(0)
            return

        # Prepare prefix sums for dp1 and dp2 of next row for fast range sum queries
        # We'll use two pointers to find reachable holds in next row for each hold in current row

        # dp1 and dp2 for next row
        dp1_nxt = dp1
        dp2_nxt = dp2

        # Prefix sums for dp1_nxt and dp2_nxt
        prefix_dp1 = [0] * (len(nxt) + 1)
        prefix_dp2 = [0] * (len(nxt) + 1)
        for idx in range(len(nxt)):
            prefix_dp1[idx + 1] = (prefix_dp1[idx] + dp1_nxt[idx]) % MOD
            prefix_dp2[idx + 1] = (prefix_dp2[idx] + dp2_nxt[idx]) % MOD

        # For each hold in current row, find indices in next row reachable within horizontal distance d
        # Since vertical distance is 1, distance^2 = 1 + (j_cur - j_nxt)^2 <= d^2
        # So |j_cur - j_nxt| <= sqrt(d^2 - 1)
        # If d=1, sqrt(d^2 -1) = 0, so only holds with same column reachable
        # If d=0, no moves possible (but d>=1 per constraints)
        # We'll compute max horizontal distance allowed:
        max_h_dist_sq = d_sq - 1
        if max_h_dist_sq < 0:
            # No moves possible between rows
            print(0)
            return
        import math
        max_h_dist = int(math.isqrt(max_h_dist_sq))

        # Two pointers for next row holds
        res_dp1 = [0] * len(cur)
        res_dp2 = [0] * len(cur)

        # For each hold in current row, find reachable holds in next row
        # nxt is sorted ascending, so we can binary search for left and right bounds
        from bisect import bisect_left, bisect_right

        for idx_cur, j_cur in enumerate(cur):
            left = bisect_left(nxt, j_cur - max_h_dist)
            right = bisect_right(nxt, j_cur + max_h_dist) - 1
            if left > right:
                # No reachable holds in next row
                continue

            # Sum dp2_nxt[left:right+1] and dp1_nxt[left:right+1]
            sum_dp2 = (prefix_dp2[right + 1] - prefix_dp2[left]) % MOD
            sum_dp1 = (prefix_dp1[right + 1] - prefix_dp1[left]) % MOD

            # dp1[i][idx_cur] = sum of dp2[i+1][reachable holds]
            res_dp1[idx_cur] = sum_dp2 % MOD

            # dp2[i][idx_cur] = sum of dp1[i][reachable holds] + sum of dp2[i+1][reachable holds] - dp1[i][idx_cur]
            # But dp1[i][reachable holds] is unknown yet, so we use the formula from problem:
            # dp2[i][j] = sum of dp1[i][reachable holds] + sum of dp2[i+1][reachable holds] - dp1[i][j]
            # We will compute dp2 after dp1 is fully computed for current row.

        # Now compute dp2 for current row
        # For dp2[i][idx_cur], we need sum of dp1[i][reachable holds] + sum_dp2 - dp1[i][idx_cur]
        # But dp1[i][reachable holds] is unknown yet, so we do a second pass.

        # To compute dp2, we need for each hold in current row:
        # sum of dp1[i][reachable holds] + sum of dp2[i+1][reachable holds] - dp1[i][idx_cur]

        # We'll build adjacency lists for current row holds to reachable holds in current row (for dp1 sums)
        # But dp1[i] is what we are computing now, so we cannot do that directly.

        # However, the problem states that at most two holds per level, and the route must use at least one hold per level.
        # The original code uses a trick with prefix sums to compute dp2.

        # We'll replicate the original approach with prefix sums for dp1 and dp2 on current row.

        # First, compute prefix sums of res_dp1 (which is dp1[i]) for current row
        prefix_res_dp1 = [0] * (len(cur) + 1)
        for idx in range(len(cur)):
            prefix_res_dp1[idx + 1] = (prefix_res_dp1[idx] + res_dp1[idx]) % MOD

        # For dp2[i][idx_cur], sum dp1[i][reachable holds] + sum dp2[i+1][reachable holds] - dp1[i][idx_cur]
        # sum dp1[i][reachable holds] can be computed similarly by bisect on cur holds

        # For each hold in current row, find reachable holds in current row within distance d horizontally (distance vertically is 0)
        # Distance between holds in same row: sqrt(0 + (j1 - j2)^2) <= d => |j1 - j2| <= d

        # We'll precompute for each hold in current row the indices of reachable holds in current row

        # Use bisect again
        dp2_res = [0] * len(cur)
        for idx_cur, j_cur in enumerate(cur):
            left = bisect_left(cur, j_cur - d)
            right = bisect_right(cur, j_cur + d) - 1
            if left > right:
                # No reachable holds in current row (should not happen since at least itself)
                dp2_res[idx_cur] = (res_dp1[idx_cur] + 0 - res_dp1[idx_cur]) % MOD
                continue
            sum_dp1_cur = (prefix_res_dp1[right + 1] - prefix_res_dp1[left]) % MOD

            # sum_dp2 from next row reachable holds already computed as sum_dp2 above for idx_cur
            # We need to recompute sum_dp2 for each idx_cur again:
            left_nxt = bisect_left(nxt, j_cur - max_h_dist)
            right_nxt = bisect_right(nxt, j_cur + max_h_dist) - 1
            sum_dp2_nxt = 0
            if left_nxt <= right_nxt:
                sum_dp2_nxt = (prefix_dp2[right_nxt + 1] - prefix_dp2[left_nxt]) % MOD

            dp2_res[idx_cur] = (sum_dp1_cur + sum_dp2_nxt - res_dp1[idx_cur]) % MOD

        dp1 = res_dp1
        dp2 = dp2_res

    # Result is sum of dp2 on top row
    ans = sum(dp2) % MOD
    print(ans)


t = int(input())
for _ in range(t):
    solve()