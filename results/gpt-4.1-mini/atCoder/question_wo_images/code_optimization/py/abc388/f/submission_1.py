import sys
import bisect

def solve():
    input = sys.stdin.readline
    N, M, A, B = map(int, input().split())

    bad_intervals = []
    for _ in range(M):
        l, r = map(int, input().split())
        if l <= N:
            bad_intervals.append((l, min(r, N)))

    # Merge overlapping bad intervals
    bad_intervals.sort()
    merged_bad = []
    for interval in bad_intervals:
        if not merged_bad or merged_bad[-1][1] < interval[0] - 1:
            merged_bad.append(interval)
        else:
            merged_bad[-1] = (merged_bad[-1][0], max(merged_bad[-1][1], interval[1]))

    # Check if start square 1 is bad
    idx = bisect.bisect_right(merged_bad, (1, float('inf')))
    if idx > 0 and merged_bad[idx - 1][0] <= 1 <= merged_bad[idx - 1][1]:
        print("No")
        return

    # Construct good intervals from bad intervals
    good_intervals = []
    prev_end = 0
    for s, e in merged_bad:
        if prev_end + 1 <= s - 1:
            good_intervals.append((prev_end + 1, s - 1))
        prev_end = e
    if prev_end < N:
        good_intervals.append((prev_end + 1, N))

    # If 1 is not in any good interval (should not happen as checked above), no path
    # Find the good interval containing 1
    # Since intervals are sorted and non-overlapping, binary search
    left, right = 0, len(good_intervals) - 1
    start_idx = -1
    while left <= right:
        mid = (left + right) // 2
        s, e = good_intervals[mid]
        if s <= 1 <= e:
            start_idx = mid
            break
        elif 1 < s:
            right = mid - 1
        else:
            left = mid + 1
    if start_idx == -1:
        print("No")
        return

    # BFS over intervals using a queue
    from collections import deque
    queue = deque()
    visited = [False] * len(good_intervals)
    queue.append(start_idx)
    visited[start_idx] = True

    # Precompute max jump length for quick checks
    # We'll try to jump from current interval to any interval that can be reached by a jump in [A,B]

    # For efficient interval lookup, extract starts and ends separately
    starts = [iv[0] for iv in good_intervals]
    ends = [iv[1] for iv in good_intervals]

    while queue:
        cur = queue.popleft()
        s_cur, e_cur = good_intervals[cur]

        # From any position x in [s_cur, e_cur], we can jump i in [A,B] steps to x+i
        # So reachable positions are in [s_cur + A, e_cur + B], capped at N
        reach_start = s_cur + A
        reach_end = min(e_cur + B, N)
        if reach_start > N:
            continue

        # Find intervals in good_intervals that intersect with [reach_start, reach_end]
        # Since intervals are sorted and non-overlapping, we can find the first interval with end >= reach_start
        left_idx = bisect.bisect_left(ends, reach_start)
        # Iterate intervals starting from left_idx while start <= reach_end
        i = left_idx
        while i < len(good_intervals) and good_intervals[i][0] <= reach_end:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
            i += 1

    # Check if N is in any visited interval
    # Since intervals are sorted, binary search for N
    idx = bisect.bisect_right(good_intervals, (N, float('inf')))
    if idx > 0 and good_intervals[idx - 1][0] <= N <= good_intervals[idx - 1][1] and visited[idx - 1]:
        print("Yes")
    else:
        print("No")

solve()