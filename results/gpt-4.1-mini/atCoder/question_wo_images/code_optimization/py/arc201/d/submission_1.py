import sys
import bisect

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    # We want to minimize max((A_i + B_i) % M) over all permutations of A.
    # Key insight: For each B_i, find A_j such that (A_j + B_i) % M <= x.
    # We binary search on x.

    # Precompute B twice for circular indexing
    B2 = B + [b + M for b in B]

    l, r = 0, M - 1
    while l < r:
        mid = (l + r) // 2

        # For each A[i], find the interval of B indices j where (A[i] + B[j]) % M <= mid
        # (A[i] + B[j]) % M <= mid
        # => B[j] <= mid - A[i] (mod M)
        # Because B is sorted, we find the range of j in B2 where B2[j] in [M - A[i], M - A[i] + mid]

        # We'll check if there exists a permutation of A to B such that all sums <= mid
        # This reduces to checking if intervals [L_i, R_i) for each i can be assigned disjointly.

        intervals = []
        for i in range(n):
            low = M - A[i]
            high = low + mid
            L = bisect.bisect_left(B2, low)
            R = bisect.bisect_right(B2, high)
            intervals.append((L, R))

        # We want to check if there exists a shift s (0 <= s < n) such that
        # for all i, intervals[i] contains i + s (mod n)
        # Because B2 is B concatenated with B+M, indices i+s and i+s+n are equivalent modulo n.

        # We try all possible shifts s by checking coverage of intervals
        # Using a difference array to check coverage of all points

        diff = [0] * (2 * n + 1)
        for i in range(n):
            L, R = intervals[i]
            # We want to cover position i + s in [L, R)
            # So s in [L - i, R - i)
            start = L - i
            end = R - i
            # Because s in [0, n), we consider intervals modulo n
            # We add coverage in diff array for s in [start, end)
            # But start and end can be negative or > n, so we normalize

            # Normalize start and end to [0, 2n) for difference array
            # We'll handle wrap-around by adding intervals accordingly

            if end <= start:
                # Interval wraps around modulo n
                # Add [start, 2n) and [0, end)
                if start < 2 * n:
                    diff[max(start,0)] += 1
                    diff[2 * n] -= 1
                if end > 0:
                    diff[0] += 1
                    diff[min(end, 2 * n)] -= 1
            else:
                # Normal interval
                if end > 0 and start < 2 * n:
                    diff[max(start,0)] += 1
                    diff[min(end, 2 * n)] -= 1

        # Prefix sum to find coverage count for each s in [0, 2n)
        for i in range(1, 2 * n):
            diff[i] += diff[i - 1]

        # Check if any s in [0, n) covers all intervals (diff[s] == n)
        if any(diff[s] == n for s in range(n)):
            r = mid
        else:
            l = mid + 1

    print(l)