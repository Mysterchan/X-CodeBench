import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    visited = [False] * N
    cycles = []
    for i in range(N):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = P[j]
            cycles.append(cycle)

    # Precompute MEX for pairs
    # MEX(x,y) = smallest non-negative integer not in {x,y}
    # Possible pairs (x,y) in {0,1,2}:
    # (0,0)=1, (0,1)=2, (0,2)=1, (1,1)=0, (1,2)=0, (2,2)=0
    # MEX is symmetric
    def mex(x,y):
        if x == y:
            return 0 if x != 0 else 1
        s = {x,y}
        for m in range(3):
            if m not in s:
                return m

    # For each cycle, we want to find the maximum score achievable for each possible count of 0s and 1s assigned in that cycle.
    # The cycle length can be large, so brute force over 3^m is impossible.
    # But since values are only 0,1,2 and MEX values are small, we can model the problem as a max weight assignment on a cycle with 3 states per node.
    # The score is sum over edges of MEX(B_i, B_{P_i}), where edges form a cycle.
    # We want to assign values to nodes with counts of 0,1,2 fixed per query, but queries differ.
    # So we precompute for each cycle a DP that for each possible (a0,a1) (number of zeros and ones assigned in that cycle), gives max score achievable.
    # Then combine cycles by knapsack-like DP.

    # To optimize:
    # For each cycle, we do DP over the cycle with states:
    # For each position, we try all 3 colors.
    # We keep track of counts of 0 and 1 assigned so far.
    # Since cycle length can be large, we use a DP with dimension (pos, first_color, prev_color, a0, a1)
    # But this is too big.
    #
    # Instead, we use the fact that the cycle is a ring and colors are from {0,1,2}.
    # We fix the color of the first node and do DP over the rest.
    # For each fixed first color, we do DP over positions 1..m-1:
    # dp[pos][prev_color][a0][a1] = max score
    #
    # At the end, we connect last node to first node to add last edge score.
    #
    # This reduces complexity to O(m * 3 * 3 * (m+1)^2) which is still large for big m.
    #
    # But sum of cycle lengths = N, and we have to do this for all cycles.
    #
    # To optimize further:
    # Since colors are only 3, and counts sum to m, we can store dp as dict keyed by (a0,a1) for each pos and prev_color.
    #
    # We'll implement this approach.

    contribs = []

    for cyc in cycles:
        m = len(cyc)
        # dp_first_color[color] = dict with key=(a0,a1), value=max_score
        # We'll compute for each possible first_color in {0,1,2}
        dp_first_color = [{} for _ in range(3)]

        # Precompute edge MEX scores for all pairs of colors
        mex_table = [[0]*3 for _ in range(3)]
        for x in range(3):
            for y in range(3):
                if x == y:
                    mex_table[x][y] = 0 if x != 0 else 1
                else:
                    s = {x,y}
                    for val in range(3):
                        if val not in s:
                            mex_table[x][y] = val
                            break

        for first_color in range(3):
            # dp[pos][prev_color] = dict {(a0,a1): max_score}
            dp = [ [dict() for _ in range(3)] for _ in range(m) ]
            # Initialize dp at pos=0
            a0 = 1 if first_color == 0 else 0
            a1 = 1 if first_color == 1 else 0
            dp[0][first_color][(a0,a1)] = 0

            for pos in range(1, m):
                for prev_color in range(3):
                    for (c0,c1), val in dp[pos-1][prev_color].items():
                        for curr_color in range(3):
                            na0 = c0 + (1 if curr_color == 0 else 0)
                            na1 = c1 + (1 if curr_color == 1 else 0)
                            # Edge from prev_color to curr_color
                            score = val + mex_table[prev_color][curr_color]
                            d = dp[pos][curr_color]
                            if (na0, na1) not in d or d[(na0, na1)] < score:
                                d[(na0, na1)] = score

            # Close the cycle: add edge from last node to first node
            res = {}
            for last_color in range(3):
                d = dp[m-1][last_color]
                add_score = mex_table[last_color][first_color]
                for (c0,c1), val in d.items():
                    total_score = val + add_score
                    if (c0,c1) not in res or res[(c0,c1)] < total_score:
                        res[(c0,c1)] = total_score
            dp_first_color[first_color] = res

        # Merge results from different first_color choices
        # For each (a0,a1), take max over first_color
        merged = {}
        for fc in range(3):
            for key, val in dp_first_color[fc].items():
                if key not in merged or merged[key] < val:
                    merged[key] = val

        contribs.append(merged)

    # Combine all cycles' dp by knapsack-like DP
    total_dp = {(0,0): 0}
    for dp in contribs:
        new_dp = {}
        for (u0,u1), val in total_dp.items():
            for (a0,a1), sc in dp.items():
                key = (u0+a0, u1+a1)
                if key[0] <= N and key[1] <= N:
                    if key not in new_dp or new_dp[key] < val + sc:
                        new_dp[key] = val + sc
        total_dp = new_dp

    # For each query, output total_dp[(A0,A1)] or 0 if not found
    # A2 = N - A0 - A1, no need to check explicitly
    out = []
    for A0,A1,A2 in queries:
        out.append(str(total_dp.get((A0,A1),0)))
    print('\n'.join(out))

if __name__ == "__main__":
    solve()