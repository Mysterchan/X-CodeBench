def main():
    import sys
    sys.setrecursionlimit(10**7)

    N = int(sys.stdin.readline())
    A = sys.stdin.readline().strip()

    # Length of A is 3^N
    # We want to find the minimum number of changes to flip the final majority bit after N operations.

    # dp(pos, level) will return a tuple (cost0, cost1)
    # cost0: minimum changes to make the subtree rooted at pos (length 3^level) have final majority 0
    # cost1: minimum changes to make the subtree rooted at pos have final majority 1

    # Base case: level=0 means length=1, just one character
    # cost0 = 0 if A[pos] == '0' else 1
    # cost1 = 0 if A[pos] == '1' else 1

    # For level > 0:
    # We split into 3 parts of length 3^(level-1)
    # For each part, get (cost0, cost1)
    # Then, to get majority 0 in the parent:
    # We need at least 2 of the 3 children to be 0
    # So we try all combinations of choosing which children are 0 or 1 to get majority 0 with minimal cost
    # Similarly for majority 1.

    # Since N <= 13, 3^N can be large (~1.6 million), but we can do a top-down DP with memoization.

    from functools import lru_cache

    pow3 = [1]
    for _ in range(N):
        pow3.append(pow3[-1]*3)

    @lru_cache(None)
    def dp(pos, level):
        if level == 0:
            # single character
            c = A[pos]
            cost0 = 0 if c == '0' else 1
            cost1 = 0 if c == '1' else 1
            return (cost0, cost1)

        length = pow3[level-1]
        # get costs for three children
        c0_0, c0_1 = dp(pos, level-1)
        c1_0, c1_1 = dp(pos+length, level-1)
        c2_0, c2_1 = dp(pos+2*length, level-1)

        # To get majority 0, at least two children must be 0
        # Possible ways to get majority 0:
        # 0 0 0
        # 0 0 1
        # 0 1 0
        # 1 0 0
        # For each child, we choose cost0 or cost1 accordingly

        # List all combinations of children states (0 or 1)
        # For majority 0, count how many zeros >= 2
        # For majority 1, count how many ones >= 2

        children_costs = [
            (c0_0, c0_1),
            (c1_0, c1_1),
            (c2_0, c2_1)
        ]

        # For majority 0
        min_cost_0 = float('inf')
        # For majority 1
        min_cost_1 = float('inf')

        # There are 8 combinations (2^3) of choosing 0 or 1 for each child
        # For each combination, check if majority is 0 or 1 and update min_cost accordingly

        for mask in range(8):
            # mask bit i = 0 means child i is 0, 1 means child i is 1
            bits = [(mask >> i) & 1 for i in range(3)]
            zero_count = bits.count(0)
            one_count = 3 - zero_count

            cost = 0
            for i in range(3):
                if bits[i] == 0:
                    cost += children_costs[i][0]
                else:
                    cost += children_costs[i][1]

            if zero_count >= 2:
                if cost < min_cost_0:
                    min_cost_0 = cost
            if one_count >= 2:
                if cost < min_cost_1:
                    min_cost_1 = cost

        return (min_cost_0, min_cost_1)

    # Compute original final majority bit
    # The final majority bit is the one with minimal cost 0 or 1 at dp(0, N)
    cost0, cost1 = dp(0, N)
    # The original final bit is the one with minimal cost 0 or 1 without changes
    # But we want to flip it, so minimal changes to flip final bit is min cost of the other bit

    # Actually, the original final bit is the majority of the original string after N operations,
    # which is the bit with minimal cost 0 or 1 when no changes are made (cost 0 for that bit).
    # But since dp returns minimal changes to get 0 or 1, and original string is fixed,
    # the minimal changes to flip final bit is the minimal cost to get the opposite bit.

    # Determine original final bit by checking which cost is zero (no changes)
    # But it's possible both cost0 and cost1 > 0 if original string is ambiguous? No, original string has a definite final bit.

    # So original final bit is the one with minimal cost (should be 0)
    if cost0 <= cost1:
        # original final bit is 0
        ans = cost1
    else:
        # original final bit is 1
        ans = cost0

    print(ans)


if __name__ == "__main__":
    main()