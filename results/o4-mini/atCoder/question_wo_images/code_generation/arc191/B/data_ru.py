import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1

        # Determine bit‐positions < msb of N where N has a 0.
        msb = N.bit_length() - 1
        zeros = []
        for b in range(msb):
            if not (N >> b) & 1:
                zeros.append(b)
        c0 = len(zeros)
        total = 1 << c0
        if K > total:
            out.append("-1")
        else:
            m = 0
            k1 = K - 1
            # Build the (K-1)th mask in those zero positions
            for j in range(c0):
                if (k1 >> j) & 1:
                    m |= 1 << zeros[j]
            out.append(str(N + m))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()