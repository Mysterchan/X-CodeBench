import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    mod = 998244353
    W, H, L, R, D, U = map(int, sys.stdin.readline().split())
    # Convert to N = W+1 columns, M = H+1 rows
    N = W + 1
    M = H + 1
    # Precompute factorials up to N+M+2
    maxn = N + M + 2
    fact = [1] * (maxn + 1)
    for i in range(1, maxn + 1):
        fact[i] = fact[i-1] * i % mod
    invfact = [1] * (maxn + 1)
    invfact[maxn] = pow(fact[maxn], mod-2, mod)
    for i in range(maxn, 0, -1):
        invfact[i-1] = invfact[i] * i % mod
    def comb(n, k):
        if k < 0 or k > n or n < 0:
            return 0
        return fact[n] * invfact[k] % mod * invfact[n-k] % mod
    # solve0(N, M) = total paths in full grid N x M
    def solve0(n, m):
        # sum of comb(dx+dy, dx) over all start (x1,y1) and end (x2>=x1,y2>=y1)
        # Known formula: C(n+m+2, n+1) - n*m -2 -n -m
        res = comb(n+m+2, n+1)
        res = (res - n*m - 2 - n - m) % mod
        return res
    # solve1(n, m) = number of non-empty paths in full n x m grid starting at (0,0)
    # except the trivial zero-step path removed => sum_{dx,dy>=0, not both zero} C(dx+dy, dx)
    # = C(n+m, n) - 1
    def solve1(n, m):
        return (comb(n+m, n) - 1) % mod
    # Initial answer: full grid
    ans = solve0(N, M)
    # Subtract contributions of paths that go through the forbidden rectangle using inclusion-exclusion
    # First subtract those that cross vertical strip [L..R]
    s = 0
    for x in range(L, R+1):
        a = x+1; b = D
        t1 = solve1(a, b)
        c = N - x; d = M - D
        t2 = solve1(c, d)
        s = (s + t1 * t2) % mod
    ans = (ans - s) % mod
    # Then subtract those that cross horizontal strip [D..U]
    s = 0
    for y in range(D, U+1):
        a = y+1; b = L
        t1 = solve1(a, b)
        c = M - y; d = N - L
        t2 = solve1(c, d)
        s = (s + t1 * t2) % mod
    ans = (ans - s) % mod
    # Finally subtract those that cross the hole completely (double count)
    # Compute double sum_{x=L..R, y=D..U} solve1(N-x, M-y)
    # Let u = N-x in [A..B], v = M-y in [C..D']
    A = N - R
    B = N - L
    C = M - U
    Dp = M - D
    # S1 = sum_{u=A..B} sum_{v=C..Dp} C(u+v, u)
    # Use identity: sum_{i=0..a, j=0..b} C(i+j,i) = C(a+b+2,a+1) - 1
    # Then apply inclusion-exclusion on ranges
    def sum_bin(a, b):
        # sum_{i=0..a, j=0..b} C(i+j, i)
        if a < 0 or b < 0:
            return 0
        return (comb(a+b+2, a+1) - 1) % mod
    # Using F = C(x+y+2,x+1)-1 form gives:
    # S1 = comb(B+Dp+2, B+1) - comb((A-1)+Dp+2, A) - comb(B+(C-1)+2, B+1) + comb((A-1)+(C-1)+2, A)
    t1 = comb(B+Dp+2, B+1)
    t2 = comb((A-1)+Dp+2, A)    # when A=0 gives comb(Dp+1,0)=1 correctly
    t3 = comb(B+(C-1)+2, B+1)   # when C=0 gives comb(B+1,B+1)=1
    t4 = comb((A-1)+(C-1)+2, A) # last term
    S1 = (t1 - t2 - t3 + t4) % mod
    # S0 = number of terms = (B-A+1)*(Dp-C+1)
    S0 = (B - A + 1) * (Dp - C + 1) % mod
    double_sum = (S1 - S0) % mod
    ans = (ans - double_sum) % mod
    print(ans)

if __name__ == "__main__":
    main()