from sys import stdin
input = lambda: stdin.readline().rstrip()

N = 400000
Q = 400000

cc = [''] * Q
uu = [0] * Q
vv = [0] * Q
zz = [0] * Q
xx = [0] * Q
yy = [0] * Q
ii = [0] * Q
jj = [0] * Q
ll = [0] * Q
rr = [0] * Q
hh = [0] * Q
ds = [-1] * Q
k = 0
ii_ = [0] * Q
dsi = [0] * Q
jj_ = [0] * Q
dsj = [0] * Q
kk = [0] * Q
cnt = 0

def find(i):
    if ds[i] < 0:
        return i
    return find(ds[i])

def join(i, j):
    global cnt, k
    i = find(i)
    j = find(j)
    ii_[cnt] = i
    dsi[cnt] = ds[i]
    jj_[cnt] = j
    dsj[cnt] = ds[j]
    kk[cnt] = k
    cnt += 1
    if i == j:
        return
    if ds[i] == ds[j]:
        ds[i] -= 1
    if ds[i] < ds[j]:
        i, j = j, i
    ds[i] = j
    k -= 1

def undo():
    global cnt, k
    cnt -= 1
    ds[ii_[cnt]] = dsi[cnt]
    ds[jj_[cnt]] = dsj[cnt]
    k = kk[cnt]

def dc(l, r, hh, m, xx):
    g0 = 0
    g1 = 0
    g2 = m
    while g1 < g2:
        if ll[hh[g1]] <= l and r <= rr[hh[g1]]:
            g1 += 1
        elif rr[hh[g1]] <= l or r <= ll[hh[g1]]:
            hh[g1], hh[g2 - 1] = hh[g2 - 1], hh[g1]
            g2 -= 1
        else:
            hh[g0], hh[g1] = hh[g1], hh[g0]
            g0 += 1
            g1 += 1
    for g in range(g0, g1):
        join(ii[hh[g]], jj[hh[g]])
    if r - l == 1:
        xx[l] = k
    else:
        z = (l + r) // 2
        dc(l, z, hh, g0, xx)
        dc(z, r, hh, g0, xx)
    for g in range(g0, g1):
        undo()

def solve(ab, n, q, xx):
    global k, cnt
    m = 0
    for c in ['A', 'B']:
        if c == 'A' or ab:
            q_ = 0
            for z in range(q):
                if cc[z] == c:
                    zz[q_] = z
                    q_ += 1
            zz[:q_] = sorted(zz[:q_], key=lambda z0: (uu[z0], vv[z0], z0))
            yl = 0
            while yl < q_:
                i = uu[zz[yl]]
                j = vv[zz[yl]]
                yr = yl + 1
                while yr < q_ and uu[zz[yr]] == i and vv[zz[yr]] == j:
                    yr += 1
                for y in range(yl, yr, 2):
                    ii[m] = i
                    jj[m] = j
                    ll[m] = zz[y]
                    rr[m] = zz[y + 1] if y + 1 < yr else q
                    m += 1
                yl = yr
    for g in range(m):
        hh[g] = g
    for i in range(n):
        ds[i] = -1
    k = n
    dc(0, q, hh, m, xx)

def main():
    n, q = map(int, input().split())
    for i in range(q):
        c, u, v = input().split()
        u = int(u) - 1
        v = int(v) - 1
        if u > v:
            u, v = v, u
        cc[i] = c
        uu[i] = u
        vv[i] = v
    solve(False, n, q, xx)
    solve(True, n, q, yy)
    for z in range(q):
        print(xx[z] - yy[z])

if __name__ == "__main__":
    main()
