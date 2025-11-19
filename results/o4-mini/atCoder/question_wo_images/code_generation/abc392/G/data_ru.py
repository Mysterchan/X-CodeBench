import sys
import threading
def main():
    import sys, math
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    S = list(map(int, (next(it) for _ in range(n))))
    if n < 3:
        print(0)
        return
    maxv = 0
    for x in S:
        if x > maxv: maxv = x
    size = 1
    while size <= 2 * maxv:
        size <<= 1
    # prepare array
    a = [0] * size
    for x in S:
        a[x] = 1.0
    # FFT
    def fft(a, invert):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j |= bit
            if i < j:
                a[i], a[j] = a[j], a[i]
        length = 2
        pi = math.pi
        while length <= n:
            ang = 2 * pi / length * (-1 if invert else 1)
            wlen = complex(math.cos(ang), math.sin(ang))
            for i in range(0, n, length):
                w = 1+0j
                half = length >> 1
                for j in range(i, i + half):
                    u = a[j]
                    v = a[j + half] * w
                    a[j] = u + v
                    a[j + half] = u - v
                    w *= wlen
            length <<= 1
        if invert:
            inv_n = 1.0 / n
            for i in range(n):
                a[i] *= inv_n

    # convert to complex
    a = [complex(val, 0) for val in a]
    fft(a, False)
    for i in range(size):
        a[i] *= a[i]
    fft(a, True)
    # a[k].real ~ convolution at k
    result = 0
    # round and sum
    for x in S:
        idx = 2 * x
        if idx < len(a):
            cnt = int(a[idx].real + 0.5)
            # remove the (x,x) pair and half
            result += (cnt - 1) // 2
    print(result)

if __name__ == "__main__":
    main()