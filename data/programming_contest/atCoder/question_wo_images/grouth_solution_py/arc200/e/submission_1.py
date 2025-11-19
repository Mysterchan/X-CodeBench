mod = 998244353
two_inv = pow(2, mod - 2, mod)
six_inv = pow(6, mod - 2, mod)

def c2(n):
    return n * (n - 1) % mod * two_inv % mod

def c3(n):
    return n * (n - 1) % mod * (n - 2) % mod * six_inv % mod

def solve(n, m):
    n2 = pow(2, n - 1, mod)
    n3 = pow(3, n - 1, mod)
    n4 = pow(4, n - 1, mod)
    nm1 = pow(m + 1, n - 1, mod)
    ans = 0

    ans += nm1

    ans += c2(m) * (n4 - n3) % mod

    ko = n4 - 3 * n3 + 3 * n2 - 1
    ans += c3(m) * ko % mod

    ko = nm1 - n2 - (m - 1) * (n3 - n2)
    ans += m * ko % mod
    ans %= mod
    ans *= pow(2, m, mod)
    ans %= mod
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n, m))