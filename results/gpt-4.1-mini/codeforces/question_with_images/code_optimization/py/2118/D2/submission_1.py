import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    delays = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))

    # Precompute for each traffic light the "red time" modulo k
    # A light is red at times t where t % k == d_i
    # At time 0, we start at position a_i, facing right (+1)
    # Each second:
    #   - If current cell has red light at current time, turn around
    #   - Move one cell in current direction
    #
    # We want to know if starting at position a_i, we will eventually leave [1, 10^15]
    #
    # Key insight:
    # The movement is deterministic and periodic modulo k.
    # The position changes by +1 or -1 each second, direction flips only at red lights.
    #
    # We can simulate the movement modulo k, but since k can be large, we use a different approach:
    #
    # The problem reduces to checking if the starting position is in a "trap" interval where the person
    # bounces forever between two traffic lights that cause direction flips at the same time modulo k.
    #
    # We can find the minimal and maximal positions reachable without being trapped.
    #
    # Approach:
    # For each traffic light i, define:
    #   - The time offset d_i (red time modulo k)
    #   - The position p_i
    #
    # We want to find intervals where the person can be trapped.
    #
    # The person can only be trapped if there exist two traffic lights i and j such that:
    #   - They are consecutive in position
    #   - Their red times d_i and d_j satisfy a certain condition that causes the person to bounce between them forever.
    #
    # We will precompute two arrays:
    #   - left_bound[i]: the minimal position reachable from p_i going left without being trapped
    #   - right_bound[i]: the maximal position reachable from p_i going right without being trapped
    #
    # Then for each query position a:
    #   - If a < left_bound[0], answer YES (can leave to the left)
    #   - Else if a > right_bound[-1], answer YES (can leave to the right)
    #   - Else find the interval [p_i, p_{i+1}] where a lies
    #     - If a is inside a trap interval, answer NO
    #     - Else YES
    #
    # To find trap intervals, we analyze pairs of consecutive traffic lights.
    #
    # The person is trapped between p_i and p_{i+1} if and only if:
    #   (d_{i+1} - d_i) % k == (p_{i+1} - p_i) % k
    #
    # This condition means the red lights are synchronized so that the person bounces forever.
    #
    # We will mark such intervals as traps.
    #
    # Then, the union of all trap intervals forms the "no escape" zones.
    #
    # For queries, if a lies inside any trap interval, answer NO, else YES.

    trap_intervals = []
    for i in range(n - 1):
        dist = positions[i + 1] - positions[i]
        diff = (delays[i + 1] - delays[i]) % k
        if diff == dist % k:
            # trap interval between positions[i] and positions[i+1]
            trap_intervals.append((positions[i], positions[i + 1]))

    # Merge overlapping trap intervals
    merged = []
    for interval in sorted(trap_intervals):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(list(interval))
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    # For queries:
    # If position < 1 or > 10^15, obviously YES (but queries are guaranteed in [1, 10^15])
    # If position < merged[0][0], YES (can escape left)
    # If position > merged[-1][1], YES (can escape right)
    # Else check if position inside any merged trap interval -> NO else YES

    # Edge cases: no traps
    if not merged:
        for a in queries:
            print("YES")
        continue

    # For binary search, create arrays of starts and ends
    starts = [interval[0] for interval in merged]
    ends = [interval[1] for interval in merged]

    for a in queries:
        # If a < first trap start or a > last trap end => YES
        if a < starts[0] or a > ends[-1]:
            print("YES")
            continue

        # Binary search to find the interval that might contain a
        idx = bisect.bisect_right(starts, a) - 1
        if idx >= 0 and starts[idx] <= a <= ends[idx]:
            print("NO")
        else:
            print("YES")