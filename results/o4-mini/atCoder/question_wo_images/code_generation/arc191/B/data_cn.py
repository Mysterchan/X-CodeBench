import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        N = int(data[idx]); K = int(data[idx+1])
        idx += 2
        bl = N.bit_length()
        # collect positions where N has 0 bit in [0..bl-1]
        zero_pos = []
        for i in range(bl):
            if not (N >> i) & 1:
                zero_pos.append(i)
        z = len(zero_pos)
        total = 1 << z
        if K > total:
            out.append("-1")
        else:
            r = 0
            k = K - 1
            # map bits of k to zero_pos
            for j in range(z):
                if (k >> j) & 1:
                    r |= (1 << zero_pos[j])
            out.append(str(N + r))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()