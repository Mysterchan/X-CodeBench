import sys
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(1000000)
import cmath
import sys

def fft(x, inv=False):
    n = len(x)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            x[i], x[j] = x[j], x[i]

    h = 1
    while h < n:
        angle = 2 * cmath.pi / (2 * h) * (-1 if inv else 1)
        wlen = cmath.exp(1j * angle)
        for i in range(0, n, 2 * h):
            w = 1.0
            for j1 in range(i, i + h):
                t = w * x[j1 + h]
                u = x[j1]
                x[j1] = u + t
                x[j1 + h] = u - t
                w *= wlen
        h <<= 1

    if inv:
        for i in range(n):
            x[i] /= n

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    n = int(data[0])
    S = list(map(int, data[1:1 + n]))

    if n < 3:
        print(0)
        return

    actual_max = max(S)
    size_fft = 1
    while size_fft < 2 * actual_max + 1:
        size_fft *= 2

    f_complex = [complex(0, 0)] * size_fft
    for x in S:
        f_complex[x] = complex(1, 0)

    fft(f_complex)

    g_complex = [a * a for a in f_complex]

    fft(g_complex, inv=True)

    g_real = [round(x.real) for x in g_complex]

    total_count = 0
    for B in S:
        k = 2 * B
        total_ordered = g_real[k]
        if total_ordered < 1:
            count_here = 0
        else:
            count_here = (total_ordered - 1) // 2
        total_count += count_here

    print(total_count)

if __name__ == '__main__':
    main()