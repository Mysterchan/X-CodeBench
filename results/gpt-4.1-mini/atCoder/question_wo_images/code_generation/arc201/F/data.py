import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # We'll keep track of cumulative sums of each problem type
    cumA = 0  # Hell
    cumB = 0  # Hard
    cumC = 0  # Medium
    cumD = 0  # Easy
    cumE = 0  # Baby

    res = []
    for __ in range(N):
        A, B, C, D, E = map(int, input().split())
        cumA += A
        cumB += B
        cumC += C
        cumD += D
        cumE += E

        # For k-th prefix, maximum number of times C3C can be held is limited by:
        # Div1 needs: 1 Hell, 1 Hard, 1 Medium
        # Div2 needs: 1 Hard, 1 Medium, 1 Easy
        # Div3 needs: 1 Medium, 1 Easy, 1 Baby
        #
        # Let x,y,z be the number of Div1, Div2, Div3 contests held.
        # We want to maximize x+y+z subject to:
        # x <= cumA (Hell)
        # x + y <= cumB (Hard)
        # x + y + z <= cumC (Medium)
        # y + z <= cumD (Easy)
        # z <= cumE (Baby)
        #
        # We want max x+y+z = total contests.

        # The problem reduces to:
        # max x+y+z
        # s.t.
        # x <= A
        # x + y <= B
        # x + y + z <= C
        # y + z <= D
        # z <= E

        # We can try to find max total = x+y+z = t
        # For given t, check feasibility:
        # From constraints:
        # x <= A
        # y <= B - x
        # z <= C - (x + y)
        # y + z <= D
        # z <= E

        # Since we want to maximize t = x + y + z,
        # we can do a binary search on t.

        # But since constraints are large, we need O(1) check.

        # Let's try to find max t by iterating over x:
        # But that would be O(N^2).

        # Instead, we can do a binary search on t.

        low, high = 0, min(cumA + cumB + cumC + cumD + cumE, 10**18)
        # upper bound can be sum of all problems divided by 3 (since each contest uses 3 problems)
        # but to be safe, use a large number.

        def can(t):
            # We want to check if there exist x,y,z >=0 with x+y+z = t satisfying:
            # x <= A
            # x + y <= B
            # x + y + z <= C
            # y + z <= D
            # z <= E

            # From x+y+z = t => y+z = t - x

            # Constraints:
            # x <= A
            # x + y <= B => y <= B - x
            # x + y + z <= C => t <= C
            # y + z <= D => t - x <= D => x >= t - D
            # z <= E

            # Also y,z >=0

            # For fixed x:
            # y + z = t - x
            # y <= B - x
            # z <= E
            # y,z >=0

            # So y in [0, B - x], z in [0, E], y+z = t - x

            # So t - x <= (B - x) + E => t - x <= B - x + E => t <= B + E

            # Also x >= t - D

            # Also x <= A

            # So x must satisfy:
            # max(0, t - D) <= x <= min(A, t, B, t) (t is total, but x <= A and x <= B and x <= t)
            # Actually, x <= A
            # Also x <= B (since x + y <= B and y >=0)
            # Also x <= t (since x <= t)

            # So x in [max(0, t - D), min(A, B, t)]

            # For x in that range, check if y and z can satisfy y+z = t - x, y <= B - x, z <= E

            # y <= B - x
            # z <= E
            # y + z = t - x

            # So t - x <= (B - x) + E => t <= B + E

            # So if t > B + E, no solution.

            # Also t <= C (from x + y + z <= C)

            # So conditions:
            # t <= C
            # t <= B + E
            # There exists x in [max(0, t - D), min(A, B, t)] (interval non-empty)

            # Check interval:
            left = max(0, t - D)
            right = min(A, B, t)
            if left > right:
                return False
            if t > C:
                return False
            if t > B + E:
                return False
            return True

        while low < high:
            mid = (low + high + 1) // 2
            if can(mid):
                low = mid
            else:
                high = mid - 1

        res.append(str(low))
    print(" ".join(res))