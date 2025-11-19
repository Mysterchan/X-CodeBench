M = 998244353
R = 3
W = [pow(R, (M - 1) >> i, M) for i in range(24)]
Winv = [pow(w, M - 2, M) for w in W]

def butterfly(a, L):
    l = L.bit_length() - 1
    width = L
    for i in reversed(range(1, l + 1)):
        w = 1
        half = width >> 1
        winv = Winv[i]
        for left in range(0, L, width):
            for j in range(half):
                p1 = left + j
                p2 = p1 + half
                v1 = a[p1]
                v2 = a[p2]
                a[p1] = (v1 + v2) % M
                a[p2] = (v1 - v2) * w % M
                w = w * winv % M
        width = half

def butterfly_inv(a, L):
    l = L.bit_length() - 1
    width = 2
    for i in range(1, l + 1):
        w = 1
        half = width >> 1
        wi = W[i]
        for left in range(0, L, width):
            for j in range(half):
                p1 = left + j
                p2 = p1 + half
                v1 = a[p1]
                v2 = a[p2]
                wv2 = v2 * w % M
                a[p1] = (v1 + wv2) % M
                a[p2] = (v1 - wv2) % M
                w = w * wi % M
        width <<= 1
    Linv = pow(L, M - 2, M)
    for i in range(L):
        a[i] = a[i] * Linv % M

def convolution(a, b):
    la = len(a)
    lb = len(b)
    lc = la + lb - 1
    L = 1 << (lc - 1).bit_length()
    fa = a + [0] * (L - la)
    fb = b + [0] * (L - lb)
    butterfly(fa, L)
    butterfly(fb, L)
    for i in range(L):
        fa[i] = fa[i] * fb[i] % M
    butterfly_inv(fa, L)
    return fa[:lc]

n = int(input())
s = input()
N = 2 * n

cw = [0]
cb = [0]
for ch in s:
    cw.append(cw[-1] + (ch == "W"))
    cb.append(cb[-1] + (ch == "B"))

fa = [1] * (N + 1)
for i in range(1, N + 1):
    fa[i] = fa[i - 1] * i % M

fb = [0] * (N + 1)
fb[N] = pow(fa[N], M - 2, M)
for i in range(N - 1, -1, -1):
    fb[i] = fb[i + 1] * (i + 1) % M

q = [0] * (N + 1)
q[0] = M - 1

def f(l, r):
    w = r - l + 1
    if w == 1:
        return
    mid = l + (w >> 1) - 1
    f(l, mid)
    
    half = (w >> 1) + 1
    ql = [0] * half
    for i in range(l, mid + 1):
        j = cb[i] - cb[l]
        ql[j] = (ql[j] + q[i]) % M
    
    d = cw[l] - cb[l]
    qr = [fa[i + d] if i + d >= 0 else 0 for i in range(-w, w)]
    
    nq = convolution(ql, qr)
    
    for i in range(mid + 1, r + 1):
        j1 = cw[i] - cw[l]
        j2 = cw[i] - cb[i]
        if j2 >= 0:
            q[i] = (q[i] - nq[w + j1] * fb[j2]) % M
    
    f(mid + 1, r)

f(0, N)
print(q[N])