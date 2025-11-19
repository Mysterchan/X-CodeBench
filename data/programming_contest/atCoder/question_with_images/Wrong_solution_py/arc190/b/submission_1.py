import sys
input = sys.stdin.readline

mod = 998244353

def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        b //= 2
    return res

def inverse(a):
    return power(a, mod - 2)

def main():
    N, a, b = map(int, input().split())
    Q = int(input())
    K = list(map(int, input().split()))

    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod

    invfact = [1] * (N + 1)
    invfact[N] = inverse(fact[N])
    for i in range(N - 1, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % mod

    def choose(n, k):
        return fact[n] * invfact[k] % mod * invfact[n - k] % mod

    def ways(k):
        if k < a or k < b or k < N - a + 1 or k < N - b + 1:
            return 0
        return 4 * choose(k - a, b - 1) % mod * choose(k - b, a - 1) % mod * choose(N - k + a - 1, N - k + 1) % mod * choose(N - k + b - 1, N - k + 1) % mod

    ans = [0] * Q
    ans[0] = ways(K[0])
    for i in range(1, Q):
        ans[i] = (ans[i - 1] + ways(K[i])) % mod

    for i in range(Q):
        print(ans[i])

if __name__ == "__main__":
    main()