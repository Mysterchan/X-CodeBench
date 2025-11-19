import sys
import threading

def main():
    import sys
    import bisect
    from collections import deque

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N, M, A, B = map(int, input().split())
    forbidden = []
    for _ in range(M):
        l, r = map(int, input().split())
        forbidden.append((l, r))
    # Build good intervals
    good = []
    if M == 0:
        good.append((1, N))
    else:
        last = 1
        for l, r in forbidden:
            if l - 1 >= last:
                good.append((last, l - 1))
            last = r + 1
        if last <= N:
            good.append((last, N))
    K = len(good)
    starts = [iv[0] for iv in good]
    ends = [iv[1] for iv in good]

    visited = [[] for _ in range(K)]
    Q = deque()

    # Try to add a new reachable segment [l, r] into interval k
    def add_segment(k, l, r):
        if l > r:
            return False
        vlist = visited[k]
        new_ranges = []
        curr = l
        # find new sub-ranges not covered by visited
        for vl, vr in vlist:
            if vr < curr:
                continue
            if vl > r:
                break
            if vl > curr:
                new_ranges.append((curr, vl - 1))
            curr = max(curr, vr + 1)
            if curr > r:
                break
        if curr <= r:
            new_ranges.append((curr, r))
        if not new_ranges:
            return False
        # insert each new range, merge, and enqueue
        for nl, nr in new_ranges:
            # merge into vlist
            pos = bisect.bisect_left(vlist, (nl, -1))
            start, end = nl, nr
            # merge with previous
            if pos > 0 and vlist[pos - 1][1] + 1 >= nl:
                pos -= 1
                start = min(start, vlist[pos][0])
                end = max(end, vlist[pos][1])
                del vlist[pos]
            # merge with next
            while pos < len(vlist) and vlist[pos][0] <= nr + 1:
                start = min(start, vlist[pos][0])
                end = max(end, vlist[pos][1])
                del vlist[pos]
            vlist.insert(pos, (start, end))
            Q.append((k, start, end))
            # check if reaches N
            if start <= N <= end:
                print("Yes")
                sys.exit(0)
        return True

    # initialize
    add_segment(0, 1, 1)

    while Q:
        k, l, r = Q.popleft()
        # shift by [A,B]
        L = l + A
        if L > N:
            continue
        R = r + B
        if R > N:
            R = N
        # find first interval with end >= L
        i = bisect.bisect_left(ends, L)
        # but bisect_left gives first idx where ends[idx] >= L
        # if i == K or ends[i] < L, adjust
        if i == K:
            continue
        # iterate intervals overlapping [L,R]
        idx = i
        while idx < K and starts[idx] <= R:
            nl = max(L, starts[idx])
            nr = min(R, ends[idx])
            add_segment(idx, nl, nr)
            idx += 1

    print("No")

if __name__ == "__main__":
    main()