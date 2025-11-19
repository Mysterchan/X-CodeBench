from collections import defaultdict

def naive(n, m):
    from itertools import product

    def check(aaa):
        diff_bits = 0
        for i in range(n):
            for j in range(n):
                xor = aaa[i] ^ aaa[j]
                if xor.bit_count() > 2:
                    return -1
                diff_bits |= xor
        return diff_bits.bit_count()

    sample = defaultdict(list)
    for aaa in product(range(1 << m), repeat=n):
        d = check(aaa)
        if d == -1:
            continue
        sample[d].append(aaa)

    ans = 0
    for d in sorted(sample.keys()):
        print(f'{d=} l={len(sample[d])} {sample[d][:5]=}')
        ans += len(sample[d])
    print(f'{ans=}')

def solve():
    MOD = 998244353
    INV2 = pow(2, -1, MOD)

    def main(n, m):

        ans = pow(m + 1, n - 1, MOD)

        tmp = pow(m + 1, n - 1, MOD)
        tmp -= pow(2, n - 1, MOD)
        tmp -= (pow(2, n - 1, MOD) - 1) * (m - 1) * INV2
        ans += tmp * m
        ans %= MOD

        if n >= 4:

            tmp = pow(4, n - 1, MOD)
            tmp -= pow(3, n - 1, MOD) * 3
            tmp += pow(2, n - 1, MOD) * 3
            tmp -= 1
            mC3 = m * (m - 1) * (m - 2) // 6
            mC2 = m * (m - 1) // 2
            ans += tmp * (mC3 + mC2)
            ans %= MOD

        ans *= pow(2, m, MOD)
        ans %= MOD

        return ans

    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        ans = main(n, m)
        print(ans)

solve()