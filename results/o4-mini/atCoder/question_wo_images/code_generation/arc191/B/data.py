import sys
import threading

def main():
    import sys

    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1])
        idx += 2

        # Find positions of zero-bits in n (from LSB=0 up to MSB-1).
        bl = n.bit_length()
        zero_pos = []
        # For each bit position i in [0..bl-1], if n has a 0 there, it's a free bit.
        for i in range(bl):
            if not (n >> i) & 1:
                zero_pos.append(i)

        z = len(zero_pos)
        # Total number of compatible X is 2^z.
        # If k is larger, impossible.
        if k > (1 << z):
            out.append("-1")
            continue

        # The k-th smallest r (where r = X - n) corresponds to (k-1) in binary
        # mapped onto the zero-bit positions.
        r = 0
        k_minus_1 = k - 1
        for j, pos in enumerate(zero_pos):
            if (k_minus_1 >> j) & 1:
                r |= (1 << pos)

        # The result X is n + r
        x = n + r
        out.append(str(x))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()