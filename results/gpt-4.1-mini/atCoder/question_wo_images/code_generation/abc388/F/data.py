import sys
input = sys.stdin.readline

def main():
    N, M, A, B = map(int, input().split())
    bad_intervals = [tuple(map(int, input().split())) for _ in range(M)]

    # Add sentinel intervals at start and end to simplify logic
    # We consider the range [1, N]
    # bad intervals are given sorted and non-overlapping

    # We'll consider the "good" intervals between bad intervals and at the edges:
    # good intervals are:
    # [1, L_1-1], [R_1+1, L_2-1], ..., [R_M+1, N]

    good_intervals = []
    prev_end = 0
    for L, R in bad_intervals:
        if L - 1 >= prev_end + 1:
            good_intervals.append((prev_end + 1, L - 1))
        prev_end = R
    if prev_end < N:
        good_intervals.append((prev_end + 1, N))

    # We start at square 1, which must be good (not bad)
    # Check if 1 is in any good interval
    # If not, immediately No
    # Also, if N is bad, no way to reach it (since we must land exactly on N)
    # But problem states 1 < L_i ≤ R_i < N, so 1 and N are never bad.

    # We want to check if we can move from 1 to N by jumps of length in [A,B]
    # landing only on good squares.

    # The problem is large N (up to 10^12), so we cannot simulate all squares.
    # We use intervals and BFS-like approach on intervals.

    # We'll keep track of reachable positions as intervals.
    # Initially reachable = [1,1]

    # For each step, from reachable intervals, we can jump i in [A,B]
    # So reachable positions after one jump are:
    # For each reachable interval [l,r], new reachable positions are [l+A, r+B]
    # intersected with good intervals and within [1,N]

    # We repeat until no new reachable positions or we reach N.

    # Since B ≤ 20, and M ≤ 2*10^4, this approach is feasible.

    from collections import deque

    # Merge good intervals for quick intersection
    # good_intervals are sorted and non-overlapping

    # reachable intervals stored as list of (start,end), sorted and non-overlapping
    reachable = [(1,1)]

    # We'll process reachable intervals step by step
    # To avoid infinite loops, we keep track of visited intervals
    # But intervals can be large, so we keep a set of visited intervals as merged intervals

    # We'll use a queue of intervals to process
    queue = deque()
    queue.append((1,1))

    # visited intervals merged
    visited = []

    def merge_intervals(intervals):
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for s,e in intervals[1:]:
            last_s, last_e = merged[-1]
            if s <= last_e + 1:
                merged[-1] = (last_s, max(last_e, e))
            else:
                merged.append((s,e))
        return merged

    # Add initial reachable interval to visited
    visited = [(1,1)]

    # Function to subtract bad intervals from a given interval
    # Actually, we have good intervals, so we intersect with good intervals
    # We'll implement intersection of [l,r] with good_intervals

    def intersect_with_good(l, r):
        res = []
        # good_intervals sorted and non-overlapping
        # find all good intervals that intersect with [l,r]
        # since good_intervals are sorted, we can binary search
        import bisect

        # Extract starts for binary search
        starts = [g[0] for g in good_intervals]

        # Find first good interval that might intersect
        idx = bisect.bisect_right(starts, r)
        # good intervals with start <= r might intersect

        # We'll check intervals from idx-1 down to 0 to find intersections
        # and from idx upwards

        # Check intervals before idx
        i = idx - 1
        while i >= 0 and good_intervals[i][1] >= l:
            gs, ge = good_intervals[i]
            inter_s = max(l, gs)
            inter_e = min(r, ge)
            if inter_s <= inter_e:
                res.append((inter_s, inter_e))
            i -= 1

        # Check intervals after idx
        i = idx
        while i < len(good_intervals) and good_intervals[i][0] <= r:
            gs, ge = good_intervals[i]
            inter_s = max(l, gs)
            inter_e = min(r, ge)
            if inter_s <= inter_e:
                res.append((inter_s, inter_e))
            i += 1

        # Merge results
        return merge_intervals(res)

    # Function to subtract visited intervals from new intervals
    # new_intervals - visited_intervals
    # Both lists sorted and non-overlapping
    def subtract_intervals(new_intervals, visited_intervals):
        res = []
        i = j = 0
        while i < len(new_intervals):
            ns, ne = new_intervals[i]
            while j < len(visited_intervals) and visited_intervals[j][1] < ns:
                j += 1
            curr_s = ns
            while j < len(visited_intervals) and visited_intervals[j][0] <= ne:
                vs, ve = visited_intervals[j]
                if vs > curr_s:
                    res.append((curr_s, min(ve-1, ne)))
                if ve >= ne:
                    curr_s = ne + 1
                    break
                curr_s = max(curr_s, ve + 1)
                j += 1
            if curr_s <= ne:
                res.append((curr_s, ne))
            i += 1
        return res

    # But the above subtract_intervals is complicated and buggy.
    # Instead, we do a simpler approach:
    # For each new interval, subtract visited intervals by scanning visited intervals.

    # Let's implement a simpler subtract function:
    def subtract_intervals_simple(new_intervals, visited_intervals):
        res = []
        vi = 0
        for ns, ne in new_intervals:
            curr_start = ns
            while vi < len(visited_intervals) and visited_intervals[vi][1] < curr_start:
                vi += 1
            temp_start = curr_start
            while vi < len(visited_intervals) and visited_intervals[vi][0] <= ne:
                vs, ve = visited_intervals[vi]
                if vs > temp_start:
                    res.append((temp_start, vs - 1))
                temp_start = max(temp_start, ve + 1)
                if temp_start > ne:
                    break
                vi += 1
            if temp_start <= ne:
                res.append((temp_start, ne))
        return res

    # BFS-like process
    while queue:
        l, r = queue.popleft()
        # From [l,r], next reachable positions are [l+A, r+B]
        nl = l + A
        nr = r + B
        if nl > N:
            continue
        if nr > N:
            nr = N

        # Intersect with good intervals
        candidates = intersect_with_good(nl, nr)
        if not candidates:
            continue

        # Subtract visited intervals
        new_intervals = subtract_intervals_simple(candidates, visited)
        if not new_intervals:
            continue

        # Add new intervals to visited and queue
        for ns, ne in new_intervals:
            # Check if N in [ns, ne]
            if ns <= N <= ne:
                print("Yes")
                return
            queue.append((ns, ne))
        visited += new_intervals
        visited = merge_intervals(visited)

    # If we exit loop without reaching N
    print("No")

if __name__ == "__main__":
    main()