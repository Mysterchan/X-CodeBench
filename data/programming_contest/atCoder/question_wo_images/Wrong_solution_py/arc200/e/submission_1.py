import sys
from itertools import product

def dprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

T = int(input())
MOD = 998244353

def solve_brute(n, m):
    cnt = 0
    detail = [0, 0, 0]
    for x in product(range(1 << m), repeat=n):
        flag = True
        for i in range(n):
            for j in range(i + 1, n):
                if bin(x[i] ^ x[j]).count("1") > 2:
                    flag = False
                    break
        if flag:
            cnt += 1
            if x[0] == 0:
                max_s = 0
                diff = 0
                for i in range(1, n):
                    diff |= x[i] ^ x[0]
                    max_s = max(max_s, bin(x[i] ^ x[0]).count("1"))
                if max_s <= 1:
                    detail[0] += 1
                elif bin(diff).count("1") <= 2:
                    detail[2] += 1
                else:
                    detail[1] += 1
    dprint(*detail)
    return cnt

def solve(n, m):
    ans = 0
    x1 = pow(m + 1, n - 1, MOD) % MOD
    x2 = pow(m, n, MOD) - m * (m - 1) // 2 - m
    x3 = (
        (m * (m - 1) // 2)
        * (pow(4, n - 1, MOD) - pow(3, n - 1, MOD) - 2 * pow(2, n - 1, MOD) + 3)
        % MOD
    )
    x4 = (m * (m - 1) * (m - 2) // 6) * (pow(4, n - 1, MOD) - 4 * pow(2, n - 1, MOD) + 3) % MOD
    ans += x1 + x2 + x3 + x4
    ans %= MOD
    ans *= pow(2, m, MOD)
    ans %= MOD
    dprint(x1, x2, x3, x4)
    return ans

for _ in range(T):
    n, m = map(int, input().split())
    print(solve(n, m))