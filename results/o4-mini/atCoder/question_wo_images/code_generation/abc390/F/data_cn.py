import sys
import threading

def main():
    import sys

    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    # positions of each value v in A
    pos = [[] for _ in range(N+2)]
    for i, v in enumerate(A, start=1):
        pos[v].append(i)

    ans = 0
    # For v from 1 to N, count T(v): number of subarrays where v appears
    # but v-1 does not; sum T(v) is the total blocks over all subarrays.
    for v in range(1, N+1):
        curr = pos[v]
        if not curr:
            continue
        prev = pos[v-1]  # for v=1, pos[0] is empty
        # build prev_extended with sentinels at 0 and N+1
        # so segments to avoid v-1 are between prev_extended[i]+1 .. prev_extended[i+1]-1
        # if prev is empty, it's one segment [1..N]
        idx_c = 0
        len_c = len(curr)
        # sentinel 0
        last = 0
        # process each prev occurrence, plus the final sentinel
        for p in prev:
            l = last + 1
            r = p - 1
            if l <= r:
                # process segment [l..r]
                # skip curr positions before l
                while idx_c < len_c and curr[idx_c] < l:
                    idx_c += 1
                if idx_c < len_c and curr[idx_c] <= r:
                    # there is at least one curr in [l..r]
                    # find end index k such that curr[k] <= r
                    k = idx_c
                    while k+1 < len_c and curr[k+1] <= r:
                        k += 1
                    # compute total subarrays in [l..r]
                    seg_len = r - l + 1
                    total_seg = seg_len * (seg_len + 1) // 2
                    # compute subarrays without any curr
                    sum_miss = 0
                    prev_pos = l - 1
                    for t in range(idx_c, k+1):
                        pt = curr[t]
                        d = pt - prev_pos - 1
                        sum_miss += d * (d + 1) // 2
                        prev_pos = pt
                    # after last curr up to r
                    d = r - prev_pos
                    sum_miss += d * (d + 1) // 2
                    ans += total_seg - sum_miss
                    idx_c = k + 1
            last = p
        # final segment after last prev up to N
        l = last + 1
        r = N
        if l <= r:
            while idx_c < len_c and curr[idx_c] < l:
                idx_c += 1
            if idx_c < len_c and curr[idx_c] <= r:
                k = idx_c
                while k+1 < len_c and curr[k+1] <= r:
                    k += 1
                seg_len = r - l + 1
                total_seg = seg_len * (seg_len + 1) // 2
                sum_miss = 0
                prev_pos = l - 1
                for t in range(idx_c, k+1):
                    pt = curr[t]
                    d = pt - prev_pos - 1
                    sum_miss += d * (d + 1) // 2
                    prev_pos = pt
                d = r - prev_pos
                sum_miss += d * (d + 1) // 2
                ans += total_seg - sum_miss
                idx_c = k + 1

    # output the final answer
    print(ans)

if __name__ == "__main__":
    main()