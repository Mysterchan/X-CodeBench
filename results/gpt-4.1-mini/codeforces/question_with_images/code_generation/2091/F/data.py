import sys
import math
input = sys.stdin.readline

MOD = 998244353

# Explanation of approach:
# We have n rows (levels), m columns (segments).
# Each cell can have a hold or not.
# We want to count the number of valid routes from bottom row (n-th) to top row (1st),
# moving only upwards or staying on the same row (not going down),
# using 1 or 2 holds per level,
# and the distance between consecutive holds <= d.
#
# Key observations:
# - The route must include at least one hold per level.
# - At most two holds per level.
# - The order of holds in the route matters.
# - The route starts at bottom row and ends at top row.
# - Moves are from holds in row i to holds in row i-1 or same row i (not lower).
#   But since route must have at least one hold per level and strictly non-lower,
#   the route must go from bottom to top, level by level.
#
# The problem is to count sequences of holds h_n, h_{n-1}, ..., h_1,
# where h_i is a set of 1 or 2 holds in row i,
# and for each consecutive pair of holds in the route,
# the Euclidean distance between holds is <= d.
#
# Because at most two holds per level, and at least one hold per level,
# the number of possible hold subsets per level is small:
# - If row i has k holds, number of subsets of size 1 or 2 is k + k*(k-1)/2.
#
# We can model the problem as a DP over levels:
# For each subset of holds in row i (size 1 or 2),
# dp[i][subset] = number of ways to form valid partial routes from bottom row n up to row i,
# ending with the subset of holds in row i.
#
# Transitions:
# For each subset s_i in row i,
# dp[i][s_i] = sum over subsets s_{i+1} in row i+1 of dp[i+1][s_{i+1}],
# if s_i and s_{i+1} are "compatible":
# meaning every hold in s_i can be reached from some hold in s_{i+1} within distance d,
# and every hold in s_{i+1} can reach some hold in s_i within distance d.
#
# Because the route is a sequence of distinct holds,
# and holds are distinct cells, and we never go down,
# and we pick subsets per level,
# the distinctness is guaranteed by choosing distinct holds per level.
#
# Finally, answer = sum of dp[1][subset] over all subsets in top row.
#
# Implementation details:
# - We'll store holds per row as a list of (row, col).
# - For each row, generate all subsets of size 1 or 2.
# - Precompute adjacency between subsets of consecutive rows.
# - Use DP from bottom to top.
#
# Complexity:
# - Number of holds per row can be large, but since sum n*m <= 4*10^6,
#   and we only consider subsets of size 1 or 2,
#   and we only connect subsets if holds are within distance d,
#   we must optimize adjacency checks.
#
# Optimization:
# - For each hold in row i, find holds in row i-1 within distance d.
# - For subsets, check if subsets are compatible by checking holds adjacency.
#
# We'll implement a two-pointer or binary search approach to find holds within distance d,
# since rows are horizontal lines, distance in row dimension is 1,
# so distance^2 = (i1 - i2)^2 + (j1 - j2)^2 <= d^2.
# Since i1 and i2 differ by 1 (adjacent rows), max vertical distance = 1,
# so horizontal distance must satisfy (j1 - j2)^2 <= d^2 - 1.
#
# So for each hold in row i, we find holds in row i-1 with column in [j - hdist, j + hdist],
# where hdist = floor(sqrt(d^2 - 1)) if d >= 1 else 0.
#
# This reduces adjacency search to interval queries.
#
# We'll implement this carefully.

