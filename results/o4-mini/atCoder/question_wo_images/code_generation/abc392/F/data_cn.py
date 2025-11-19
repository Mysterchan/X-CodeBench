import sys
import threading

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    P = list(map(int, data[1:]))

    # Fenwick tree (BIT) of size n, initialized with 1s.
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = i & -i

    # Result array
    res = [0] * (n + 1)

    # Precompute highest power of two ≤ n for find-kth routine
    max_bit = 1 << (n.bit_length() - 1)

    # Process in reverse: place i into the P[i-1]-th empty slot
    for i in range(n, 0, -1):
        k = P[i-1]
        idx = 0
        b = max_bit
        # Find the position pos so that it's the k-th '1' in the BIT
        while b:
            t = idx + b
            if t <= n and bit[t] < k:
                idx = t
                k -= bit[t]
            b >>= 1
        pos = idx + 1

        res[pos] = i
        # Mark this slot as filled (decrement the BIT at pos by 1)
        j = pos
        while j <= n:
            bit[j] -= 1
            j += j & -j

    # Output the result
    out = ' '.join(map(str, res[1:]))
    sys.stdout.write(out)

if __name__ == "__main__":
    main()