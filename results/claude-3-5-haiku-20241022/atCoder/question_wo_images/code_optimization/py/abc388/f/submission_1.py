import sys
import bisect

def solve():
    try:
        input = sys.stdin.readline
        N_str, M_str, A_str, B_str = input().split()
        N, M, A, B = int(N_str), int(M_str), int(A_str), int(B_str)

        bad_intervals = []
        for _ in range(M):
            l, r = map(int, input().split())
            if l <= N:
                bad_intervals.append((l, min(r, N)))
    except (IOError, ValueError):
        return

    # Coalesce bad intervals
    if bad_intervals:
        bad_intervals.sort()
        merged = []
        current_s, current_e = bad_intervals[0]
        for next_s, next_e in bad_intervals[1:]:
            if next_s <= current_e + 1:
                current_e = max(current_e, next_e)
            else:
                merged.append((current_s, current_e))
                current_s, current_e = next_s, next_e
        merged.append((current_s, current_e))
        bad_intervals = merged

    # Check if start position is bad
    if bad_intervals:
        idx = bisect.bisect_right(bad_intervals, (1, float('inf')))
        if idx > 0 and bad_intervals[idx - 1][0] <= 1 <= bad_intervals[idx - 1][1]:
            print("No")
            return

    # BFS with interval representation
    visited = [(1, 1)]
    current_wave = [(1, 1)]

    while current_wave:
        # Generate next wave
        next_wave = []
        for c, d in current_wave:
            if c + A <= N:
                next_wave.append((c + A, min(d + B, N)))

        if not next_wave:
            break

        # Merge next wave intervals
        next_wave.sort()
        merged = []
        current_s, current_e = next_wave[0]
        for next_s, next_e in next_wave[1:]:
            if next_s <= current_e + 1:
                current_e = max(current_e, next_e)
            else:
                merged.append((current_s, current_e))
                current_s, current_e = next_s, next_e
        merged.append((current_s, current_e))
        next_wave = merged

        # Subtract forbidden (bad + visited)
        newly_reachable = []
        for s, e in next_wave:
            current_pos = s
            
            # Check against bad intervals
            for bs, be in bad_intervals:
                if bs > e:
                    break
                if be < current_pos:
                    continue
                if current_pos < bs:
                    newly_reachable.append((current_pos, min(e, bs - 1)))
                current_pos = max(current_pos, be + 1)
                if current_pos > e:
                    break
            
            if current_pos <= e:
                # Check against visited intervals
                temp_pos = current_pos
                for vs, ve in visited:
                    if vs > e:
                        break
                    if ve < temp_pos:
                        continue
                    if temp_pos < vs:
                        newly_reachable.append((temp_pos, min(e, vs - 1)))
                    temp_pos = max(temp_pos, ve + 1)
                    if temp_pos > e:
                        break
                
                if temp_pos <= e:
                    newly_reachable.append((temp_pos, e))

        if not newly_reachable:
            break

        # Merge visited with newly reachable
        visited = sorted(visited + newly_reachable)
        merged = []
        current_s, current_e = visited[0]
        for next_s, next_e in visited[1:]:
            if next_s <= current_e + 1:
                current_e = max(current_e, next_e)
            else:
                merged.append((current_s, current_e))
                current_s, current_e = next_s, next_e
        merged.append((current_s, current_e))
        visited = merged

        current_wave = newly_reachable

    # Check if N is reachable
    idx = bisect.bisect_right(visited, (N, float('inf')))
    if idx > 0 and visited[idx - 1][0] <= N <= visited[idx - 1][1]:
        print("Yes")
    else:
        print("No")

solve()