def main():
    t = int(input())
    for _ in range(t):
        n, m, d = map(int, input().split())
        grid = [input().strip() for __ in range(n)]

        # Holds per row: list of columns where holds exist
        # Rows are from top (0) to bottom (n-1)
        holds = []
        for i in range(n):
            row_holds = []
            for j in range(m):
                if grid[i][j] == 'X':
                    row_holds.append(j)
            holds.append(row_holds)

        # If bottom row has no holds, no routes
        if not holds[-1]:
            print(0)
            continue

        # Precompute subsets per row: subsets of size 1 or 2
        # Each subset represented as tuple of indices in holds[row]
        # We'll store subsets as tuples of hold indices (not columns)
        subsets = []
        for r in range(n):
            hs = holds[r]
            subs = []
            k = len(hs)
            # subsets of size 1
            for i1 in range(k):
                subs.append((i1,))
            # subsets of size 2
            for i1 in range(k):
                for i2 in range(i1+1, k):
                    subs.append((i1,i2))
            subsets.append(subs)

        # If any row has no holds, no routes
        if any(len(holds[r]) == 0 for r in range(n)):
            print(0)
            continue

        # Precompute adjacency between holds in consecutive rows
        # For each hold in row i, find holds in row i-1 within distance d
        # Distance between (i,j1) and (i-1,j2) = sqrt(1 + (j1-j2)^2) <= d
        # So (j1-j2)^2 <= d^2 - 1
        # If d < 1, no moves possible between rows
        # For d >= 1, hdist = floor(sqrt(d^2 - 1))
        # We'll build for each row i (from bottom-1 to top),
        # a list of reachable holds in row i-1 for each hold in row i

        d_sq = d*d
        if d < 1:
            # No moves possible between rows
            # So no routes if n>1
            if n > 1:
                print(0)
                continue
            else:
                # n=1, just count subsets of bottom row
                # But route must start bottom and end top (same row)
                # So answer = number of subsets of bottom row
                # which is number of subsets of size 1 or 2
                print(len(subsets[0]) % MOD)
                continue

        hdist = int(math.isqrt(max(0, d_sq - 1)))

        # For each row i from bottom-1 to top (i from n-1 down to 1),
        # build adjacency from holds in row i to holds in row i-1
        # We'll store for each hold in row i, the list of holds in row i-1 reachable

        # To speed up, holds in each row are sorted by column
        # holds[r] is sorted by construction

        adj_holds = [None]*(n)
        # adj_holds[i][h_i] = list of holds in row i-1 reachable from hold h_i in row i
        # For i=0 (top row), no previous row
        adj_holds[0] = []
        for i in range(1,n):
            prev_row = holds[i-1]
            cur_row = holds[i]
            adj = [[] for _ in range(len(cur_row))]
            # For each hold in cur_row, find holds in prev_row with column in [c - hdist, c + hdist]
            # Use two pointers to find range in prev_row
            # prev_row is sorted
            for idx_cur, c_cur in enumerate(cur_row):
                left = c_cur - hdist
                right = c_cur + hdist
                # binary search left bound
                l = 0
                r = len(prev_row)
                while l < r:
                    mid = (l+r)//2
                    if prev_row[mid] < left:
                        l = mid+1
                    else:
                        r = mid
                start = l
                # binary search right bound
                l = 0
                r = len(prev_row)
                while l < r:
                    mid = (l+r)//2
                    if prev_row[mid] <= right:
                        l = mid+1
                    else:
                        r = mid
                end = l
                # holds in prev_row[start:end] are candidates
                # check exact distance (though vertical distance is 1, horizontal within range)
                for idx_prev in range(start, end):
                    # distance squared = 1 + (c_cur - prev_row[idx_prev])^2 <= d^2 guaranteed by range
                    # so no need to check again
                    adj[idx_cur].append(idx_prev)
            adj_holds[i] = adj

        # Now we have holds and adjacency between holds in consecutive rows
        # Next, build adjacency between subsets of consecutive rows
        # subsets[i] = list of subsets in row i, each subset is tuple of hold indices
        # We want to know for each subset s_i in row i,
        # which subsets s_{i-1} in row i-1 are reachable from s_i
        # i.e. for each hold in s_i, there is at least one hold in s_{i-1} reachable,
        # and for each hold in s_{i-1}, there is at least one hold in s_i reachable.
        #
        # We'll build a bipartite graph between holds in row i and row i-1:
        # edges from holds in row i to holds in row i-1 given by adj_holds[i]
        #
        # For each pair of subsets (s_i, s_{i-1}), check compatibility:
        # - For each hold in s_i, exists hold in s_{i-1} reachable from it (adj_holds[i])
        # - For each hold in s_{i-1}, exists hold in s_i that can reach it (reverse adjacency)
        #
        # To speed up:
        # For each hold in row i-1, build reverse adjacency: holds in row i that can reach it
        # Then for subsets, check conditions quickly.

        # Precompute reverse adjacency for each row i (except top)
        rev_adj_holds = [None]*n
        rev_adj_holds[0] = []
        for i in range(1,n):
            size_prev = len(holds[i-1])
            size_cur = len(holds[i])
            rev_adj = [[] for _ in range(size_prev)]
            for h_cur in range(size_cur):
                for h_prev in adj_holds[i][h_cur]:
                    rev_adj[h_prev].append(h_cur)
            rev_adj_holds[i] = rev_adj

        # For DP:
        # dp[i][subset_index] = number of routes from bottom row n to row i ending with subsets[i][subset_index]
        # We'll do bottom-up from i = n-1 (bottom row) to i=0 (top row)
        # Base case: dp[n-1][*] = 1 for all subsets in bottom row (since route starts there)
        # Transition:
        # dp[i-1][s_prev] += sum of dp[i][s_cur] over s_cur compatible with s_prev

        # To speed up compatibility checks, we precompute for each row i (from bottom to top-1),
        # for each subset s_prev in row i-1,
        # the list of subsets s_cur in row i that are compatible.

        # We'll build a compatibility graph from subsets[i-1] to subsets[i]

        # To check compatibility between subsets s_prev (row i-1) and s_cur (row i):
        # s_prev: holds indices in row i-1
        # s_cur: holds indices in row i
        #
        # Conditions:
        # 1) For each hold in s_cur, exists hold in s_prev reachable from it (adj_holds[i])
        # 2) For each hold in s_prev, exists hold in s_cur that can reach it (rev_adj_holds[i])
        #
        # We'll implement a function to check compatibility.

        def compatible(i, s_prev, s_cur):
            # i: current row index (row i)
            # s_prev: subset in row i-1 (tuple of hold indices)
            # s_cur: subset in row i (tuple of hold indices)
            # Check conditions:
            # For each hold in s_cur, check if any hold in s_prev is reachable from it
            # For each hold in s_prev, check if any hold in s_cur can reach it

            # For holds in s_cur:
            for h_cur in s_cur:
                # adj_holds[i][h_cur] = holds in row i-1 reachable from h_cur
                reachable_prev = adj_holds[i][h_cur]
                # Check intersection with s_prev
                found = False
                for h_p in s_prev:
                    # binary search since s_prev is small (size 1 or 2)
                    if h_p in reachable_prev:
                        found = True
                        break
                if not found:
                    return False

            # For holds in s_prev:
            for h_prev in s_prev:
                # rev_adj_holds[i][h_prev] = holds in row i reachable to h_prev
                reachable_cur = rev_adj_holds[i][h_prev]
                found = False
                for h_c in s_cur:
                    if h_c in reachable_cur:
                        found = True
                        break
                if not found:
                    return False

            return True

        # To speed up membership checks, convert adj_holds[i][h_cur] and rev_adj_holds[i][h_prev] to sets
        for i in range(1,n):
            for h_cur in range(len(adj_holds[i])):
                adj_holds[i][h_cur] = set(adj_holds[i][h_cur])
            for h_prev in range(len(rev_adj_holds[i])):
                rev_adj_holds[i][h_prev] = set(rev_adj_holds[i][h_prev])

        # Precompute compatibility graph:
        # For each i in [1..n-1], build graph from subsets[i-1] to subsets[i]
        # edges[i-1][idx_prev] = list of idx_cur compatible subsets
        edges = [None]*(n-1)
        for i in range(1,n):
            subs_prev = subsets[i-1]
            subs_cur = subsets[i]
            edges_i = [[] for _ in range(len(subs_prev))]
            # For each pair (s_prev, s_cur), check compatibility
            # Since subsets are small (size 1 or 2), and number of subsets per row can be large,
            # we try to prune by indexing subsets by holds for faster checks.

            # We'll just brute force here, hoping it passes due to constraints and pruning.

            # To speed up, we can index subsets by holds for quick filtering:
            # For each hold in row i-1, which subsets contain it?
            # For each hold in row i, which subsets contain it?

            # But let's try brute force first.

            for idx_prev, s_prev in enumerate(subs_prev):
                for idx_cur, s_cur in enumerate(subs_cur):
                    if compatible(i, s_prev, s_cur):
                        edges_i[idx_prev].append(idx_cur)
            edges[i-1] = edges_i

        # DP arrays
        # dp[i][subset_index]: number of routes from bottom row n to row i ending with subsets[i][subset_index]
        # We'll do bottom-up from bottom row (n-1) to top row (0)
        dp = [None]*n
        dp[n-1] = [1]*len(subsets[n-1])  # base case: bottom row subsets count = 1

        for i in range(n-2, -1, -1):
            dp[i] = [0]*len(subsets[i])
            edges_i = edges[i]
            dp_next = dp[i+1]
            for idx_prev in range(len(subsets[i])):
                s = 0
                for idx_cur in edges_i[idx_prev]:
                    s += dp_next[idx_cur]
                dp[i][idx_prev] = s % MOD

        # Answer = sum of dp[0][*] (top row subsets)
        ans = sum(dp[0]) % MOD
        print(ans)

if __name__ == "__main__":
    main()