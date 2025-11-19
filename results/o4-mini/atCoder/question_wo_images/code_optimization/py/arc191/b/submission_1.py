import sys
import threading

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    ans = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1])
        idx += 2

        # bit-length of n
        d = n.bit_length()
        # gather positions of zero‐bits in n (from least to most significant)
        zero_pos = []
        for b in range(d):
            if not (n >> b) & 1:
                zero_pos.append(b)
        t0 = len(zero_pos)
        # total compatibles = 2^t0
        if k > (1 << t0):
            ans.append("-1")
            continue

        # form the (k-1)-th mask over zero‐bit positions
        mask = k - 1
        r = 0
        for i in range(t0):
            if (mask >> i) & 1:
                r |= (1 << zero_pos[i])

        # X = n + r
        ans.append(str(n + r))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()