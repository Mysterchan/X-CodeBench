import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

M = 998244353
R = 3

# Precompute roots of unity for NTT
W = [pow(R, (M - 1) >> i, M) for i in range(24)]
Winv = [pow(w, M - 2, M) for w in W]

def butterfly(a):
    n = len(a)
    h = (n - 1).bit_length()
    a += [0] * (1 << h)  # pad to power of two
    n = 1 << h
    for ph in range(1, h + 1):
        w = Winv[ph]
        step = 1 << ph
        half = step >> 1
        for s in range(0, n, step):
            w_cur = 1
            for i in range(half):
                l = s + i
                r = s + i + half
                x = a[l]
                y = a[r]
                a[l] = (x + y) % M
                a[r] = (x - y) * w_cur % M
                w_cur = w_cur * w % M
    return a[:n]

def butterfly_inv(a):
    n = len(a)
    h = (n - 1).bit_length()
    a += [0] * (1 << h)
    n = 1 << h
    for ph in range(h, 0, -1):
        w = W[ph]
        step = 1 << ph
        half = step >> 1
        for s in range(0, n, step):
            w_cur = 1
            for i in range(half):
                l = s + i
                r = s + i + half
                x = a[l]
                y = a[r]
                a[l] = (x + y * w_cur) % M
                a[r] = (x - y * w_cur) % M
                w_cur = w_cur * w % M
    inv_n = pow(n, M - 2, M)
    for i in range(n):
        a[i] = a[i] * inv_n % M
    return a[:n]

def convolution(a, b):
    la = len(a)
    lb = len(b)
    lc = la + lb - 1
    size = 1 << ((lc - 1).bit_length())
    a += [0] * (size - la)
    b += [0] * (size - lb)
    fa = butterfly(a)
    fb = butterfly(b)
    for i in range(size):
        fa[i] = fa[i] * fb[i] % M
    c = butterfly_inv(fa)
    return c[:lc]

n = int(input())
s = input().strip()

# Prefix sums of W and B counts
cW = [0] * (2 * n + 1)
cB = [0] * (2 * n + 1)
for i in range(2 * n):
    cW[i + 1] = cW[i] + (s[i] == 'W')
    cB[i + 1] = cB[i] + (s[i] == 'B')

N = 2 * n

# Precompute factorials and inverse factorials
fa = [1] * (N + 1)
for i in range(1, N + 1):
    fa[i] = fa[i - 1] * i % M
fb = [1] * (N + 1)
fb[N] = pow(fa[N], M - 2, M)
for i in range(N - 1, -1, -1):
    fb[i] = fb[i + 1] * (i + 1) % M

q = [0] * (N + 1)
q[0] = -1 % M

def f(l, r):
    w = r - l + 1
    if w == 1:
        return
    mid = l + w // 2 - 1
    f(l, mid)

    ql = [0] * (w // 2 + 1)
    baseB = cB[l]
    for i in range(l, mid + 1):
        j = cB[i] - baseB
        ql[j] = (ql[j] + q[i]) % M

    d = cW[l] - cB[l]
    # Prepare qr array for convolution
    # qr[i] = fa[i + d] if i + d >= 0 else 0 for i in range(-w, w)
    # We'll build qr for indices 0..2w-1 corresponding to i in [-w, w-1]
    qr = []
    for i in range(-w, w):
        idx = i + d
        if 0 <= idx <= N:
            qr.append(fa[idx])
        else:
            qr.append(0)

    nq = convolution(ql, qr)

    baseW = cW[l]
    baseDiff = cW[l] - cB[l]
    for i in range(mid + 1, r + 1):
        j1 = cB[i] - baseB
        j2 = cW[i] - cB[i]
        if j2 >= 0:
            val = nq[w + j1] * fb[j2] % M
            q[i] = (q[i] - val) % M

    f(mid + 1, r)

f(0, N)
print(q[N] % M)