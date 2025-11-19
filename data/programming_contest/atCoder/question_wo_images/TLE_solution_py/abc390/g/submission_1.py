def main():
    import sys,sys
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    mod = 998244353

    groups = []
    low = 1
    d = 1
    while low <= N:
        high = min(N, 10**d - 1)
        if low <= high:
            cnt = high - low + 1

            s = (low + high) * cnt // 2
            s %= mod

            X = pow(10, d, mod)
            groups.append((cnt, X, s))
        d += 1
        low = 10**(d-1)

    def ntt(a, inv=False):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j -= bit
                bit //= 2
            j += bit
            if i < j:
                a[i], a[j] = a[j], a[i]
        length = 2
        root = 3
        if inv:
            root = pow(root, mod-2, mod)
        while length <= n:
            step = (mod - 1) // length
            wlen = pow(root, step, mod)
            for i in range(0, n, length):
                w = 1
                for j in range(i, i + length//2):
                    u = a[j]
                    v = a[j+length//2] * w % mod
                    a[j] = (u+v) % mod
                    a[j+length//2] = (u-v) % mod
                    w = w * wlen % mod
            length *= 2
        if inv:
            inv_n = pow(n, mod-2, mod)
            for i in range(n):
                a[i] = a[i] * inv_n % mod

    def conv(a, b):

        n = len(a) + len(b) - 1
        size = 1
        while size < n:
            size *= 2
        A = a[:] + [0]*(size - len(a))
        B = b[:] + [0]*(size - len(b))
        ntt(A, inv=False)
        ntt(B, inv=False)
        for i in range(size):
            A[i] = A[i] * B[i] % mod
        ntt(A, inv=True)
        return A[:n]

    def make_poly(cnt, X):
        poly = [1]*(cnt+1)
        poly[0] = 1
        for j in range(1, cnt+1):
            poly[j] = poly[j-1] * (cnt - j + 1) % mod
            poly[j] = poly[j] * pow(j, mod-2, mod) % mod
            poly[j] = poly[j] * X % mod
        return poly

    Fpoly = [1]
    for (cnt, X, s) in groups:
        poly_d = make_poly(cnt, X)
        Fpoly = conv(Fpoly, poly_d)

    dp2 = [0] * (len(Fpoly))
    for (cnt, X, Sval) in groups:
        if cnt < 1:
            continue
        nF = len(Fpoly)
        Q = [0]*(nF-1)
        Q[0] = Fpoly[0]
        for i in range(nF-2):
            Q[i+1] = (Fpoly[i+1] - X * Q[i]) % mod

        H = [0]*nF
        for i in range(1, nF):
            H[i] = Sval * X % mod
            H[i] = H[i] * Q[i-1] % mod
        for i in range(nF):
            dp2[i] = (dp2[i] + H[i]) % mod

    T = (N*(N+1)//2) % mod
    fact = [1]*(N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1]*i % mod
    res = 0
    for r in range(0, N):
        ways = fact[r] * fact[N-1-r] % mod
        val = (Fpoly[r]*T - dp2[r]) % mod
        res = (res + ways * val) % mod
    sys.stdout.write(str(res % mod))

if __name__ == '__main__':
    main()