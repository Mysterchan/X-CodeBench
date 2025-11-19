import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    S = list(map(int, data[1:]))
    if n < 3:
        print(0)
        return

    m = max(S)
    size = 1
    while size <= 2*m:
        size <<= 1

    # Build the indicator array
    A = [0.0] * size
    for x in S:
        A[x] = 1.0

    # Iterative in-place FFT
    from math import pi, cos, sin
    def fft(a, invert):
        n = len(a)
        j = 0
        # bit-reversal permutation
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j |= bit
            if i < j:
                a[i], a[j] = a[j], a[i]
        length = 2
        while length <= n:
            ang = 2 * pi / length * (-1 if invert else 1)
            wlen = complex(cos(ang), sin(ang))
            for i in range(0, n, length):
                w = 1+0j
                half = length >> 1
                for k in range(half):
                    u = a[i + k]
                    v = a[i + k + half] * w
                    a[i + k] = u + v
                    a[i + k + half] = u - v
                    w *= wlen
            length <<= 1
        if invert:
            inv_n = 1.0 / n
            for i in range(n):
                a[i] *= inv_n

    # Prepare complex array
    fa = list(map(complex, A))
    # Forward FFT
    fft(fa, False)
    # Point-wise square (convolution with itself)
    for i in range(size):
        fa[i] *= fa[i]
    # Inverse FFT
    fft(fa, True)

    # Round the real parts to nearest integers
    # conv[s] = number of ordered pairs (x,y) in S with x+y = s
    # For each B in S, number of ways to pick A<C with A+C=2B is (conv[2B] - 1)//2
    res = fa  # reuse array
    ans = 0
    for B in S:
        s = int(2*B)
        cnt = int(res[s].real + 0.5)
        # subtract the (B,B) pair, then divide by 2 to get unordered A<C
        ans += (cnt - 1) // 2
    print(ans)

if __name__ == "__main__":
    main()