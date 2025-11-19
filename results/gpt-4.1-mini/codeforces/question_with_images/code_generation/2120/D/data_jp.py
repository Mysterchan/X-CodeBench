MOD = 10**9 + 7

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    # n = a + k - 1
    # m = b + k*(a - 1)
    # これらをMODで割った余りを出力
    n = (a + k - 1) % MOD
    m = (b + k * (a - 1)) % MOD
    print(n, m)