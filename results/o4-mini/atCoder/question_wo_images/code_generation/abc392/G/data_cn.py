import sys
import threading
def main():
    import sys, math
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    S = list(map(int, data[1:1+n]))
    # Determine maximum value in S
    M = 0
    for v in S:
        if v > M: M = v
    size = 1
    while size <= 2 * M:
        size <<= 1

    # Prepare the array for FFT: f[x] = 1 if x in S else 0
    f = [0] * size
    for v in S:
        f[v] = 1

    # Bit-reversed permutation preparation
    log_n = size.bit_length() - 1
    rev = [0] * size
    for i in range(1, size):
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (log_n - 1))
    for i in range(size):
        j = rev[i]
        if i < j:
            f[i], f[j] = f[j], f[i]

    # Cooley-Tukey FFT
    PI2 = 2 * math.pi
    half = 1
    while half < size:
        length = half << 1
        angle = PI2 / length
        # roots of unity for this stage
        wlen = complex(math.cos(angle), math.sin(angle))
        for i in range(0, size, length):
            w = 1+0j
            # butterfly
            for j in range(i, i + half):
                u = f[j]
                v = f[j + half] * w
                f[j] = u + v
                f[j + half] = u - v
                w *= wlen
        half = length

    # Point-wise square (since we want convolution of f with itself)
    for i in range(size):
        f[i] *= f[i]

    # Inverse FFT
    half = 1
    while half < size:
        length = half << 1
        angle = -PI2 / length
        wlen = complex(math.cos(angle), math.sin(angle))
        for i in range(0, size, length):
            w = 1+0j
            for j in range(i, i + half):
                u = f[j]
                v = f[j + half] * w
                f[j] = u + v
                f[j + half] = u - v
                w *= wlen
        half = length
    # Divide all by size
    inv_n = 1.0 / size
    for i in range(size):
        f[i] *= inv_n

    # Now f[t].real is the count of ordered pairs (a,c) with a+c = t
    # For each B in S, we look at t = 2*B. We subtract the (B,B) pair (count=1),
    # then divide by 2 to get the number of valid (A,C) with A<C and A+C=2B.
    total = 0
    res = 0
    for B in S:
        t = 2 * B
        if t < size:
            cnt = int(f[t].real + 0.5)
            # remove the (B,B) self-pair, then half
            res += (cnt - 1) // 2
    # Print result
    sys.stdout.write(str(res))

if __name__ == "__main__":
    main()