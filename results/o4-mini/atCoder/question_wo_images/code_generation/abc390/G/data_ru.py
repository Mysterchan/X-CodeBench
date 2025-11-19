import threading
import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    mod = 998244353
    root = 3

    def ntt(a, invert):
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
        while length <= n:
            wlen = pow(root, (mod - 1) // length, mod)
            if invert:
                wlen = pow(wlen, mod - 2, mod)
            for i in range(0, n, length):
                w = 1
                half = length >> 1
                for j in range(i, i + half):
                    u = a[j]
                    v = a[j + half] * w % mod
                    a[j] = u + v if u + v < mod else u + v - mod
                    a[j + half] = u - v if u >= v else u - v + mod
                    w = w * wlen % mod
            length <<= 1
        if invert:
            inv_n = pow(n, mod - 2, mod)
            for i in range(n):
                a[i] = a[i] * inv_n % mod

    def convolution(a, b):
        na = len(a); nb = len(b)
        if not na or not nb:
            return []
        n = na + nb - 1
        lim = 1
        while lim < n:
            lim <<= 1
        fa = a + [0] * (lim - na)
        fb = b + [0] * (lim - nb)
        ntt(fa, False); ntt(fb, False)
        for i in range(lim):
            fa[i] = fa[i] * fb[i] % mod
        ntt(fa, True)
        return fa[:n]

    input = sys.stdin.readline
    N_line = input().strip()
    if not N_line:
        N_line = input().strip()
    N = int(N_line)
    # Group by digit length
    groups = []
    pow10 = [1] * 8
    for i in range(1, 8):
        pow10[i] = pow10[i - 1] * 10
    maxd = len(str(N))
    for d in range(1, maxd + 1):
        L = pow10[d - 1]
        R = min(pow10[d] - 1, N)
        if L > R:
            continue
        c = R - L + 1
        v = pow(10, d, mod)
        groups.append((d, L, R, c, v))
    D = len(groups)
    # Precompute factorials
    maxN = N
    fact = [1] * (maxN + 1)
    for i in range(1, maxN + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact = [1] * (maxN + 1)
    invfact[maxN] = pow(fact[maxN], mod - 2, mod)
    for i in range(maxN, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod
    # Build polynomials
    polys = []
    for (d, L, R, c, v) in groups:
        p = [0] * (c + 1)
        # compute v^j iteratively
        cur = 1
        fc = fact[c]
        for j in range(0, c + 1):
            # C(c, j) * v^j
            p[j] = fc * invfact[j] % mod * invfact[c - j] % mod * cur % mod
            cur = cur * v % mod
        polys.append(p)
    # Multiply all polys via divide and conquer
    def dc(l, r):
        if l == r:
            return polys[l]
        m = (l + r) >> 1
        left = dc(l, m)
        right = dc(m + 1, r)
        return convolution(left, right)

    E = dc(0, D - 1)  # length N+1
    # Precompute A[m] = m! * (N-1-m)! for m=0..N-1
    A = [0] * N
    for m in range(0, N):
        A[m] = fact[m] * fact[N - 1 - m] % mod
    inv2 = (mod + 1) // 2
    answer = 0
    # For each group, compute H and S_d and ksum
    for (d, L, R, c, v) in groups:
        # Compute H[0..N-1]
        H0 = [0] * N
        H0[0] = 1  # E[0] == 1
        for m in range(1, N):
            # H[m] = E[m] - v * H[m-1]
            val = E[m] - v * H0[m - 1] % mod
            H0[m] = val + mod if val < 0 else val
        # Compute S_d
        Sd = 0
        for m in range(0, N):
            Sd = (Sd + H0[m] * A[m]) % mod
        # Compute ksum for k in [L..R]
        cnt = c
        ksum = (L + R) % mod * cnt % mod * inv2 % mod
        answer = (answer + ksum * Sd) % mod
    print(answer)

if __name__ == "__main__":
    main()