import sys
import threading
def main():
    import sys, math
    data = sys.stdin.read().split()
    N = int(data[0])
    S = list(map(int, data[1:]))
    if N == 0:
        print(0)
        return
    maxv = max(S)
    size = 1
    need = maxv * 2 + 1
    while size < need:
        size <<= 1

    # build indicator array
    a = [0.0] * size
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

    # prepare complex array
    fa = list(map(complex, a))
    fft(fa, False)
    for i in range(size):
        fa[i] *= fa[i]
    fft(fa, True)

    # count triples
    present = set(S)
    ans = 0
    # for each b in S, number of unordered (a,c): (fa[2b] - 1)//2
    for b in S:
        cnt = int(fa[2*b].real + 0.5)
        # subtract the (b,b) pair, then divide by 2
        ans += (cnt - 1) // 2
    print(ans)

if __name__ == "__main__":
    main()