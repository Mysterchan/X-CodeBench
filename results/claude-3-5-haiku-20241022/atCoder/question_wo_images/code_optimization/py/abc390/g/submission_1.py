def main():
    import sys
    N = int(sys.stdin.read().strip())
    mod = 998244353

    # Group numbers by digit count
    groups = []
    d = 1
    low = 1
    while low <= N:
        high = min(N, 10**d - 1)
        if low <= high:
            cnt = high - low + 1
            s = (low + high) * cnt // 2 % mod
            X = pow(10, d, mod)
            groups.append((cnt, X, s))
        d += 1
        low = 10**(d-1)

    # NTT implementation
    def ntt(a, inv=False):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j ^= bit
            if i < j:
                a[i], a[j] = a[j], a[i]
        
        length = 2
        root = 3 if not inv else pow(3, mod-2, mod)
        while length <= n:
            wlen = pow(root, (mod - 1) // length, mod)
            for i in range(0, n, length):
                w = 1
                half = length >> 1
                for j in range(i, i + half):
                    u = a[j]
                    v = a[j + half] * w % mod
                    a[j] = (u + v) % mod
                    a[j + half] = (u - v) % mod
                    w = w * wlen % mod
            length <<= 1
        
        if inv:
            inv_n = pow(n, mod-2, mod)
            for i in range(n):
                a[i] = a[i] * inv_n % mod

    def conv(a, b):
        n = len(a) + len(b) - 1
        size = 1
        while size < n:
            size <<= 1
        A = a + [0] * (size - len(a))
        B = b + [0] * (size - len(b))
        ntt(A, False)
        ntt(B, False)
        for i in range(size):
            A[i] = A[i] * B[i] % mod
        ntt(A, True)
        return A[:n]

    # Build generating function
    Fpoly = [1]
    inv_cache = {}
    
    for cnt, X, s in groups:
        poly = [1]
        coeff = 1
        Xpow = X
        for j in range(1, cnt + 1):
            if j not in inv_cache:
                inv_cache[j] = pow(j, mod-2, mod)
            coeff = coeff * (cnt - j + 1) % mod * inv_cache[j] % mod
            poly.append(coeff * Xpow % mod)
            if j < cnt:
                Xpow = Xpow * X % mod
        Fpoly = conv(Fpoly, poly)

    # Compute dp2
    nF = len(Fpoly)
    dp2 = [0] * nF
    
    for cnt, X, Sval in groups:
        if cnt < 1:
            continue
        
        Q = [0] * (nF - 1)
        Q[0] = Fpoly[0]
        for i in range(nF - 2):
            Q[i + 1] = (Fpoly[i + 1] - X * Q[i]) % mod
        
        coeff = Sval * X % mod
        for i in range(1, nF):
            dp2[i] = (dp2[i] + coeff * Q[i - 1]) % mod

    # Compute final result
    T = N * (N + 1) // 2 % mod
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    
    res = 0
    for r in range(N):
        ways = fact[r] * fact[N - 1 - r] % mod
        val = (Fpoly[r] * T - dp2[r]) % mod
        res = (res + ways * val) % mod
    
    print(res)

if __name__ == '__main__':
    main()