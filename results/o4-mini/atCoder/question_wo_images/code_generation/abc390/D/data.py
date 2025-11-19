import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    M = 1 << N

    # Precompute sum_sub[mask] = sum of A[i] for bits i in mask.
    sum_sub = [0] * M
    for mask in range(1, M):
        # lowbit = mask & -mask
        lb = mask & -mask
        i = lb.bit_length() - 1
        sum_sub[mask] = sum_sub[mask ^ lb] + A[i]

    # Precompute lowest bit index and mask without that bit, and the lowbit mask.
    lowest_idx = [0] * M
    mask_wo_low = [0] * M
    lowbit_mask = [0] * M
    for mask in range(1, M):
        lb = mask & -mask
        lowbit_mask[mask] = lb
        i = lb.bit_length() - 1
        lowest_idx[mask] = i
        mask_wo_low[mask] = mask ^ lb

    # DP table: f[mask] is set of possible XORs for partitioning mask.
    f = [None] * M
    f[0] = {0}

    # Iterate masks from 1 to M-1
    for mask in range(1, M):
        base_bit = lowbit_mask[mask]
        rest_mask = mask_wo_low[mask]
        cur_set = set()
        sub = rest_mask
        # Enumerate all submasks of rest_mask
        while True:
            block = sub | base_bit
            rem = mask ^ block
            s_val = sum_sub[block]
            # Combine with all XORs of the remainder
            for x in f[rem]:
                cur_set.add(x ^ s_val)
            if sub == 0:
                break
            sub = (sub - 1) & rest_mask
        f[mask] = cur_set

    # Answer is size of f[M-1]
    print(len(f[M - 1]))

if __name__ == "__main__":
    main()