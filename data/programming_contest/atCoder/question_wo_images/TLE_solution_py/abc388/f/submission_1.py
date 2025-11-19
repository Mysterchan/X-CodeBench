import sys
from collections import deque
import bisect

def solve():

    try:
        input = sys.stdin.readline
        N_str, M_str, A_str, B_str = input().split()
        N, M, A, B = int(N_str), int(M_str), int(A_str), int(B_str)

        bad_intervals_in = []
        for _ in range(M):
            l, r = map(int, input().split())

            if l <= N:
                bad_intervals_in.append((l, min(r, N)))
    except (IOError, ValueError):
        return

    def coalesce(intervals):
        if not intervals:
            return []
        merged = []
        current_s, current_e = intervals[0]
        for next_s, next_e in intervals[1:]:
            if next_s <= current_e + 1:
                current_e = max(current_e, next_e)
            else:
                merged.append((current_s, current_e))
                current_s, current_e = next_s, next_e
        merged.append((current_s, current_e))
        return merged

    bad_intervals_in.sort()
    bad = coalesce(bad_intervals_in)

    def merge_and_coalesce(list1, list2):
        temp_list = sorted(list1 + list2)
        return coalesce(temp_list)

    def subtract_list(A, B):
        res = []
        a_ptr, b_ptr = 0, 0
        while a_ptr < len(A):
            s, e = A[a_ptr]
            current_pos = s

            while b_ptr < len(B) and B[b_ptr][1] < current_pos:
                b_ptr += 1

            temp_b_ptr = b_ptr
            while current_pos <= e and temp_b_ptr < len(B):
                bs, be = B[temp_b_ptr]
                if bs > e:
                    break
                if current_pos < bs:
                    res.append((current_pos, min(e, bs - 1)))
                current_pos = max(current_pos, be + 1)
                temp_b_ptr += 1

            if current_pos <= e:
                res.append((current_pos, e))

            a_ptr += 1
        return res

    if bad:
        idx = bisect.bisect_right(bad, (1, float('inf')))
        if idx > 0 and bad[idx - 1][0] <= 1 <= bad[idx - 1][1]:
            print("No")
            return

    q = deque([(1, 1)])
    visited = [(1, 1)]

    while q:

        next_wave_raw = [(c + A, min(d + B, N)) for c, d in q if c + A <= N]
        q.clear()

        if not next_wave_raw:
            break

        next_wave_raw.sort()
        next_wave_merged = coalesce(next_wave_raw)

        forbidden = merge_and_coalesce(bad, visited)
        newly_reachable = subtract_list(next_wave_merged, forbidden)

        if not newly_reachable:
            break

        for s, e in newly_reachable:
            q.append((s, e))

        visited = merge_and_coalesce(visited, newly_reachable)

    idx = bisect.bisect_right(visited, (N, float('inf')))
    if idx > 0 and visited[idx - 1][0] <= N <= visited[idx - 1][1]:
        print("Yes")
    else:
        print("No")

solve()