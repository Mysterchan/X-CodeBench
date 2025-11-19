import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    # Precompute sumA[mask] = sum of A[i] for bits in mask
    M = 1 << N
    sumA = [0] * M
    for mask in range(1, M):
        lsb = mask & -mask
        i = (lsb.bit_length() - 1)
        sumA[mask] = sumA[mask ^ lsb] + A[i]

    # dp[mask] = set of possible XOR sums for partitioning 'mask'
    dp = [None] * M
    dp[0] = {0}

    # Group masks by popcount to fill dp in increasing order
    from collections import defaultdict
    masks_by_cnt = defaultdict(list)
    for mask in range(1, M):
        masks_by_cnt[mask.bit_count()].append(mask)

    # Fill dp
    for cnt in range(1, N + 1):
        for mask in masks_by_cnt[cnt]:
            base = mask & -mask       # least significant bit
            rest_mask = mask ^ base
            cur_set = set()
            # Enumerate all submasks that include 'base'
            sub1 = rest_mask
            while True:
                sub = sub1 | base
                rem = mask ^ sub
                s_val = sumA[sub]
                # Combine with all values from dp[rem]
                for v in dp[rem]:
                    cur_set.add(v ^ s_val)
                if sub1 == 0:
                    break
                sub1 = (sub1 - 1) & rest_mask
            dp[mask] = cur_set

    full = (1 << N) - 1
    print(len(dp[full]))

if __name__ == "__main__":
    main()