import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))

    # Fenwick Tree (BIT) to track empty slots: 1 means empty, 0 means occupied
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        # Initialize so that tree[i] = sum of a[i - lowbit(i) + 1 .. i] = lowbit(i)
        tree[i] = i & -i

    def add(idx, val):
        # Add 'val' at position idx
        while idx <= N:
            tree[idx] += val
            idx += idx & -idx

    def find_kth(k):
        # Find the smallest index idx such that the prefix sum up to idx is >= k
        idx = 0
        curr_sum = 0
        # Start from the largest power of two <= N
        bit = 1 << (N.bit_length() - 1)
        while bit:
            nxt = idx + bit
            if nxt <= N and curr_sum + tree[nxt] < k:
                curr_sum += tree[nxt]
                idx = nxt
            bit >>= 1
        return idx + 1

    # Result array
    A = [0] * N

    # Process insertions in reverse: i = N down to 1
    for i in range(N, 0, -1):
        k = P[i - 1]          # We want the k-th empty slot
        pos = find_kth(k)     # Find its actual index in [1..N]
        A[pos - 1] = i        # Place i there (0-based in A)
        add(pos, -1)          # Mark this slot as occupied

    # Output the final array
    print(" ".join(map(str, A)))

if __name__ == "__main__":
    main()